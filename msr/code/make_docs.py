"""
Script to generate human-readable documentation from the WLV schema. 

Reads a Relax NG schema and builds a Markdown page for viewing in the browser. 

"""


# === Imports 

import pandas as pd
import glob
from os.path import join
import xml.etree.ElementTree as ET
import lxml
from lxml import etree
import re


# === HTML template

"""
This is simply the Markdown container document that will hold the information
retrieved from the Relax NG schema file. 

TODO: Add table of contents with links to elements and attributes. 
"""

md ="\
# The Wine Label Vocabulary: Schema Documentation\n\n\
This document documents all elements and attributes included in the Wine Label Vocabulary (WLV) in a human-readable form. This document has been generated automatically from the Relax NG schema.\n\n\
## 1. Elements included in the WLV\n\n\
<elements/>\n\n\
## 2. Attributes included in the WLV\n\n\
<attributes/>\n\
"


# === Functions


def open_file(rngfile): 
    """
    Open and parse the Relax NG file. 
    Returns an XML tree.
    """
    with open(rngfile, "r", encoding="utf8") as infile:
        rng = etree.parse(infile)
        return rng


def get_names(rng): 
    """
    Defines the elements and attributes to include. 
    Returns two lists. 
    TODO: Extract these two lists from the schema file. 
    """
    elm_names = ["wlv", "curation", "metadata", "collectionContext", "labelPart", "figure"]
    att_names = ["curationDate", "curationUpdate", "labelID", "collectionID", "figureNum"]
    return elm_names, att_names
    

def extract_elminfo(rng, elm_names):
    """
    Extracts relevant information for each element from the RNG file.
    Returns dictionary that holds the elements in alphabetical order. 
    TODO: Write the XPath expressions for more pieces of information.
    """
    elements = {}
    # Namespaces
    namespaces = {'rng':'http://relaxng.org/ns/structure/1.0',
                  'a':'http://relaxng.org/ns/compatibility/annotations/1.0'}
    for elm in elm_names: 
        try: 
            elements[elm] = {"documentation" : rng.xpath("//rng:define[@name='"+elm+"']/a:documentation/text()", namespaces=namespaces)[0],
                             "frequency" : "tbc.",
                             "children" : "tbc.",
                             "attributes" : "tbc."}
        except: 
            print("Error when trying to find data for element", elm)
    
    elements_sorted = dict(sorted(elements.items()))
    return elements_sorted


def extract_attinfo(rng, att_names):
    """
    Extracts relevant information for each attribute from the RNG file.
    Returns dictionary that holds the attributes in alphabetical order. 
    TODO: Write the XPath expressions for more pieces of information.
    """
    attributes = {}
    # Namespaces
    namespaces = {'rng':'http://relaxng.org/ns/structure/1.0',
                  'a':'http://relaxng.org/ns/compatibility/annotations/1.0'}
    for att in att_names: 
        try: 
            attributes[att] = {"documentation" : rng.xpath("//rng:define[@name='"+att+"']/a:documentation/text()", namespaces=namespaces)[0],
                               "frequency" : "tbc.",
                               "values" : "tbc."}
        except: 
            print("Error when trying to find data for attribute", att)
            
    attributes_sorted = dict(sorted(attributes.items()))
    return attributes_sorted



def format_elements(elements): 
    """
    Creates the entries, written in HTML, for each element.
    Returns a string that can be inserted into the empty HTML template. 
    """
    elements_md = []
    for name,content in elements.items(): 
        elm_md = ["\n### "+name,
                    content["documentation"]+"\n",
                    "- Frequency: "+content["frequency"],
                    "- Children: "+content["children"],
                    "- Attributes: "+content["attributes"]]
        elements_md.append("\n".join(elm_md))
    elements_md = "\n".join(elements_md)
    return elements_md


def format_attributes(attributes): 
    """
    Creates the entries, written in HTML, for each attributes.
    Returns a string that can be inserted into the empty HTML template. 
    """
    attributes_md = []
    for name,content in attributes.items(): 
        att_md = ["\n### "+name,
                    content["documentation"]+"\n",
                    "- Frequency: "+content["frequency"],
                    "- Values: "+content["values"]]
        attributes_md.append("\n".join(att_md))       
    attributes_md = "\n".join(attributes_md)
    return attributes_md

  
def inject_data(md, elements, attributes): 
    """
    Integrates the information about elements and attributes into the HTML template.
    Returns a string that is a complete HTML document. 
    """
    md = re.sub("<elements/>", elements, md)
    md = re.sub("<attributes/>", attributes, md)
    return md


def save_md(docs): 
    """
    Saves the documentation generated as a HTML document to disk.
    """
    with open("wlv-docs.md", "w", encoding="utf8") as outfile: 
        outfile.write(docs)
 
 
# === Main

def main(): 
    """
    Coordinates the process.
    """
    rng = open_file(rngfile=join("..", "..", "schemas", "wlv-label-schema.rng")) 
    elm_names, att_names = get_names(rng)
    elements = extract_elminfo(rng, elm_names)
    attributes = extract_attinfo(rng, att_names)
    elements = format_elements(elements)
    attributes = format_attributes(attributes)
    docs = inject_data(md, elements, attributes)
    save_md(docs)

main()



