"""

Script to create an HTML map with markers for each label in a collection
of wine labels. 

Requires folium, a metadata table and a set of wine label images. 

"""


# === Imports 

import folium
import base64
from folium import IFrame
from os.path import join
import pandas as pd
from folium.plugins import MarkerCluster


# === Functions

def initialize_map(): 
    """
    Initializes an empty map with just one marker in Trier.
    All further information is added to this map.
    """
    mymap = folium.Map(location=[49.9, 6.7], zoom_start=10, tiles="OpenStreetMap")
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
        metadata = pd.read_csv(infile, sep=";")
    #print(metadata.head())
    return metadata


def add_label(mymap, name, group): 
    """
    This function adds markers with images and text to the map. 
    For each place name, whether with one label or several, this function is called. 
    One marker for each place name is added to a marker cluster. 
    The marker cluster is then added to the map. 
    """
    cluster = MarkerCluster(name="place").add_to(mymap)
    for item in group.iteritems(): 
        encoded = base64.b64encode(open(join("..", "img", item[1]["imagefile"]), 'rb').read()).decode()
        formatstring = "<strong>" + str(item[1]["label"]) +\
                       " (" + str(item[1]["year"]) + ")</strong> " +\
                       "<a href=\"" + str(item[1]["url"]) +"\" target=\"_blank\">=> weitere Infos</a><br/>" +\
                       '<img src="data:image/png;base64,{}">'
        html = formatstring.format
        iframe = IFrame(html(encoded), width=700, height=500)
        popup = folium.Popup(iframe, max_width=650)
        icon = folium.Icon(color="red", icon="info-sign")
        marker = folium.Marker(location=[item[1]["lat"], item[1]["long"]], popup=popup, icon=icon)
        marker.add_to(cluster)
    return mymap


def save_map(mymap): 
    """
    Saves the finished map to a standalone HTML file. 
    All image information is included in this HTML file. 
    """
    mymap.save("wlv-map.html")


# === Main

def main(): 
    """
    Coordinates the creation of a wine label map.
    """
    mymap = initialize_map()
    metadata = read_metadata(join("..", "metadata.csv"))
    metadata_grouped = metadata.groupby("place")
    for name,group in metadata_grouped: 
        mymap = add_label(mymap, name, group.T)
    save_map(mymap)

main()
