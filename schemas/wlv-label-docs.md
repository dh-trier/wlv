# The Wine Label Vocabulary: Schema Documentation

This document documents all elements and attributes included in the Wine Label Vocabulary (WLV) in a human-readable form. This document has been generated automatically from the Relax NG schema.

For more information on the WLV, see https://github.com/dh-trier/wlv

## Contents

1. [Elements](#Elements)
2. [Attributes](#Attributes)

## Elements


### agent

(no data)

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): agentRole, ref, uri.

### alcohol

(no data)

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): alcoholNorm.

### background

Information about the background of the label. Needs to be filled in only if there is some special background, other than the blank paper, to the visual and/or textual information provided. 

- Contained by element(s): visual.
- Contains element(s): This element has no children.
- Has attribute(s): backgroundStyle.

### barrelNumber

(no data)

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): This element has no attributes.

### collection

The wine label collection the label belongs to.

- Contained by element(s): metadata.
- Contains element(s): This element has no children.
- Has attribute(s): collectionID.

### collectionContext

Any information that describes the individual label in the context of the collection, for example its location in the collection.

- Contained by element(s): metadata.
- Contains element(s): This element has no children.
- Has attribute(s): pageID, scanID.

### comments

(no data)

- Contained by element(s): metadata, label.
- Contains element(s): This element has no children.
- Has attribute(s): This element has no attributes.

### conservation

(no data)

- Contained by element(s): provenance.
- Contains element(s): This element has no children.
- Has attribute(s): conservationNorm.

### controlNumber

(no data)

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): ref, controlNumberType.

### curation

Information on the curation process of the wine label description.

- Contained by element(s): metadata.
- Contains element(s): This element has no children.
- Has attribute(s): curatorID, curationDate, curationUpdate.

### dating

(no data)

- Contained by element(s): provenance.
- Contains element(s): This element has no children.
- Has attribute(s): year, notBefore, notAfter, certainty.

### figure

(figure) Any visual, figurative element on the label. The label is classified as to its type and position using the attributes. It can be described in the element content using a simple list of terms mentioning each recognizable element of the figure. (In a future iteration of WLV, a controlled vocabulary of visual elements commonly found on wine labels will be made available for this purpose.)

- Contained by element(s): visual.
- Contains element(s): figureItem.
- Has attribute(s): figureNum, figureType, figurePosition.

### figureItem

(figure item) A visual element or depicted object that can be identified in the figure.

- Contained by element(s): figure.
- Contains element(s): This element has no children.
- Has attribute(s): itemData.

### frame

Information about the frame of the label.

- Contained by element(s): visual.
- Contains element(s): This element has no children.
- Has attribute(s): frameType, frameStyle, frameColor.

### label

The main container for information about the label. A label must have at least one part, but can have several parts.

- Contained by element(s): wlv.
- Contains element(s): comments, labelPart, provenance.
- Has attribute(s): labelType.

### labelNumber

(no data)

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): This element has no attributes.

### labelPart

(label part) Any physically separate part of the label / labeling.

- Contained by element(s): label.
- Contains element(s): physical, visual, textual.
- Has attribute(s): partNum, partType.

### licence

(no data)

- Contained by element(s): metadata.
- Contains element(s): This element has no children.
- Has attribute(s): uri, licenceAbbr, licenceScope.

### location

(no data)

- Contained by element(s): wineName.
- Contains element(s): This element has no children.
- Has attribute(s): locationType, locationRole, locationNorm, locationRegNr, figureNum, ref, uri.

### metadata

One of two mandatory top-level elements. Contains metadata related to the label description itself.

- Contained by element(s): wlv.
- Contains element(s): collection, curation, licence, collectionContext, comments.
- Has attribute(s): uri.

### otherText

(no data)

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): textType, textPosition, figureNum.

### physical

Information regarding the physical aspects of the label, in particular shape, size and material.

