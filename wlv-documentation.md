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

-- editor @ref

-- institution

-- location @ref

-- date @dateNorm

-- licence @url

-- curators

--- curatorID @ref

- labels

-- label

--- part

---- physical

----- shape @sizeH @sizeV

----- material

---- visual

----- frame @frameStyle @frameType

----- background @backgroundStyle

----- figure

---- textual

----- millesime

----- grape-variety @ref

----- qualityIndicator @qualityIndicatorType

----- wineCharacter

----- wineColor

----- agent @ref

----- location @ref

----- motto

----- alcohol @alcoholNorm

----- volume @volumeNorm

----- controlNumber @controlNumberType

----- barrelNumber

----- otherText @otherTextType


## Attributes present on most elements inside the element textual

@fontType: { "Antiqua-Sans" | "Antiqua-Serif" | "Fraktur" | "Cursive" }

@fontSize: { "larger" | "normal" | "smaller" }

@fontStyle: { "recte" | "italic" | "bold" | "smallcaps" | "allcaps" | "other" }

@fontColor: { "red" | "black" | text }

@intialColor: { "red" | "black" | text }




