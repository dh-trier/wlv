# The Wine Label Vocabulary: Schema Documentation

This document documents all elements and attributes included in the Wine Label Vocabulary (WLV) in a human-readable form. This document has been generated automatically from the Relax NG schema.

For more information on the WLV, see https://github.com/dh-trier/wlv

## Contents

1. [Quicklinks](#Quicklinks)
1. [Elements](#Elements)
2. [Attributes](#Attributes)

## Quicklinks

**Elements**: [agent](#agent), [alcohol](#alcohol), [background](#background), [barrelNumber](#barrelNumber), [collection](#collection), [collectionContext](#collectionContext), [comments](#comments), [conservation](#conservation), [controlNumber](#controlNumber), [curation](#curation), [dating](#dating), [figure](#figure), [figureItem](#figureItem), [frame](#frame), [label](#label), [labelGroup](#labelGroup), [labelNumber](#labelNumber), [licence](#licence), [location](#location), [metadata](#metadata), [otherText](#otherText), [physical](#physical), [provenance](#provenance), [qualityAward](#qualityAward), [qualityGrapes](#qualityGrapes), [qualityHistorical](#qualityHistorical), [qualityLabel](#qualityLabel), [qualityLevel](#qualityLevel), [qualityProduction](#qualityProduction), [scan](#scan), [source](#source), [textual](#textual), [visual](#visual), [volume](#volume), [wineAging](#wineAging), [wineColor](#wineColor), [wineGrapes](#wineGrapes), [wineMillesime](#wineMillesime), [wineName](#wineName), [wineOther](#wineOther), [wineTaste](#wineTaste), [wlv](#wlv)

**Attributes**: [agentRole](#agentRole), [alcoholNorm](#alcoholNorm), [backgroundStyle](#backgroundStyle), [certainty](#certainty), [collectionID](#collectionID), [conservationNorm](#conservationNorm), [controlNumberType](#controlNumberType), [curationDate](#curationDate), [curationUpdate](#curationUpdate), [curatorID](#curatorID), [figureNum](#figureNum), [figurePosition](#figurePosition), [figureType](#figureType), [fontColor](#fontColor), [fontInitials](#fontInitials), [fontManner](#fontManner), [fontSize](#fontSize), [fontStyle](#fontStyle), [fontType](#fontType), [frameColor](#frameColor), [frameStyle](#frameStyle), [frameType](#frameType), [itemData](#itemData), [labelID](#labelID), [labelNum](#labelNum), [labelPosition](#labelPosition), [labelType](#labelType), [licenceAbbr](#licenceAbbr), [licenceScope](#licenceScope), [locationNorm](#locationNorm), [locationRegNr](#locationRegNr), [locationRole](#locationRole), [locationType](#locationType), [material](#material), [notAfter](#notAfter), [notBefore](#notBefore), [pageID](#pageID), [printingTechnique](#printingTechnique), [qualityAwardNorm](#qualityAwardNorm), [qualityGrapesNorm](#qualityGrapesNorm), [qualityLabelType](#qualityLabelType), [qualityLevelNorm](#qualityLevelNorm), [qualityProductionNorm](#qualityProductionNorm), [ref](#ref), [scanID](#scanID), [shape](#shape), [sizeH](#sizeH), [sizeV](#sizeV), [tasteGroupNorm](#tasteGroupNorm), [textPosition](#textPosition), [textType](#textType), [uri](#uri), [volumeNorm](#volumeNorm), [wdw](#wdw), [wineAgingNorm](#wineAgingNorm), [wineColorNorm](#wineColorNorm), [wineGrapesNorm](#wineGrapesNorm), [wineMillesimeNorm](#wineMillesimeNorm), [wineNameNorm](#wineNameNorm), [wineNameType](#wineNameType), [wineOtherType](#wineOtherType), [year](#year)

## Elements
### agent

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [agentRole](#agentRole), [ref](#ref), [uri](#uri).

### alcohol

(no data)

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [alcoholNorm](#alcoholNorm).

### background

Information about the background of the label. Needs to be filled in only if there is some special background, other than the blank paper, to the visual and/or textual information provided. 

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [visual](#visual).
- Contains element(s): This element has no children.
- Has attribute(s): [backgroundStyle](#backgroundStyle).

### barrelNumber

(no data)

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): This element has no attributes.

### collection

The wine label collection the label belongs to.

- Status: Mandatory.
- Frequency: Exactly once.
- Contained by element(s): [metadata](#metadata).
- Contains element(s): This element has no children.
- Has attribute(s): [collectionID](#collectionID).

### collectionContext

Any information that describes the individual label in the context of the collection, for example its location in the collection.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [metadata](#metadata).
- Contains element(s): This element has no children.
- Has attribute(s): [pageID](#pageID), [scanID](#scanID).

### comments

(no data)

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [metadata](#metadata), [labelGroup](#labelGroup), [label](#label).
- Contains element(s): This element has no children.
- Has attribute(s): This element has no attributes.

### conservation

(no data)

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [provenance](#provenance).
- Contains element(s): This element has no children.
- Has attribute(s): [conservationNorm](#conservationNorm).

### controlNumber

(no data)

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ref](#ref), [controlNumberType](#controlNumberType).

### curation

Information on the curation process of the wine label description.

- Status: Mandatory.
- Frequency: Exactly once.
- Contained by element(s): [metadata](#metadata).
- Contains element(s): This element has no children.
- Has attribute(s): [curatorID](#curatorID), [curationDate](#curationDate), [curationUpdate](#curationUpdate).

### dating

(no data)

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [provenance](#provenance).
- Contains element(s): This element has no children.
- Has attribute(s): [year](#year), [notBefore](#notBefore), [notAfter](#notAfter), [certainty](#certainty).

### figure

(figure) Any visual, figurative element on the label. The label is classified as to its type and position using the attributes. It can be described in the element content using a simple list of terms mentioning each recognizable element of the figure. (In a future iteration of WLV, a controlled vocabulary of visual elements commonly found on wine labels will be made available for this purpose.)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [visual](#visual).
- Contains element(s): [figureItem](#figureItem).
- Has attribute(s): [figureNum](#figureNum), [figureType](#figureType), [figurePosition](#figurePosition).

### figureItem

(figure item) A visual element or depicted object that can be identified in the figure.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [figure](#figure).
- Contains element(s): This element has no children.
- Has attribute(s): [itemData](#itemData).

### frame

Information about the frame of the label.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [visual](#visual).
- Contains element(s): This element has no children.
- Has attribute(s): [frameType](#frameType), [frameStyle](#frameStyle), [frameColor](#frameColor).

### label

(label) Any single label or physically separate part of the label group.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [wlv](#wlv), [labelGroup](#labelGroup).
- Contains element(s): [physical](#physical), [visual](#visual), [textual](#textual), [comments](#comments), [provenance](#provenance).
- Has attribute(s): [labelNum](#labelNum), [labelPosition](#labelPosition).

### labelGroup

The main container for information about the label. A label must have at least one part, but can have several parts.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [wlv](#wlv).
- Contains element(s): [comments](#comments), [label](#label), [provenance](#provenance).
- Has attribute(s): This element has no attributes.

### labelNumber

(no data)

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): This element has no attributes.

### licence

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [metadata](#metadata).
- Contains element(s): This element has no children.
- Has attribute(s): [uri](#uri), [licenceAbbr](#licenceAbbr), [licenceScope](#licenceScope).

### location

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [wineName](#wineName).
- Contains element(s): This element has no children.
- Has attribute(s): [locationType](#locationType), [locationRole](#locationRole), [locationNorm](#locationNorm), [locationRegNr](#locationRegNr), [figureNum](#figureNum), [ref](#ref), [uri](#uri).

### metadata

One of two mandatory top-level elements. Contains metadata related to the label description itself.

- Status: Mandatory.
- Frequency: Exactly once.
- Contained by element(s): [wlv](#wlv).
- Contains element(s): [collection](#collection), [curation](#curation), [licence](#licence), [collectionContext](#collectionContext), [comments](#comments).
- Has attribute(s): [uri](#uri).

### otherText

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [textType](#textType), [textPosition](#textPosition), [figureNum](#figureNum).

### physical

Information regarding the physical aspects of the label, in particular shape, size and material.

- Status: Mandatory.
- Frequency: Exactly once.
- Contained by element(s): [label](#label).
- Contains element(s): This element has no children.
- Has attribute(s): [shape](#shape), [sizeH](#sizeH), [sizeV](#sizeV), [material](#material), [printingTechnique](#printingTechnique).

### provenance

(no data)

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [labelGroup](#labelGroup), [label](#label).
- Contains element(s): [dating](#dating), [source](#source), [scan](#scan), [conservation](#conservation).
- Has attribute(s): This element has no attributes.

### qualityAward

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ref](#ref), [wdw](#wdw), [qualityAwardNorm](#qualityAwardNorm).

### qualityGrapes

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ref](#ref), [wdw](#wdw), [qualityGrapesNorm](#qualityGrapesNorm).

### qualityHistorical

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [wdw](#wdw), [ref](#ref).

### qualityLabel

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ref](#ref), [wdw](#wdw), [qualityLabelType](#qualityLabelType).

### qualityLevel

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ref](#ref), [wdw](#wdw), [qualityLevelNorm](#qualityLevelNorm).

### qualityProduction

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ref](#ref), [wdw](#wdw), [qualityProductionNorm](#qualityProductionNorm).

### scan

(no data)

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [provenance](#provenance).
- Contains element(s): This element has no children.
- Has attribute(s): [scanID](#scanID).

### source

(no data)

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [provenance](#provenance).
- Contains element(s): This element has no children.
- Has attribute(s): [year](#year).

### textual

(no data)

- Status: Mandatory.
- Frequency: Exactly once.
- Contained by element(s): [label](#label).
- Contains element(s): [wineMillesime](#wineMillesime), [wineName](#wineName), [wineGrapes](#wineGrapes), [wineTaste](#wineTaste), [wineAging](#wineAging), [wineOther](#wineOther), [qualityGrapes](#qualityGrapes), [qualityLevel](#qualityLevel), [qualityAward](#qualityAward), [qualityLabel](#qualityLabel), [qualityProduction](#qualityProduction), [qualityHistorical](#qualityHistorical), [agent](#agent), [location](#location), [alcohol](#alcohol), [volume](#volume), [controlNumber](#controlNumber), [barrelNumber](#barrelNumber), [labelNumber](#labelNumber), [otherText](#otherText).
- Has attribute(s): This element has no attributes.

### visual

Any visual and non-textual or non-linguistic elements discernible on the label.

- Status: Mandatory.
- Frequency: Exactly once.
- Contained by element(s): [label](#label).
- Contains element(s): [frame](#frame), [background](#background), [figure](#figure).
- Has attribute(s): This element has no attributes.

### volume

(no data)

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [volumeNorm](#volumeNorm).

### wineAging

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [wineAgingNorm](#wineAgingNorm), [ref](#ref), [wdw](#wdw).

### wineColor

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [(no data)](#(no data)).
- Contains element(s): This element has no children.
- Has attribute(s): [wineColorNorm](#wineColorNorm), [ref](#ref), [wdw](#wdw).

### wineGrapes

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [wineGrapesNorm](#wineGrapesNorm), [ref](#ref), [wdw](#wdw).

### wineMillesime

The year that the wine was harvested in.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [wineMillesimeNorm](#wineMillesimeNorm).

### wineName

The name of the wine. Typically printed in a somewhat larger font size than other information. For historical wine labels of the Mosel region, the wine name is typically composed of a location  (Ort, Gemeinde, Leitgemeinde) and the name or nickname of the specific vineyard belonging to that location. Note that the element 'wineName' has, as a consequence, an empty child element 'location' that can appear more than once and may hold information about the location and the vineyard separately. 

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): [location](#location).
- Has attribute(s): [wineNameType](#wineNameType), [wineNameNorm](#wineNameNorm), [ref](#ref), [uri](#uri), [wdw](#wdw).

### wineOther

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [wineOtherType](#wineOtherType), [ref](#ref).

### wineTaste

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ref](#ref), [wdw](#wdw).

### wlv

The root element in a label description using the Wine Label Vocabulary.

- Status: (no data).
- Frequency: (no data).
- Contained by element(s): This is the root element.
- Contains element(s): [metadata](#metadata), [labelGroup](#labelGroup), [label](#label).
- Has attribute(s): [labelID](#labelID), [labelType](#labelType).

## Attributes


### agentRole
(no data)

- Status: Mandatory.
- Contained by element: [agent](#agent).
- Possible values: 
    * cultivation / Anbau
    * production / Weinbau
    * distribution / Vertrieb
    * cooperative / Kooperative
    * printer / Drucker
    * artist / Künstler/in
    * multiple / verschiedene
    * other / andere.

### alcoholNorm
(no data)

- Status: Mandatory.
- Contained by element: [alcohol](#alcohol).
- Possible values: This element has no default values.

### backgroundStyle
(no data)

- Status: Mandatory.
- Contained by element: [background](#background).
- Possible values: pattern, color, none.

### certainty
(no data)

- Status: Optional.
- Contained by element: [dating](#dating).
- Possible values: source, evidence, estimate, low.

### collectionID
A unique identifier for the wine label collection.

- Status: Mandatory.
- Contained by element: [collection](#collection).
- Possible values: This element has no default values.

### conservationNorm
(no data)

- Status: Mandatory.
- Contained by element: [conservation](#conservation).
- Possible values: 
    * new
    * like new
    * very good
    * good
    * acceptable
    * damaged
    * incomplete.

### controlNumberType
(no data)

- Status: Optional.
- Contained by element: [controlNumber](#controlNumber).
- Possible values: Amtliche Prüfnummer (Q480240), Losnummer, other.

### curationDate
The date (or year) when the wine label description was created.

- Status: Mandatory.
- Contained by element: [curation](#curation).
- Possible values: This element has no default values.

### curationUpdate
The date (or year) when the wine label description was last updated.

- Status: Optional.
- Contained by element: [curation](#curation).
- Possible values: This element has no default values.

### curatorID
A unique identifier for the person that has curated the wine label description.

- Status: Mandatory.
- Contained by element: [curation](#curation).
- Possible values: This element has no default values.

### figureNum
(figure number) Allows to number several figures for better identification.

- Status: Mandatory.
- Contained by element: [figure](#figure).
- Possible values: This element has no default values.

### figurePosition
(figure position) The position of the figure on the label surface, in a grid of nine quadrants. The quadrants are numbered like on the number-pad of a phone, starting at the top left with 1 and ending at the bottom right with 9. Any quadrant that the figure covers to a significant extent is included in the position description. (The textual designators are still valid, but will be deprecated.)

- Status: Optional.
- Contained by element: [figure](#figure).
- Possible values: 
    * upper-left
    * upper-right
    * upper-center
    * upper-across
    * center-left
    * center-right
    * center-center
    * center-across
    * lower-left
    * lower-right
    * lower-center
    * lower-across
    * left-across
    * center-across
    * right-across
    * full-size.

### figureType
(figure type) Allows a simple classification of figures into common types.

- Status: Mandatory.
- Contained by element: [figure](#figure).
- Possible values: 
    * symbolic
    * realistic
    * abstract
    * seal
    * coat-of-arms
    * symbolic.

### fontColor
(no data)

- Status: Optional.
- Contained by element: All elements contained by [textual](#textual).
- Possible values: This element has no default values.

### fontInitials
(no data)

- Status: Optional.
- Contained by element: All elements contained by [textual](#textual).
- Possible values: This element has no default values.

### fontManner
(no data)

- Status: Optional.
- Contained by element: All elements contained by [textual](#textual).
- Possible values: This element has no default values.

### fontSize
(no data)

- Status: Optional.
- Contained by element: All elements contained by [textual](#textual).
- Possible values: This element has no default values.

### fontStyle
(no data)

- Status: Optional.
- Contained by element: All elements contained by [textual](#textual).
- Possible values: This element has no default values.

### fontType
(no data)

- Status: Optional.
- Contained by element: All elements contained by [textual](#textual).
- Possible values: This element has no default values.

### frameColor
(no data)

- Status: Mandatory.
- Contained by element: [frame](#frame).
- Possible values: 
    * black
    * grey
    * gold
    * red
    * green.

### frameStyle
(no data)

- Status: Mandatory.
- Contained by element: [frame](#frame).
- Possible values: 
    * lines
    * floral
    * pattern
    * band
    * other.

### frameType
(no data)

- Status: Mandatory.
- Contained by element: [frame](#frame).
- Possible values: outer, inner, other.

### itemData
(item data) This attribute provides a fixed vocabulary, in German only, with a very broad category system (Artefakte, Fauna, Flora, Gebäude, Landschaft, Personen, Sonstiges) and a Wikidata identifier in brackets, to name the figure item. (No text content is allowed here. If there is text on a coat of arms or a banderole, it needs to be added under the heading 'textual'.)

- Status: Mandatory.
- Contained by element: [figureItem](#figureItem).
- Possible values: 
    * Banderole (Artefakte;Q2689628)
    * Brezel (Artefakte;Q160525)
    * Boot (Artefakte;Q35872)
    * Globus (Artefakte;Q133792)
    * Gemälde (Artefakte;Q3305213)
    * Fahrzeug (Artefakte;Q42889)
    * Harfe (Artefakte;Q47369)
    * Harpune (Artefakte;Q207574)
    * Helm (Artefakte;Q910873)
    * Hut (Artefakte;Q80151)
    * Krone (Artefakte;Q170984)
    * Krug (Artefakte;Q766983)
    * Medaille (Artefakte;Q131647)
    * Musikinstrument (Artefakte;Q)
    * Pfeil (Artefakte;Q45922)
    * Rad (Artefakte;Q446)
    * Schiff (Artefakte;Q11446)
    * Siegel (Artefakte;Q162919)
    * Schild (Artefakte;Q131559)
    * Schlüssel (Artefakte;Q132041)
    * Schwert (Artefakte;Q12791)
    * Stoff (Artefakte;Q5849500)
    * Vase (Artefakte;Q191851)
    * Wage (Artefakte;Q134566)
    * Wappen (Artefakte;Q14659)
    * Weinglas (Artefakte;Q1531435)
    * Weinflasche (Artefakte;Q23490)
    * Weinfass (Artefakte;Q10289)
    * Adler (Fauna;Q2092297)
    * Bär (Fauna;Q30090244)
    * Feder (Fauna;Q81025)
    * Flügel (Fauna;Q161358)
    * Hund (Fauna;Q144)
    * Katze (Fauna;Q146)
    * Löwe (Fauna;Q140)
    * Pferd (Fauna;Q726)
    * Ochse (Fauna;Q473194)
    * Reh/Hirsch (Fauna;Q29838690)
    * Schaf (Fauna;Q7368)
    * Spinne (Fauna;Q1357)
    * Vogel (Fauna;Q5113)
    * Baum (Flora;Q10884)
    * Blume (Flora;Q886167)
    * Blüte (Flora;Q506)
    * Pflanze (Flora;Q756)
    * Weintraube (Flora;Q10978)
    * Weinblätter (Flora;Q33971)
    * Weinstock (Flora;Q2135068)
    * Burg (Bauwerke;Q23413)
    * Brücke (Bauwerke;Q12280)
    * Dock (Bauwerke;Q124282)
    * Dorf (Bauwerke;Q532)
    * Gebäude (Bauwerke;Q41176)
    * Fenster (Bauwerke;Q35473)
    * Interieur (Bauwerke;Q2998430)
    * Keller (Bauwerke;Q43275450)
    * Kirchengebäude (Bauwerke;Q16970)
    * Mauer (Bauwerke;Q42948)
    * Stadt (Bauwerke;Q532)
    * Straße (Bauwerke;Q34442)
    * Tor/Türe (Bauwerke;Q36794)
    * Treppe (Bauwerke;Q12511)
    * Turm (Bauwerke;Q12518)
    * Zaun (Bauwerke;Q148571)
    * Ufer (Landschaft;Q468756)
    * Fluss (Landschaft;Q4022)
    * Hügel (Landschaft;Q54050)
    * Weinberg (Landschaft;Q22715)
    * Mann (Personen;Q8441)
    * Frau (Personen;Q467)
    * Kind (Personen;Q7569)
    * Mensch (Personen;Q5)
    * Personengruppe (Personen;Q16334295)
    * Ritter (Sonstiges;Q102083)
    * Satyr (Sonstiges;Q163709)
    * Engel (Sonstiges;Q235113)
    * Drache (Sonstiges;Q7559)
    * Stern (Sonstiges;Q523)
    * Mond (Sonstiges;Q405)
    * Sonne (Sonstiges;Q525).

### labelID
A unique identifier for the label.

- Status: Mandatory.
- Contained by element: [wlv](#wlv).
- Possible values: This element has no default values.

### labelNum
The number of the label, starting at 1.

- Status: Optional.
- Contained by element: [label](#label).
- Possible values: This element has no default values.

### labelPosition
The type of the label part, primarily defined by its supposed location on the bottle.

- Status: Mandatory.
- Contained by element: [label](#label).
- Possible values: 
    * front
    * back
    * neck
    * wraparound
    * band.

### labelType
This describes the label primarily with regard to its geographical scope.

- Status: Optional.
- Contained by element: [wlv](#wlv).
- Possible values: 
    * Lageetikett
    * Gutsetikett
    * Ortsetikett
    * tbc
    * other.

### licenceAbbr
(no data)

- Status: Optional.
- Contained by element: [licence](#licence).
- Possible values: CC BY, public domain.

### licenceScope
(no data)

- Status: Mandatory.
- Contained by element: [licence](#licence).
- Possible values: 
    * all
    * markup
    * visual
    * metadata
    * textual.

### locationNorm
(no data)

- Status: Optional.
- Contained by element: [location](#location).
- Possible values: This element has no default values.

### locationRegNr
(no data)

- Status: Optional.
- Contained by element: [location](#location).
- Possible values: This element has no default values.

### locationRole
(no data)

- Status: Optional.
- Contained by element: [location](#location).
- Possible values: 
    * cultivation / Anbau
    * production / Weinbau
    * distribution / Vertrieb
    * cooperative / Kooperative
    * printer / Drucker
    * artist / Künstler/in
    * multiple / verschiedene
    * other / andere.

### locationType
(no data)

- Status: Mandatory.
- Contained by element: [location](#location).
- Possible values: 
    * country / Land
    * region / Gebiet
    * area / Bereich
    * locality / Ortsname
    * locality / Leitgemeinde
    * winery / Weingut
    * vineyard / historischer Lagenname
    * vineyard / Großlage
    * vineyard / Einzellage
    * other.

### material
The material from which the label is made (in most cases, this is paper). 

- Status: Mandatory.
- Contained by element: [physical](#physical).
- Possible values: paper, plastic, metal.

### notAfter
(no data)

- Status: Optional.
- Contained by element: [dating](#dating).
- Possible values: This element has no default values.

### notBefore
(no data)

- Status: Optional.
- Contained by element: [dating](#dating).
- Possible values: This element has no default values.

### pageID
(no data)

- Status: Optional.
- Contained by element: [collectionContext](#collectionContext).
- Possible values: This element has no default values.

### printingTechnique
The technical printing process used for printing the visual and/or textual information onto the base material. 

- Status: Optional.
- Contained by element: [physical](#physical).
- Possible values: 
    * lithograph
    * offset
    * moving-type
    * litho+type
    * mixed
    * other.

### qualityAwardNorm
(no data)

- Status: Optional.
- Contained by element: [qualityAward](#qualityAward).
- Possible values: Weinprämierung, Gütezeichen, other.

### qualityGrapesNorm
(no data)

- Status: Optional.
- Contained by element: [qualityGrapes](#qualityGrapes).
- Possible values: 
    * Kabinett
    * Spätlese
    * Auslese
    * Beerenauslese
    * Trockenbeerenauslese
    * Eiswein
    * other.

### qualityLabelType
(no data)

- Status: Optional.
- Contained by element: [qualityLabel](#qualityLabel).
- Possible values: vineyard, grapes, other.

### qualityLevelNorm
(no data)

- Status: Optional.
- Contained by element: [qualityLevel](#qualityLevel).
- Possible values: 
    * Tafelwein/Wein
    * Landwein
    * Qualitätswein
    * Prädikatswein
    * other.

### qualityProductionNorm
(no data)

- Status: Optional.
- Contained by element: [qualityProduction](#qualityProduction).
- Possible values: on-location, other.

### ref
(reference) Contains authority file data, norm data, other stable and unique identifiers. Sources include: Wikidata, Register-Nummer der Weinlagen, Gemeinsame Normdaten-Datei.

- Status: Optional.
- Contained by element: 
    * [wineName](#wineName)
    * [wineColor](#wineColor)
    * [wineGrapes](#wineGrapes)
    * [wineTaste](#wineTaste)
    * [wineAging](#wineAging)
    * [wineOther](#wineOther)
    * [qualityGrapes](#qualityGrapes)
    * [qualityLevel](#qualityLevel)
    * [qualityAward](#qualityAward)
    * [qualityLabel](#qualityLabel)
    * [qualityProduction](#qualityProduction)
    * [qualityHistorical](#qualityHistorical)
    * [agent](#agent)
    * [location](#location)
    * [controlNumber](#controlNumber).
- Possible values: 
    * RegNr:
    * Wikidata:
    * GND:
    * enwiki:
    * dewiki:
    * frwiki:.

### scanID
(no data)

- Status: Optional.
- Contained by element: [scan](#scan).
- Possible values: This element has no default values.

### shape
Information regarding the shape of the physical label.

- Status: Mandatory.
- Contained by element: [physical](#physical).
- Possible values: 
    * square
    * circle
    * rectangle
    * oval
    * diamond
    * trapezoid
    * octogon
    * other.

### sizeH
The height of the label measured in millimeters.

- Status: Mandatory.
- Contained by element: [physical](#physical).
- Possible values: tbc.

### sizeV
(no data)

- Status: Mandatory.
- Contained by element: [physical](#physical).
- Possible values: tbc.

### tasteGroupNorm
(no data)

- Status: Mandatory.
- Contained by element: .
- Possible values: This element has no default values.

### textPosition
(no data)

- Status: Mandatory.
- Contained by element: [otherText](#otherText).
- Possible values: stand-alone, in-figure.

### textType
(no data)

- Status: Mandatory.
- Contained by element: [otherText](#otherText).
- Possible values: 
    * coat-text
    * motto
    * quotation
    * slogan
    * statement
    * copyright
    * vineyard (Lage)
    * other.

### uri
(uniform resource identifier) Für einen Link zu weiteren Informationen.

- Status: Optional.
- Contained by element: 
    * [metadata](#metadata)
    * [licence](#licence)
    * [wineName](#wineName)
    * [agent](#agent)
    * [location](#location).
- Possible values: https://creativecommons.org/licenses/by/4.0/, https://github.com/dh-trier/wlv.

### volumeNorm
(no data)

- Status: Mandatory.
- Contained by element: [volume](#volume).
- Possible values: This element has no default values.

### wdw
(no data)

- Status: Optional.
- Contained by element: 
    * [wineName](#wineName)
    * [wineColor](#wineColor)
    * [wineGrapes](#wineGrapes)
    * [wineTaste](#wineTaste)
    * [wineAging](#wineAging)
    * [qualityGrapes](#qualityGrapes)
    * [qualityLevel](#qualityLevel)
    * [qualityAward](#qualityAward)
    * [qualityLabel](#qualityLabel)
    * [qualityProduction](#qualityProduction)
    * [qualityHistorical](#qualityHistorical).
- Possible values: http://wdw.uni-trier.de/onlinewb/index.php3?ID.

### wineAgingNorm
(no data)

- Status: Mandatory.
- Contained by element: [wineAging](#wineAging).
- Possible values: barrique, other.

### wineColorNorm
(no data)

- Status: Mandatory.
- Contained by element: [wineColor](#wineColor).
- Possible values: red (Rotwein), white (Weisswein), rose (Rosé/Rotling), other.

### wineGrapesNorm
(no data)

- Status: Mandatory.
- Contained by element: [wineGrapes](#wineGrapes).
- Possible values: 
    * Riesling
    * Müller-Thurgau/Rivaner
    * Elbling
    * Spätburgunder
    * Grauburgunder
    * Chardonnay
    * Auxerrois
    * Weißburgunder
    * other.

### wineMillesimeNorm
(no data)

- Status: Mandatory.
- Contained by element: [wineMillesime](#wineMillesime).
- Possible values: This element has no default values.

### wineNameNorm
(no data)

- Status: Optional.
- Contained by element: [wineName](#wineName).
- Possible values: This element has no default values.

### wineNameType
(no data)

- Status: Mandatory.
- Contained by element: [wineName](#wineName).
- Possible values: 
    * country / Land
    * region / Gebiet
    * area / Bereich
    * locality / Ortsname
    * locality / Leitgemeinde
    * winery / Weingut
    * vineyard / historischer Lagenname
    * vineyard / Großlage
    * vineyard / Einzellage
    * variety / Rebsorte
    * other.

### wineOtherType
(no data)

- Status: Optional.
- Contained by element: [wineOther](#wineOther).
- Possible values: additives, usage, other.

### year
(no data)

- Status: Optional.
- Contained by element: [dating](#dating), [source](#source).
- Possible values: This element has no default values.
