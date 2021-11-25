# The Wine Label Vocabulary: Schema Documentation

This document documents all elements and attributes included in the Wine Label Vocabulary (WLV) in a human-readable form. This document has been generated automatically from the Relax NG schema.

For more information on the WLV, see https://github.com/dh-trier/wlv

## 1. Elements included in the WLV


### agent

(no data)

- Child element(s): This element has no children.
- Attribute(s): agentRole, ref, url

### alcohol

(no data)

- Child element(s): This element has no children.
- Attribute(s): alcoholNorm

### background

(no data)

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

- Child element(s): This element has no children.
- Attribute(s): figureNum, figureType, figurePosition

### frame

(no data)

- Child element(s): This element has no children.
- Attribute(s): frameType, frameStyle, frameColor

### label

(no data)

- Child element(s): comments, labelPart, provenance
- Attribute(s): labelType

### labelNumber

(no data)

- Child element(s): This element has no children.
- Attribute(s): This element has no attributes.

### labelPart

(label part) Any physically separate part of the label.

- Child element(s): physical, visual, textual
- Attribute(s): partNum, partType

### licence

(no data)

- Child element(s): This element has no children.
- Attribute(s): url, licenceAbbr, licenceScope

### location

(no data)

- Child element(s): This element has no children.
- Attribute(s): locationRole, locationType, locationNorm, locationPosition, figureNum, ref

### metadata

One of two mandatory top-level elements. Contains metadata related to the label description itself.

- Child element(s): collection, curation, licence, collectionContext, comments
- Attribute(s): url

### otherText

(no data)

- Child element(s): This element has no children.
- Attribute(s): textType, textPosition, figureNum

### physical

(no data)

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

- Child element(s): wineMillesime, wineOrigin, wineGrapes, wineTaste, wineAging, wineOther, qualityGrapes, qualityLevel, qualityAward, qualityLabel, qualityProduction, qualityHistorical, agent, location, alcohol, volume, controlNumber, barrelNumber, labelNumber, otherText
- Attribute(s): This element has no attributes.

### visual

(no data)

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

(no data)

- Child element(s): This element has no children.
- Attribute(s): wineMillesimeNorm

### wineOrigin

(no data)

- Child element(s): This element has no children.
- Attribute(s): wineOriginType, wineOriginNorm, wineOriginLocality, ref, url, wdw

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

## 2. Attributes included in the WLV


### agentRole
(no data)

- Values: producer/bottler, distributor/importer/exporter, cooperative/association, printer, artist, other

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

### labelID
A unique identifier for the label.

- Values: This element has no default values.

### labelType
(no data)

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

### locationPosition
(no data)

- Values: standalone, in-figure

### locationRole
(no data)

- Values: producer/bottler, distributor/importer/exporter, cooperative/association, printer, artist, other

### locationType
(no data)

- Values: locality, region, country, other

### material
(no data)

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
(no data)

- Values: This element has no default values.

### partType
(no data)

- Values: front, back, neck, wraparound, band

### printingTechnique
(no data)

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
(no data)

- Values: wikidata:, gnd:, enwiki:, dewiki:, frwiki:

### scanID
(no data)

- Values: This element has no default values.

### shape
(no data)

- Values: square, circle, rectangle, oval, diamond, trapezoid, octogon, other

### sizeH
(no data)

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

### url
(no data)

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

- Values: Riesling, other

### wineMillesimeNorm
(no data)

- Values: This element has no default values.

### wineOriginLocality
(no data)

- Values: This element has no default values.

### wineOriginNorm
(no data)

- Values: This element has no default values.

### wineOriginType
(no data)

- Values: country (Land), region (Gebiet), area (Bereich), locality (Ort), winery (Weingut), vineyard (Lage), other

### wineOtherType
(no data)

- Values: additives, usage, other

### year
(no data)

- Values: This element has no default values.
