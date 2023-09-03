"""

Script to create an HTML map with markers for each label in a collection
of wine labels. 

Requires folium, a metadata table and a set of wine label images. 

"""


# === Imports  === 

import folium
import base64
from folium import IFrame
from os.path import join
import pandas as pd
from folium.plugins import MarkerCluster
import glob
import os


# === Files, folders and parameters === 

wdir = join(os.getcwd(), "mapping", "")



# === Functions === 

def initialize_map(): 
    """
    Initializes an empty map with just one marker in Trier.
    initial position is defined here. 
    All further information is added to this map.
    """
    mymap = folium.Map(location=[49.740453759157894, 6.668294112243435], zoom_start=16, tiles="OpenStreetMap")
    marker = folium.Marker(
        [49.756667, 6.641389], 
        popup="Trier (Mosel)", 
        icon=folium.Icon(color="blue", icon="info-sign"))
    marker.add_to(mymap)
    return mymap


def read_metadata(metadatafile): 
    """
    Reads metadata about labels and label images from a CSV file. 
    The file contains: id, label, place, year, lat, long, imagefile, url. 
    """
    with open(metadatafile, "r", encoding="utf8") as infile: 
        metadata = pd.read_csv(infile, sep=";", index_col=0)
    #print(metadata.head())
    return metadata


def add_label(mymap, name, group): 
    """
    This function adds markers with images and text to the map. 
    For each place name, whether with one label or several, this function is called. 
    For each label, an image file is searched in the "img" folder and added. 
    One marker for each place name is added to a marker cluster. 
    The marker cluster is then added to the map. 
    """
    cluster = MarkerCluster(name="place").add_to(mymap)
    for item in group.iteritems(): 
        #print(item[1])
        try: 
            imagefile = glob.glob(join(wdir, "img", item[1].name + "*0600x.jpg"))[0]
            #print(imagefile)
        except: 
            imagefile = join(wdir, "img", "dummy.jpg")
        encoded = base64.b64encode(open(imagefile, 'rb').read()).decode()
        formatstring = "<strong>" + str(item[1]["wineOrigin"]) +\
                       " (" + str(item[1]["wineMillesime"]) + ")</strong> " +\
                       "<a href=\"https://de.wikipedia.org/wiki/Mosel_(Weinanbaugebiet)\" target=\"_blank\">=> weitere Infos</a><br/>" +\
                       '<img src="data:image/png;base64,{}">'
        html = formatstring.format
        iframe = IFrame(html(encoded), width=700, height=500)
        popup = folium.Popup(iframe, max_width=650)
        icon = folium.Icon(color="red", icon="info-sign")
        marker = folium.Marker(location=[item[1]["lat"], item[1]["long"]], popup=popup, icon=icon)
        marker.add_to(cluster)
    return mymap



# === Weingüter mit Markern === 


def read_winemakers(): 
    with open(join(wdir, "data", "mosel_weingueter.csv"), "r", encoding="utf8") as infile: 
        winemakers = pd.read_csv(infile, sep=";", index_col=None)
    return winemakers


def add_winemakers(mymap): 
    winemakers = read_winemakers()
    for item in winemakers.iterrows():
        icon = folium.Icon(color="red", icon="info-sign")
        icontext = item[1]["name"] + " (" + item[1]["gemeinde"] + ")"
        marker = folium.Marker(
            location = [item[1]["lat"], item[1]["long"]], 
            popup = icontext, 
            icon = icon, 
            tooltip = icontext
            )
        marker.add_to(mymap)
    return mymap



# === Etiketten für Piesport === 

def add_piesport(mymap): 
    """
    This function adds a marker for Piesport with several images. 
    """
    imagefile = join(wdir, "img", "mwa-Piesport_0001.jpg")
    encoded = base64.b64encode(open(imagefile, 'rb').read()).decode()
    formatstring = '<img src="data:image/png;base64,{}">'
    html = formatstring.format
    iframe = IFrame(html(encoded), width=700, height=500)
    popup = folium.Popup(iframe, max_width=650)
    icon = folium.Icon(color="red", icon="info-sign")
    marker = folium.Marker(
        location = (49.88023364314281, 6.924762830563002), 
        popup = popup,
        tooltip = "Piesport", 
        icon=icon)
    marker.add_to(mymap)
    return mymap






# === Weinlagen mit Polygon ===


def define_lagen(): 
    lagen = [{
        "name" : "St. Maximiner Kreuzberg (Trier)",
        "polygon" : [
            (49.74820954217373, 6.653151604368142), 
            (49.746965326200566, 6.6529044777532595), 
            (49.74677296412426, 6.653007232930956), 
            (49.74659917041536, 6.653286013455679), 
            (49.74521419434047, 6.651954907053104), 
            (49.74605448666682, 6.6499571920033835),
            (49.7464206566979, 6.649501637239448),
            (49.74680977408599, 6.649736663564916),
            (49.747041305872216, 6.649367729226153),
            (49.74789390759729, 6.649854996899384),
            (49.747786903783194, 6.650364153089779),
            (49.74819009996053, 6.650666877957927),
            ]},
            {
        "name" : "Deutschherrenberg (Trier)",
        "polygon" : [
            (49.74655798994467, 6.653388762929856),
            (49.746555021572796, 6.654089103335911),
            (49.74685457084772, 6.654871403446343),
            (49.747157109443336, 6.655435776845783),
            (49.747075157241895, 6.656321328196155),
            (49.7473821113339, 6.656384952891889),
            (49.747452007686654, 6.658078035065125),
            (49.74774704378746, 6.659406223656299),
            (49.74481481686979, 6.660789853396877),
            (49.74455107832864, 6.659770309497866),
            (49.74395303323706, 6.655578231917966),
            (49.74458166153261, 6.6557648763329205),
            (49.74485719079146, 6.65493854348916),
            (49.74540939698355, 6.654671487785074),
            (49.744542413120875, 6.653520521823592),
            (49.74524157616657, 6.651903748173637),
            ]},
            {
        "name" : "Deutschherrenköpfchen (Trier)",
        "polygon" : [
            (49.74540500551935, 6.654504780520199),
            (49.74485537513191, 6.6548962301962575),
            (49.7445681332608, 6.655704796120304),
            (49.743914040950166, 6.655405217293984),
            (49.744125925291186, 6.6545622228418475),
            (49.74419328210623, 6.653935464855505),
            (49.744547016792396, 6.653480890787323),
            ]},
             ]
    return lagen




def add_vineyards(mymap):
    lagen = define_lagen()
    for lage in lagen: 
        folium.Polygon(lage["polygon"],
            popup = lage["name"], 
            tooltip = lage["name"],
            color = "blue",
            weight = 4,
            fill = True, 
            fill_color = "green", 
            fill_opacity = 0.4,
            ).add_to(mymap)
    return mymap



def save_map(mymap, filename): 
    """
    Saves the finished map to a standalone HTML file. 
    All image information is included in this HTML file. 
    """
    mymap.save(filename)


# === Main === 


def main(): 
    """
    Coordinates the creation of a wine label map.
    """
    mymap = initialize_map()
    add_winemakers(mymap)
    add_piesport(mymap)
    metadata = read_metadata(join(wdir, "data", "mosel-metadata.csv"))
    metadata_grouped = metadata.groupby("wineOrigin")
    for name,group in metadata_grouped: 
        print(str(len(group)) + "x", name)
        mymap = add_label(mymap, name, group.T)
    add_vineyards(mymap)
    save_map(mymap, join(wdir, "mosel-map_v4.html"))

main()
