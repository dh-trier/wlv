# The Wine Label Vocabulary: Schema Documentation

This document documents all elements and attributes included in the Wine Label Vocabulary (WLV) in a human-readable form. This document has been generated automatically from the Relax NG schema.

For more information on the WLV, see https://github.com/dh-trier/wlv

## Contents

1. [Elements](#Elements)
2. [Attributes](#Attributes)

## Elements


### agent

(no data)

- Child element(s): This element has no children.
- Attribute(s): agentRole, ref, uri

### alcohol

(no data)

- Child element(s): This element has no children.
- Attribute(s): alcoholNorm

### background

Information about the background of the label. Needs to be filled in only if there is some special background, other than the blank paper, to the visual and/or textual information provided. 

- Child element(s): This element has no children.
- Attribute(s): backgroundStyle

### barrelNumber

(no data)

- Child element(s): This element has no children.
- Attribute(s): This element has no attributes.

### collection

The wine label collection the label belongs to.

- Child element(s): This element has no children.
- Attribute(s): collectionID

### collectionContext

Any information that describes the individual label in the context of the collection, for example its location in the collection.

- Child element(s): This element has no children.
- Attribute(s): pageID, scanID

### comments

(no data)

- Child element(s): This element has no children.
- Attribute(s): This element has no attributes.

### conservation

(no data)

- Child element(s): This element has no children.
- Attribute(s): conservationNorm

### controlNumber

(no data)

- Child element(s): This element has no children.
- Attribute(s): ref, controlNumberType

### curation

Information on the curation process of the wine label description.

- Child element(s): This element has no children.
- Attribute(s): curatorID, curationDate, curationUpdate

### dating

(no data)

- Child element(s): This element has no children.
- Attribute(s): year, notBefore, notAfter, certainty

### figure

(figure) Any visual, figurative element on the label. The label is classified as to its type and position using the attributes. It can be described in the element content using a simple list of terms mentioning each recognizable element of the figure. (In a future iteration of WLV, a controlled vocabulary of visual elements commonly found on wine labels will be made available for this purpose.)

- Child element(s): figureItem
- Attribute(s): figureNum, figureType, figurePosition

### figureItem

(figure item) A visual element or depicted object that can be identified in the figure.

- Child element(s): This element has no children.
- Attribute(s): itemData

### frame

Information about the frame of the label.

- Child element(s): This element has no children.
- Attribute(s): frameType, frameStyle, frameColor

### label

The main container for information about the label. A label must have at least one part, but can have several parts.

- Child element(s): comments, labelPart, provenance
- Attribute(s): labelType

### labelNumber

(no data)

- Child element(s): This element has no children.
- Attribute(s): This element has no attributes.

### labelPart

(label part) Any physically separate part of the label / labeling.

- Child element(s): physical, visual, textual
- Attribute(s): partNum, partType

### licence

(no data)

- Child element(s): This element has no children.
- Attribute(s): uri, licenceAbbr, licenceScope

### location

(no data)

- Child element(s): This element has no children.
- Attribute(s): locationType, locationRole, locationNorm, locationRegNr, figureNum, ref, uri

### metadata

One of two mandatory top-level elements. Contains metadata related to the label description itself.

- Child element(s): collection, curation, licence, collectionContext, comments
- Attribute(s): uri

### otherText

(no data)

- Child element(s): This element has no children.
- Attribute(s): textType, textPosition, figureNum

### physical

Information regarding the physical aspects of the label, in particular shape, size and material.

- Child element(s): This element has no children.
- Attribute(s): shape, sizeH, sizeV, material, printingTechnique

### provenance

(no data)

- Child element(s): dating, source, scan, conservation
- Attribute(s): This element has no attributes.

### qualityAward

(no data)

- Child element(s): This element has no children.
- Attribute(s): ref, wdw, qualityAwardNorm

### qualityGrapes

(no data)

- Child element(s): This element has no children.
- Attribute(s): ref, wdw, qualityGrapesNorm

### qualityHistorical

(no data)

- Child element(s): This element has no children.
- Attribute(s): wdw, ref

### qualityLabel

(no data)

- Child element(s): This element has no children.
- Attribute(s): ref, wdw, qualityLabelType

### qualityLevel

(no data)

- Child element(s): This element has no children.
- Attribute(s): ref, wdw, qualityLevelNorm

### qualityProduction

(no data)

- Child element(s): This element has no children.
- Attribute(s): ref, wdw, qualityProductionNorm

### scan

(no data)

- Child element(s): This element has no children.
- Attribute(s): scanID

### source

(no data)

- Child element(s): This element has no children.
- Attribute(s): year

### textual

(no data)

- Child element(s): wineMillesime, wineName, wineGrapes, wineTaste, wineAging, wineOther, qualityGrapes, qualityLevel, qualityAward, qualityLabel, qualityProduction, qualityHistorical, agent, location, alcohol, volume, controlNumber, barrelNumber, labelNumber, otherText
- Attribute(s): This element has no attributes.

### visual

Any visual and non-textual or non-linguistic elements discernible on the label.

- Child element(s): frame, background, figure
- Attribute(s): This element has no attributes.

### volume

(no data)

- Child element(s): This element has no children.
- Attribute(s): volumeNorm

### wineAging

(no data)

- Child element(s): This element has no children.
- Attribute(s): wineAgingNorm, ref, wdw

### wineColor

(no data)

- Child element(s): This element has no children.
- Attribute(s): wineColorNorm, ref, wdw

### wineGrapes

(no data)

- Child element(s): This element has no children.
- Attribute(s): wineGrapesNorm, ref, wdw

### wineMillesime

The year that the wine was harvested in.

- Child element(s): This element has no children.
- Attribute(s): wineMillesimeNorm

### wineName

The name of the wine. Typically printed in a somewhat larger font size than other information. For historical wine labels of the Mosel region, the wine name is typically composed of a location  (Ort, Gemeinde, Leitgemeinde) and the name or nickname of the specific vineyard belonging to that location. Note that the element 'wineName' has, as a consequence, an empty child element 'location' that can appear more than once and may hold information about the location and the vineyard separately. 

- Child element(s): location
- Attribute(s): wineNameType, wineNameNorm, ref, uri, wdw

### wineOther

(no data)

- Child element(s): This element has no children.
- Attribute(s): wineOtherType, ref

### wineTaste

(no data)

- Child element(s): This element has no children.
- Attribute(s): ref, wdw

### wlv

The root element in a label description using the Wine Label Vocabulary.

- Child element(s): metadata, label
- Attribute(s): labelID

## Attributes


### agentRole
(no data)

- Values: cultivation / Anbau, production / Weinbau, distribution / Vertrieb, cooperative / Kooperative, printer / Drucker, artist / Künstler/in, multiple / verschiedene, other / andere

### alcoholNorm
(no data)

- Values: This element has no default values.

### backgroundStyle
(no data)

- Values: pattern, color, none

### certainty
(no data)

- Values: source, evidence, estimate, low

### collectionID
A unique identifier for the wine label collection.

- Values: This element has no default values.

### conservationNorm
(no data)

- Values: new, like new, very good, good, acceptable, damaged, incomplete

### controlNumberType
(no data)

- Values: Amtliche Prüfnummer (Q480240), Losnummer, other

### curationDate
The date (or year) when the wine label description was created.

- Values: This element has no default values.

### curationUpdate
The date (or year) when the wine label description was last updated.

- Values: This element has no default values.

### curatorID
A unique identifier for the person that has curated the wine label description.

- Values: This element has no default values.

### figureNum
(figure number) Allows to number several figures for better identification.

- Values: This element has no default values.

### figurePosition
(figure position) The position of the figure on the label surface, in a grid of nine quadrants. The quadrants are numbered like on the number-pad of a phone, starting at the top left with 1 and ending at the bottom right with 9. Any quadrant that the figure covers to a significant extent is included in the position description. (The textual designators are still valid, but will be deprecated.)

- Values: upper-left, upper-right, upper-center, upper-across, center-left, center-right, center-center, center-across, lower-left, lower-right, lower-center, lower-across, left-across, center-across, right-across, full-size

### figureType
(figure type) Allows a simple classification of figures into common types.

- Values: symbolic, realistic, abstract, seal, coat-of-arms, symbolic

### fontColor
(no data)

- Values: This element has no default values.

### fontInitials
(no data)

- Values: This element has no default values.

### fontManner
(no data)

- Values: This element has no default values.

### fontSize
(no data)

- Values: This element has no default values.

### fontStyle
(no data)

- Values: This element has no default values.

### fontType
(no data)

- Values: This element has no default values.

### frameColor
(no data)

- Values: black, grey, gold, red, green

### frameStyle
(no data)

- Values: lines, floral, pattern, band, other

### frameType
(no data)

- Values: outer, inner, other

### itemData
(item data) This attribute provides a fixed vocabulary, in English (eng) and German (deu), and with a Wikidata identifier (wd), to name the figure item. No text content is allowed here.

- Values: coat-of-arms;deu=Wappen;Wikidata=Q14659, eng=grape;deu=Weintraube;Wikidata=Q10978, eng=sword;deu=Schwert;Wikidata=Q12791, eng=vineyard;deu=Weinberg;Wikidata=Q22715, eng=;deu=;Wikidata=

### labelID
A unique identifier for the label.

- Values: This element has no default values.

### labelType
This describes the label primarily with regard to its geographical scope.

- Values: Lageetikett, Gutsetikett, Ortsetikett, tbc, other

### licenceAbbr
(no data)

- Values: CC BY, public domain

### licenceScope
(no data)

- Values: all, markup, visual, metadata, textual

### locationNorm
(no data)

- Values: This element has no default values.

### locationRegNr
(no data)

- Values: This element has no default values.

### locationRole
(no data)

- Values: cultivation / Anbau, production / Weinbau, distribution / Vertrieb, cooperative / Kooperative, printer / Drucker, artist / Künstler/in, multiple / verschiedene, other / andere

### locationType
(no data)

- Values: country / Land, region / Gebiet, area / Bereich, locality / Ortsname, locality / Leitgemeinde, winery / Weingut, vineyard / historischer Lagenname, vineyard / Großlage, vineyard / Einzellage, other

### material
The material from which the label is made (in most cases, this is paper). 

- Values: paper, plastic, metal

### notAfter
(no data)

- Values: This element has no default values.

### notBefore
(no data)

- Values: This element has no default values.

### pageID
(no data)

- Values: This element has no default values.

### partNum
The number of the label, starting at 1.

- Values: This element has no default values.

### partType
The type of the label part, primarily defined by its supposed location on the bottle.

- Values: front, back, neck, wraparound, band

### printingTechnique
The technical printing process used for printing the visual and/or textual information onto the base material. 

- Values: lithograph, offset, moving-type, litho+type, mixed, other

### qualityAwardNorm
(no data)

- Values: Weinprämierung, Gütezeichen, other

### qualityGrapesNorm
(no data)

- Values: Kabinett, Spätlese, Auslese, Beerenauslese, Trockenbeerenauslese, Eiswein, other

### qualityLabelType
(no data)

- Values: vineyard, grapes, other

### qualityLevelNorm
(no data)

- Values: Tafelwein/Wein, Landwein, Qualitätswein, Prädikatswein, other

### qualityProductionNorm
(no data)

- Values: on-location, other

### ref
(reference) Contains authority file data, norm data, other stable and unique identifiers. Sources include: Wikidata, Register-Nummer der Weinlagen, Gemeinsame Normdaten-Datei.

- Values: RegNr:, Wikidata:, GND:, enwiki:, dewiki:, frwiki:

### scanID
(no data)

- Values: This element has no default values.

### shape
Information regarding the shape of the physical label.

- Values: square, circle, rectangle, oval, diamond, trapezoid, octogon, other

### sizeH
The height of the label measured in millimeters.

- Values: tbc

### sizeV
(no data)

- Values: tbc

### tasteGroupNorm
(no data)

- Values: This element has no default values.

### textPosition
(no data)

- Values: stand-alone, in-figure

### textType
(no data)

- Values: coat-text, motto, quotation, slogan, statement, copyright, vineyard (Lage), other

### uri
(uniform resource identifier) Für einen Link zu weiteren Informationen.

- Values: https://creativecommons.org/licenses/by/4.0/, https://github.com/dh-trier/wlv

### volumeNorm
(no data)

- Values: This element has no default values.

### wdw
(no data)

- Values: http://wdw.uni-trier.de/onlinewb/index.php3?ID

### wineAgingNorm
(no data)

- Values: barrique, other

### wineColorNorm
(no data)

- Values: red (Rotwein), white (Weisswein), rose (Rosé/Rotling), other

### wineGrapesNorm
(no data)

- Values: Riesling, Müller-Thurgau/Rivaner, Elbling, Spätburgunder, Grauburgunder, Chardonnay, Auxerrois, Weißburgunder, other

### wineMillesimeNorm
(no data)

- Values: This element has no default values.

### wineNameNorm
(no data)

- Values: This element has no default values.

### wineNameType
(no data)

- Values: country / Land, region / Gebiet, area / Bereich, locality / Ortsname, locality / Leitgemeinde, winery / Weingut, vineyard / historischer Lagenname, vineyard / Großlage, vineyard / Einzellage, variety / Rebsorte, other

### wineOtherType
(no data)

- Values: additives, usage, other

### year
(no data)

- Values: This element has no default values.
