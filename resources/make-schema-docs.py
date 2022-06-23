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
## WLV Schema Documentation\n\n\
This document documents all elements and attributes included in the Wine Label Vocabulary (WLV) in a human-readable form. This document has been generated automatically from the Relax NG schema.\n\n\
For more information on the WLV, see https://github.com/dh-trier/wlv\n\n\
### Contents\n\n\
1. [Quicklinks](#Quicklinks)\n\
1. [Elements](#Elements)\n\
2. [Attributes](#Attributes)\n\n\
### Quicklinks\n\n\
**Elements**: <list_elements/>\n\n\
**Attributes**: <list_attributes/>\n\n\
### Elements\
<elements/>\n\n\
### Attributes\n\n\
<attributes/>\n\
"


# === Functions


def read_md(mdfile): 
    """
    Open and read a Markdown file. 
    Returns the content of the file as a string. 
    """
    with open(mdfile, "r", encoding="utf8") as infile: 
        md = infile.read()
        return md


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
            atts = ["["+hit+"](#"+hit+")" for hit in hits if hit in att_names]
            elms = ["["+hit+"](#"+hit+")" for hit in hits if hit in elm_names]
            # atts
            elements[elm]["attributes"] = ", ".join(atts)
            if len(atts) == 0: 
                elements[elm]["attributes"] = "This element has no attributes"
            # children
            elements[elm]["children"] = ", ".join(elms)
            if len(elms) == 0: 
                elements[elm]["children"] = "This element has no children"
        except: 
            elements[elm]["attributes"] = "(no data)"
            elements[elm]["children"] = "(no data)"

       
        # Contained by element
        
        try: 
            if elm == "wlv": 
                containedby = ["This is the root element"]
            else: 
                containedby = rng.xpath("//rng:element//rng:ref[@name='"+elm+"']/../../@name", namespaces=ns)
                #print("1", elm, containedby)
                if len(containedby) == 0: 
                    containedby = rng.xpath("//rng:element//rng:ref[@name='"+elm+"']/../../../@name", namespaces=ns)
                    #print("2", elm, containedby)
                    if len(containedby) == 0: 
                        containedby = rng.xpath("//rng:element//rng:ref[@name='"+elm+"']/../../../../@name", namespaces=ns)
                        #print("3", elm, containedby)
                        if len(containedby) == 0: 
                            containedby = ["(no data)"]
                            #print("4", elm, containedby)
                containedby = ["["+item+"](#"+item+")" for item in containedby]
        except: 
            containedby = ["(no data)"]
            #print("5", elm, containedby)
        #print("6", elm, containedby)
        elements[elm]["containedby"] = ", ".join(containedby)


        # Frequency of element
        try: 
            result = rng.xpath("name(//rng:element//rng:ref[@name='"+elm+"']/..)", namespaces=ns)
            if result == "element": 
                status = "Mandatory"
                frequency = "Exactly once"
            elif result == "optional": 
                status = "Optional"
                frequency = "Once at most"
            elif result == "zeroOrMore": 
                status = "Optional"
                frequency = "Zero, once or several times"
            elif result == "oneOrMore": 
                status = "Mandatory"
                frequency = "Once or several times"
            #print("1", elm, frequency)
            elements[elm]["status"] = status
            elements[elm]["frequency"] = frequency
        except: 
            frequency = "(no data)"
            status = "(no data)"
            #print("2", elm, frequency)
            elements[elm]["status"] = status
            elements[elm]["frequency"] = frequency
            
    
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
            
        # attribute values
        try: 
            vals = rng.xpath("//rng:define[@name='"+att+"']//rng:value/text()", namespaces=ns)
            if len(vals) == 0: 
                attributes[att]["values"] = "This element has no default values"
            elif len(vals) < 5: 
                attributes[att]["values"] = ", ".join(vals)
            else: 
                attributes[att]["values"] = "\n    * ".join(vals)
                attributes[att]["values"] = "\n    * " + attributes[att]["values"]
        except: 
            attributes[att]["attributes"] = "No data found"

        
        # Contained by element
        
        if att[0:4] == "font": 
            attributes[att]["containedby"] = "All elements contained by [textual](#textual)" 
        else:
            try: 
                containedby = rng.xpath("//rng:element//rng:ref[@name='"+att+"']/../../@name", namespaces=ns)
                #print("1", elm, containedby)
                if len(containedby) == 0: 
                    containedby = rng.xpath("//rng:element//rng:ref[@name='"+att+"']/../../../@name", namespaces=ns)
                    #print("2", elm, containedby)
                    if len(containedby) == 0: 
                        containedby = rng.xpath("//rng:element//rng:ref[@name='"+att+"']/../../../../@name", namespaces=ns)
                        #print("3", elm, containedby)
                        if len(containedby) == 0: 
                            containedby = ["(no data)"]
                            #print("4", elm, containedby)
                containedby = ["["+item+"](#"+item+")" for item in containedby if item != "(no data)"]
            except: 
                containedby = ["(no data)"]
                #print("5", elm, containedby)
            #print("6", elm, containedby)
            if len(containedby) < 5: 
                attributes[att]["containedby"] = ", ".join(containedby)
            else: 
                attributes[att]["containedby"] = "\n    * ".join(containedby)
                attributes[att]["containedby"] = "\n    * " + attributes[att]["containedby"]

        # Status of attribute
        if att[0:4] == "font": 
            attributes[att]["status"] = "Optional"
        else: 
            try: 
                result = rng.xpath("name(//rng:element//rng:ref[@name='"+att+"']/..)", namespaces=ns)
                if result == "element": 
                    status = "Mandatory"
                elif result == "optional": 
                    status = "Optional"
                elif result == "zeroOrMore": 
                    status = "Optional"
                #print("1", att, status)
                attributes[att]["status"] = status
            except:
                status = "(no data)"
                #print("2", att, status)
                attributes[att]["status"] = status

           
    attributes_sorted = dict(sorted(attributes.items()))
    return attributes_sorted



def format_elements(elements): 
    """
    Creates the entries, written in HTML, for each element.
    Returns a string that can be inserted into the empty HTML template. 
    """
    elements_md = []
    for name,content in elements.items(): 
        elm_md = ["\n#### "+name,
                    "\n" + content["documentation"]+"\n",
                    "- Status: " + content["status"]+".",
                    "- Frequency: " + content["frequency"]+".",
                    "- Contained by element(s): " + content["containedby"]+".",
                    "- Contains element(s): " + content["children"]+".",
                    "- Has attribute(s): " + content["attributes"]+"."]
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
        att_md = ["\n#### "+name,
                    content["documentation"]+"\n",
                    "- Status: " + content["status"] + ".",
                    "- Contained by element: " + content["containedby"] + ".",
                    "- Possible values: "+content["values"]+"."]
        attributes_md.append("\n".join(att_md))       
    attributes_md = "\n".join(attributes_md)
    return attributes_md

  
def inject_data(intro, md, elements, attributes, elm_names, att_names): 
    """
    Integrates the information about elements and attributes into the HTML template.
    Returns a string that is a complete HTML document. 
    """
    elmstring = ", ".join(["["+item+"](#"+item+")" for item in sorted(elm_names)])
    attstring = ", ".join(["["+item+"](#"+item+")" for item in sorted(att_names)])
    md = re.sub("<list_elements/>", elmstring, md)
    md = re.sub("<list_attributes/>", attstring, md)
    md = re.sub("<elements/>", elements, md)
    md = re.sub("<attributes/>", attributes, md)
    md = intro + "\n\n" + md
    return md


def save_md(docs, docsfile): 
    """
    Saves the documentation generated as a HTML document to disk.
    """
    with open(docsfile, "w", encoding="utf8") as outfile: 
        outfile.write(docs)
 


# === Main

def main(): 
    """
    Coordinates the process.
    """
    mdfile = join("resources", "wlv-introduction.md")
    rngfile = join("resources", "wlv-label-schema.rng")
    docsfile = join("resources", "wlv-label-docs.md")
    ns = {'rng':'http://relaxng.org/ns/structure/1.0',
          'a':'http://relaxng.org/ns/compatibility/annotations/1.0'}
    rng = open_file(rngfile) 
    elm_names, att_names = get_names(rng, ns)
    elements = extract_elminfo(rng, elm_names, ns, att_names)
    attributes = extract_attinfo(rng, att_names, ns)
    elements = format_elements(elements)
    attributes = format_attributes(attributes)
    intro = read_md(mdfile)
    docs = inject_data(intro, md, elements, attributes, elm_names, att_names)
    save_md(docs, docsfile)

main()