- Contained by element(s): labelPart.
- Contains element(s): This element has no children.
- Has attribute(s): shape, sizeH, sizeV, material, printingTechnique.

### provenance

(no data)

- Contained by element(s): label.
- Contains element(s): dating, source, scan, conservation.
- Has attribute(s): This element has no attributes.

### qualityAward

(no data)

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): ref, wdw, qualityAwardNorm.

### qualityGrapes

(no data)

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): ref, wdw, qualityGrapesNorm.

### qualityHistorical

(no data)

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): wdw, ref.

### qualityLabel

(no data)

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): ref, wdw, qualityLabelType.

### qualityLevel

(no data)

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): ref, wdw, qualityLevelNorm.

### qualityProduction

(no data)

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): ref, wdw, qualityProductionNorm.

### scan

(no data)

- Contained by element(s): provenance.
- Contains element(s): This element has no children.
- Has attribute(s): scanID.

### source

(no data)

- Contained by element(s): provenance.
- Contains element(s): This element has no children.
- Has attribute(s): year.

### textual

(no data)

- Contained by element(s): labelPart.
- Contains element(s): wineMillesime, wineName, wineGrapes, wineTaste, wineAging, wineOther, qualityGrapes, qualityLevel, qualityAward, qualityLabel, qualityProduction, qualityHistorical, agent, location, alcohol, volume, controlNumber, barrelNumber, labelNumber, otherText.
- Has attribute(s): This element has no attributes.

### visual

Any visual and non-textual or non-linguistic elements discernible on the label.

- Contained by element(s): labelPart.
- Contains element(s): frame, background, figure.
- Has attribute(s): This element has no attributes.

### volume

(no data)

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): volumeNorm.

### wineAging

(no data)

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): wineAgingNorm, ref, wdw.

### wineColor

(no data)

- Contained by element(s): (no data).
- Contains element(s): This element has no children.
- Has attribute(s): wineColorNorm, ref, wdw.

### wineGrapes

(no data)

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): wineGrapesNorm, ref, wdw.

### wineMillesime

The year that the wine was harvested in.

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): wineMillesimeNorm.

### wineName

The name of the wine. Typically printed in a somewhat larger font size than other information. For historical wine labels of the Mosel region, the wine name is typically composed of a location  (Ort, Gemeinde, Leitgemeinde) and the name or nickname of the specific vineyard belonging to that location. Note that the element 'wineName' has, as a consequence, an empty child element 'location' that can appear more than once and may hold information about the location and the vineyard separately. 

- Contained by element(s): textual.
- Contains element(s): location.
- Has attribute(s): wineNameType, wineNameNorm, ref, uri, wdw.

### wineOther

(no data)

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): wineOtherType, ref.

### wineTaste

(no data)

- Contained by element(s): textual.
- Contains element(s): This element has no children.
- Has attribute(s): ref, wdw.

### wlv

The root element in a label description using the Wine Label Vocabulary.

- Contained by element(s): This is the root element.
- Contains element(s): metadata, label.
- Has attribute(s): labelID.

## Attributes


### agentRole
(no data)

- Values: cultivation / Anbau, production / Weinbau, distribution / Vertrieb, cooperative / Kooperative, printer / Drucker, artist / Künstler/in, multiple / verschiedene, other / andere.

### alcoholNorm
(no data)

- Values: This element has no default values.

### backgroundStyle
(no data)

- Values: pattern, color, none.

### certainty
(no data)

- Values: source, evidence, estimate, low.

### collectionID
A unique identifier for the wine label collection.

- Values: This element has no default values.

### conservationNorm
(no data)

- Values: new, like new, very good, good, acceptable, damaged, incomplete.

### controlNumberType
(no data)

- Values: Amtliche Prüfnummer (Q480240), Losnummer, other.

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

- Values: upper-left, upper-right, upper-center, upper-across, center-left, center-right, center-center, center-across, lower-left, lower-right, lower-center, lower-across, left-across, center-across, right-across, full-size.

