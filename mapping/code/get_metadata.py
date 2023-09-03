"""
Script to extract metadata from wine label descriptions in XML. 

Provides data required for mapping of labels: 
- wineMillesime (year)
- wineOrigin (place)
- latitude and longitude (from a CSV)

Uses Element Tree to identify data in the XML file as a lightweight
alternative to XPath with the lxml library.

Saves all metadata to a CSV file. 

"""


# === Imports 

import pandas as pd
import glob
from os.path import join
import xml.etree.ElementTree as ET


# === Functions
 
def extract_metadata(xml):
    """
    Extract the required metadata from each XML label description. 
    Returns a dict. 
    """
    data = {}
    
    for element in xml.iter():         
        # wineMillesime
        if element.tag == "wineMillesime":
            try: 
                data["wineMillesime"] = element.attrib["wineMillesimeNorm"]
            except:
                try: 
                    data["wineMillesime"] = element.text
                except: 
                    data["wineMillesime"] = "unb."
        # wineOrigin
        if element.tag == "wineOrigin": 
            try: 
                data["wineOrigin"] = element.attrib["wineOriginNorm"]
            except: 
                try: 
                    data["wineOrigin"] = element.text
                except: 
                    data["wineOrigin"] = "unb."


        # Fill in placeholder for elements missing altogether
        try: 
            data["wineMillesime"]
        except:             
            data["wineMillesime"] = "unb."
        try: 
            data["wineOrigin"]
        except: 
            data["wineOrigin"] = "unb."
    
    return data


def read_latlong():
    """
    Reads the CSV file with latitude and longitude information for 
    relevant localities in the Mosel region. 
    Returns a DataFrame.
    """
    with open("lat-long.csv", "r", encoding="utf8") as infile: 
        latlong = pd.read_csv(infile, sep=";", index_col="place")
    #print(latlong)
    return latlong


def add_latlong(metadata, labelid, latlong): 
    """
    Adds the information about latitude and longitude from the 
    CSV file to the metadata of a given label. 
    Returns the metadata dict object. 
    """
    data = metadata[labelid]
    wineOrigin = data["wineOrigin"]
    metadata[labelid]["lat"] = latlong.loc[wineOrigin, "lat"]
    metadata[labelid]["long"] = latlong.loc[wineOrigin, "long"]
    return metadata


def save_metadata(metadata): 
    """
    Transforms the dict of dicts with all the label metadata to a DataFrame. 
    Saves the DataFrame to a CSV file for further use by the mapping script.
    """
    metadata = pd.DataFrame(metadata).T
    print(metadata)
    with open(join("..", "msr-metadata.csv"), "w", encoding="utf8") as outfile: 
        metadata.to_csv(outfile, sep=";")


# === Main    

def main(): 
    """
    Coordinates the metadata collection.
    """
    metadata = {}
    latlong = read_latlong()
    for xmlfile in glob.glob(join("..", "xml", "*.xml")):
        if "collection" not in xmlfile:  
            #print(xmlfile)
            xml = ET.parse(xmlfile).getroot()
            labelid = xml.attrib["labelID"]
            metadata[labelid] = extract_metadata(xml)
            metadata = add_latlong(metadata, labelid, latlong)
    save_metadata(metadata)

main()




