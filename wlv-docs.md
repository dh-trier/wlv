## Introduction 

This file describes the "Wine Label Vocabulary" (WLV) used in the project "Weinetiketten im Wandel" at the Trier Center for Digital Humanities. 

Note that the WLV does not describe the wine or the bottle, but specifically the labels. 

The WLV is documented as a Relax NG schema in the compact, flat syntax. See the file ```wlv-schema.rnc```. 

The basic idea is that each XML file contains the description of one collection of labels. Each label can have several parts (like the front and back labels). Each part has three layers of description: physical, visual and textual. 

Within the visual layer, element content is used to describe the figures visible on the label. Within the textual layer, element content is used to replicate the textual contents of the label. The physical layer does not have element content. 


## Overview of elements and structure

wlv

- metadata

-- title

-- editor 

-- institution

-- location

-- date 

-- licence @short

-- curators

--- curatorID 

- labels

-- label @curatorID @curationDate @comment

--- part

---- physical @shape @sizeH @sizeV @material

---- visual

----- frame @frameType

----- background

----- figure

---- textual

----- millesime

----- wineOrigin

----- wineType

----- wineGrapes

----- wineTaste

----- wineAging

----- wineOther

----- qualityGrapes

----- qualityLevel

----- qualityAward

----- qualityProduction

----- qualityHistorical



----- agent

----- location



----- alcohol

----- volume 

----- controlNumber

----- barrelNumber

----- labelNumber 


----- motto

----- coatText

----- otherText



## Attributes present on most elements inside the element textual

@{elementname}Norm or @{elementname}Type

@ref: For a reference to an authority such as GND, Geonames, Wikidata or a Wikipedia page.

@url: For a reference to a website about or by the instance mentioned.  

@fontType: { "Antiqua-Sans" | "Antiqua-Serif" | "Fraktur" | "Cursive" }

@fontSize: { "larger" | "normal" | "smaller" }

@fontStyle: { "recte" | "italic" | "bold" | "smallcaps" | "allcaps" | "other" }

@fontColor: { "red" | "black" | text }

@intialColor: { "red" | "black" | text }