### figureType
(figure type) Allows a simple classification of figures into common types.

- Values: symbolic, realistic, abstract, seal, coat-of-arms, symbolic.

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

- Values: black, grey, gold, red, green.

### frameStyle
(no data)

- Values: lines, floral, pattern, band, other.

### frameType
(no data)

- Values: outer, inner, other.

### itemData
(item data) This attribute provides a fixed vocabulary, in German only, with a very broad category system (Artefakte, Fauna, Flora, Gebäude, Landschaft, Personen, Sonstiges) and a Wikidata identifier in brackets, to name the figure item. (No text content is allowed here. If there is text on a coat of arms or a banderole, it needs to be added under the heading 'textual'.)

- Values: Banderole (Artefakte;Q2689628), Brezel (Artefakte;Q160525), Boot (Artefakte;Q35872), Globus (Artefakte;Q133792), Gemälde (Artefakte;Q3305213), Fahrzeug (Artefakte;Q42889), Harfe (Artefakte;Q47369), Harpune (Artefakte;Q207574), Helm (Artefakte;Q910873), Hut (Artefakte;Q80151), Krone (Artefakte;Q170984), Krug (Artefakte;Q766983), Medaille (Artefakte;Q131647), Musikinstrument (Artefakte;Q), Pfeil (Artefakte;Q45922), Rad (Artefakte;Q446), Schiff (Artefakte;Q11446), Siegel (Artefakte;Q162919), Schild (Artefakte;Q131559), Schlüssel (Artefakte;Q132041), Schwert (Artefakte;Q12791), Stoff (Artefakte;Q5849500), Vase (Artefakte;Q191851), Wage (Artefakte;Q134566), Wappen (Artefakte;Q14659), Weinglas (Artefakte;Q1531435), Weinflasche (Artefakte;Q23490), Weinfass (Artefakte;Q10289), Adler (Fauna;Q2092297), Bär (Fauna;Q30090244), Feder (Fauna;Q81025), Flügel (Fauna;Q161358), Hund (Fauna;Q144), Katze (Fauna;Q146), Löwe (Fauna;Q140), Pferd (Fauna;Q726), Ochse (Fauna;Q473194), Reh/Hirsch (Fauna;Q29838690), Schaf (Fauna;Q7368), Spinne (Fauna;Q1357), Vogel (Fauna;Q5113), Baum (Flora;Q10884), Blume (Flora;Q886167), Blüte (Flora;Q506), Pflanze (Flora;Q756), Weintraube (Flora;Q10978), Weinblätter (Flora;Q33971), Weinstock (Flora;Q2135068), Burg (Bauwerke;Q23413), Brücke (Bauwerke;Q12280), Dock (Bauwerke;Q124282), Dorf (Bauwerke;Q532), Gebäude (Bauwerke;Q41176), Fenster (Bauwerke;Q35473), Interieur (Bauwerke;Q2998430), Keller (Bauwerke;Q43275450), Kirchengebäude (Bauwerke;Q16970), Mauer (Bauwerke;Q42948), Stadt (Bauwerke;Q532), Straße (Bauwerke;Q34442), Tor/Türe (Bauwerke;Q36794), Treppe (Bauwerke;Q12511), Turm (Bauwerke;Q12518), Zaun (Bauwerke;Q148571), Ufer (Landschaft;Q468756), Fluss (Landschaft;Q4022), Hügel (Landschaft;Q54050), Weinberg (Landschaft;Q22715), Mann (Personen;Q8441), Frau (Personen;Q467), Kind (Personen;Q7569), Mensch (Personen;Q5), Personengruppe (Personen;Q16334295), Ritter (Sonstiges;Q102083), Satyr (Sonstiges;Q163709), Engel (Sonstiges;Q235113), Drache (Sonstiges;Q7559), Stern (Sonstiges;Q523), Mond (Sonstiges;Q405), Sonne (Sonstiges;Q525).

### labelID
A unique identifier for the label.

- Values: This element has no default values.

