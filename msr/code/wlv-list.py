import pandas as pd
import glob
from os.path import join
import xml.etree.ElementTree as ET

 
def extract_metadata(xml):
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
                    data["wineMillesime"] = "(no data)"
        # wineOrigin
        if element.tag == "wineOrigin": 
            try: 
                data["wineOrigin"] = element.attrib["wineOriginNorm"]
            except: 
                try: 
                    data["wineOrigin"] = element.text
                except: 
                    data["wineOrigin"] = "(no data)"

        # Fill in placeholder for elements missing altogether
        try: 
            data["wineMillesime"]
        except:             
            data["wineMillesime"] = "(no data)"
        try: 
            data["wineOrigin"]
        except: 
            data["wineOrigin"] = "(no data)"
    
    return data


def save_metadata(metadata): 
    metadata = pd.DataFrame(metadata).T
    print(metadata)
    with open(join("..", "msr-metadata.csv"), "w", encoding="utf8") as outfile: 
        metadata.to_csv(outfile, sep=";")
    


def main(): 
    metadata = {}
    for xmlfile in glob.glob(join("..", "xml", "*.xml")):
        if "collection" not in xmlfile:  
            #print(xmlfile)
            xml = ET.parse(xmlfile).getroot()
            labelid = xml.attrib["labelID"]
            metadata[labelid] = extract_metadata(xml)
    save_metadata(metadata)

main()




