"""
Script to generate human-readable documentation from the WLV schema. 

Reads a Relax NG schema and builds an HTML page for viewing in the browser. 

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
This is simply the HTML container document that will hold the information
retrieved from the Relax NG schema file. 
"""

html ="\
<!doctype html>\
<html lang=\"en\">\
<head>\
<meta charset=\"utf-8\">\
<title>The Wine Label Vocabulary: Schema Documentation</title>\
<meta property=\"og:title\" content=\"The Wine Label Vocabulary: Schema Documentation\">\
<link rel=\"stylesheet\" href=\"style.css\">\
</head>\
<body>\
<h1>The Wine Label Vocabulary: Schema Documentation</h1>\
<div>\
<p>This document documents all elements and attributes included in the Wine Label Vocabulary (WLV) in a human-readable form. This document has been generated automatically from the Relax NG schema.</p>\
</div>\
<h2>1. Elements included in the WLV</h2>\
<div>\
<elements/>\
</div>\
<h2>2. Attributes included in the WLV</h2>\
<div>\
<attributes/>\
</div>\
</body>\
</html>\
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
    elements_html = []
    for name,content in elements.items(): 
        elm_html = ["<h3>"+name+"</h3>",
                    "<p>"+content["documentation"]+"</p>",
                    "<ul>",
                    "<li>Frequency: "+content["frequency"]+"</li>",
                    "<li>Children: "+content["children"]+"</li>",
                    "<li>Attributes: "+content["attributes"]+"</li>",
                    "</ul>"]
        elements_html.append("\n".join(elm_html))       
    elements_html = "\n".join(elements_html)
    return elements_html


def format_attributes(attributes): 
    """
    Creates the entries, written in HTML, for each attributes.
    Returns a string that can be inserted into the empty HTML template. 
    """
    attributes_html = []
    for name,content in attributes.items(): 
        att_html = ["<h3>"+name+"</h3>",
                    "<p>"+content["documentation"]+"</p>",
                    "<ul>",
                    "<li>Frequency: "+content["frequency"]+"</li>",
                    "<li>Values: "+content["values"]+"</li>",
                    "</ul>"]
        attributes_html.append("\n".join(att_html))       
    attributes_html = "\n".join(attributes_html)
    return attributes_html

  
def inject_data(html, elements, attributes): 
    """
    Integrates the information about elements and attributes into the HTML template.
    Returns a string that is a complete HTML document. 
    """
    html = re.sub("<elements/>", elements, html)
    html = re.sub("<attributes/>", attributes, html)
    return html


def save_html(docs): 
    """
    Saves the documentation generated as a HTML document to disk.
    """
    with open("wlv-docs.html", "w", encoding="utf8") as outfile: 
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
    docs = inject_data(html, elements, attributes)
    save_html(docs)

main()