### labelType
This describes the label primarily with regard to its geographical scope.

- Values: Lageetikett, Gutsetikett, Ortsetikett, tbc, other.

### licenceAbbr
(no data)

- Values: CC BY, public domain.

### licenceScope
(no data)

- Values: all, markup, visual, metadata, textual.

### locationNorm
(no data)

- Values: This element has no default values.

### locationRegNr
(no data)

- Values: This element has no default values.

### locationRole
(no data)

- Values: cultivation / Anbau, production / Weinbau, distribution / Vertrieb, cooperative / Kooperative, printer / Drucker, artist / Künstler/in, multiple / verschiedene, other / andere.

### locationType
(no data)

- Values: country / Land, region / Gebiet, area / Bereich, locality / Ortsname, locality / Leitgemeinde, winery / Weingut, vineyard / historischer Lagenname, vineyard / Großlage, vineyard / Einzellage, other.

### material
The material from which the label is made (in most cases, this is paper). 

- Values: paper, plastic, metal.

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

- Values: front, back, neck, wraparound, band.

### printingTechnique
The technical printing process used for printing the visual and/or textual information onto the base material. 

- Values: lithograph, offset, moving-type, litho+type, mixed, other.

### qualityAwardNorm
(no data)

- Values: Weinprämierung, Gütezeichen, other.

### qualityGrapesNorm
(no data)

- Values: Kabinett, Spätlese, Auslese, Beerenauslese, Trockenbeerenauslese, Eiswein, other.

### qualityLabelType
(no data)

- Values: vineyard, grapes, other.

### qualityLevelNorm
(no data)

- Values: Tafelwein/Wein, Landwein, Qualitätswein, Prädikatswein, other.

### qualityProductionNorm
(no data)

- Values: on-location, other.

### ref
(reference) Contains authority file data, norm data, other stable and unique identifiers. Sources include: Wikidata, Register-Nummer der Weinlagen, Gemeinsame Normdaten-Datei.

- Values: RegNr:, Wikidata:, GND:, enwiki:, dewiki:, frwiki:.

### scanID
(no data)

- Values: This element has no default values.

### shape
Information regarding the shape of the physical label.

- Values: square, circle, rectangle, oval, diamond, trapezoid, octogon, other.

### sizeH
The height of the label measured in millimeters.

- Values: tbc.

### sizeV
(no data)

- Values: tbc.

### tasteGroupNorm
(no data)

- Values: This element has no default values.

### textPosition
(no data)

- Values: stand-alone, in-figure.

### textType
(no data)

- Values: coat-text, motto, quotation, slogan, statement, copyright, vineyard (Lage), other.

### uri
(uniform resource identifier) Für einen Link zu weiteren Informationen.

- Values: https://creativecommons.org/licenses/by/4.0/, https://github.com/dh-trier/wlv.

### volumeNorm
(no data)

- Values: This element has no default values.

### wdw
(no data)

- Values: http://wdw.uni-trier.de/onlinewb/index.php3?ID.

### wineAgingNorm
(no data)

- Values: barrique, other.

### wineColorNorm
(no data)

- Values: red (Rotwein), white (Weisswein), rose (Rosé/Rotling), other.

### wineGrapesNorm
(no data)

- Values: Riesling, Müller-Thurgau/Rivaner, Elbling, Spätburgunder, Grauburgunder, Chardonnay, Auxerrois, Weißburgunder, other.

### wineMillesimeNorm
(no data)

- Values: This element has no default values.

### wineNameNorm
(no data)

- Values: This element has no default values.

### wineNameType
(no data)

- Values: country / Land, region / Gebiet, area / Bereich, locality / Ortsname, locality / Leitgemeinde, winery / Weingut, vineyard / historischer Lagenname, vineyard / Großlage, vineyard / Einzellage, variety / Rebsorte, other.

### wineOtherType
(no data)

- Values: additives, usage, other.

### year
(no data)

- Values: This element has no default values.
