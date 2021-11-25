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


# === Markdown template

"""
This is simply the Markdown container document that will hold the information
retrieved from the Relax NG schema file. 

TODO: Add table of contents with links to elements and attributes. 
"""

md ="\
# The Wine Label Vocabulary: Schema Documentation\n\n\
This document documents all elements and attributes included in the Wine Label Vocabulary (WLV) in a human-readable form. This document has been generated automatically from the Relax NG schema.\n\n\
For more information on the WLV, see https://github.com/dh-trier/wlv\n\n\
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


def get_names(rng, ns): 
    """
    Extracts the complete list of elements and attributes from the schema file.
    Returns two lists. 
    """
    elm_names = rng.findall(".//rng:element/rng:name", namespaces=ns)
    elm_names = [elm.text for elm in elm_names]
    
    att_names = rng.findall(".//rng:attribute/rng:name", namespaces=ns)
    att_names = [att.text for att in att_names]
    
    #elm_names = ["wlv", "curation", "metadata", "collectionContext", "labelPart", "figure"]
    #att_names = ["curationDate", "curationUpdate", "labelID", "collectionID", "figureNum"]
    return elm_names, att_names
    

def extract_elminfo(rng, elm_names, ns, att_names):
    """
    Extracts relevant information for each element from the RNG file.
    Returns a dictionary that holds the elements in alphabetical order. 
    TODO: Write the XPath expressions for more pieces of information.
    -- Is the element mandatory or optional etc.?
    """
    elements = {}
    for elm in elm_names: 
        elements[elm] = {}
        # documentation
        try: 
            elements[elm]["documentation"] = rng.xpath("//rng:define[@name='"+elm+"']/a:documentation/text()", namespaces=ns)[0]
        except: 
            elements[elm]["documentation"] = "(no data)" 
        
        # attributes and children
        try: 
            hits = rng.xpath("//rng:define[@name='"+elm+"']/rng:element//rng:ref/@name", namespaces=ns)
            atts = [hit for hit in hits if hit in att_names]
            elms = [hit for hit in hits if hit in elm_names]
            # atts
            elements[elm]["attributes"] = ", ".join(atts)
            if len(atts) == 0: 
                elements[elm]["attributes"] = "This element has no attributes."
            # children
            elements[elm]["children"] = ", ".join(elms)
            if len(elms) == 0: 
                elements[elm]["children"] = "This element has no children."
        except: 
            elements[elm]["attributes"] = "No data found."
            elements[elm]["children"] = "No data found."

        elements[elm]["frequency"] = "tbc."
        #elements[elm]["children"] = "tbc."
    
    elements_sorted = dict(sorted(elements.items()))
    return elements_sorted


def extract_attinfo(rng, att_names, ns):
    """
    Extracts relevant information for each attribute from the RNG file.
    Returns dictionary that holds the attributes in alphabetical order. 
    TODO: Write the XPath expressions for more pieces of information.
    -- What values are default / mandatory for the attribute?
    -- Is the attribute mandatory, optional, etc.?
    """
    attributes = {}
    for att in att_names: 
        attributes[att] = {}
        
        # documentation
        try: 
            attributes[att]["documentation"] = rng.xpath("//rng:define[@name='"+att+"']/a:documentation/text()", namespaces=ns)[0]
        except: 
            attributes[att]["documentation"] = "(no data)"
            
        # values
        try: 
            vals = rng.xpath("//rng:define[@name='"+att+"']//rng:value/text()", namespaces=ns)
            attributes[att]["values"] = ", ".join(vals)
            if len(vals) == 0: 
                attributes[att]["values"] = "This element has no default values."
        except: 
            attributes[att]["attributes"] = "No data found."

        
        attributes[att]["frequency"] = "tbc."
        #attributes[att]["values"] = "tbc."
            
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
                    "\n" + content["documentation"]+"\n",
                    "- Child element(s): "+content["children"],
                    "- Attribute(s): "+content["attributes"]]
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
    with open(join("..", "wlv-docs.md"), "w", encoding="utf8") as outfile: 
        outfile.write(docs)
 
 
# === Main

def main(): 
    """
    Coordinates the process.
    """
    ns = {'rng':'http://relaxng.org/ns/structure/1.0',
          'a':'http://relaxng.org/ns/compatibility/annotations/1.0'}
    rng = open_file(rngfile=join("..", "..", "schemas", "wlv-label-schema.rng")) 
    elm_names, att_names = get_names(rng, ns)
    elements = extract_elminfo(rng, elm_names, ns, att_names)
    attributes = extract_attinfo(rng, att_names, ns)
    elements = format_elements(elements)
    attributes = format_attributes(attributes)
    docs = inject_data(md, elements, attributes)
    save_md(docs)

main()



