# The Wine Label Vocabulary: Documentation

The following document has two parts: First, a prose description of collections and labels intended to provide an overview of the data model. Second, a documentation of all elements and labels generated from the schema file. 

The Wine Label Vocabulary (WLV) is formally defined in a Relax NG Schema, where all definitions of elements and attributes, with their rules of location and frequency of occurrence, their datatypes, their rules for acceptable values and similar information are documented.

Generally speaking, a collection of wine labels described using the WLV has two groups of files: One single file describing the collection of labels (see: element [collection](#collection), and a set of individual files each describing one label (see: element [label](#label) or a group of labels (see: element [labelGroup](#labelGroup).  


## Coding the collection file

The collection file describes the collection and lists its contents, i.e. label descriptions. The root element of an XML-WLV file for the collections is called [wlv](#wlv) (see also for wine-labels). For a collection, it contains two main sections: the metadata and the list of labels. The wlv element here has two attributes: the collectionID and an URL.

### The collection metadata

In the [metadata](#metadata), we want to give further information about the collection at hand. We collect the data about the collection title in the element [title](#title) (which itself is attributed with text). Another element forms the [editor](#editor) who is the person that created the file for the collection. Further elements are the owner, institution, address and a date. 

To specify the collection, one can also add an address and a date for where the collection comes from and when it was collected. It is also important to mark the license. Other elements are the [curator(s)](#curator) who are responsible for describing the collection as a file. Finally, the description element provides the possibility to add a textual description of the wine label collection.

### The list of labels

To the collection, we also want to add the labels that are included. Therefore, we add the [label](#label) element. If there is more than one physically distinct label belonging to the same labeling (say, a front label and a separate back label for the same wine), [labelGroup](#labelGroup) can be used: It can contain several `label` elements. A label should be attributed with its [labelID](#labelID) so that we can identify it.


## Coding the label descriptions

The labels are encoded separately from the collection metadata, and each label is encoded in a separate file. The root element of a XML-WLV file for labels is called [wlv](#wlv). Each WLV file contains the description of one wine label, with two main sections: the metadata and the label. The `wlv` element only has one attribute: [@labelID](#labelID).

### Metadata

The metadata for a label names the collection the label belongs to, provides information about the curation of the label description, and indicates the licence of the label description. Accordingly, the `metadata` element contains three mandatory elements: [collection](#collection), [curation](#curation) and [licence](#licence): (1) `collection` has a sole attribute `@collectionID` that indicates the identifier of the label's collection. (The collection itself is described in a separate document.) (2) The empty element [curation](#curation) has the attributes `@curationDate` (mandatory; year or date), `@curator` (mandatory; string) and `@curationUpdate` (optional; year or date). (3) The element [[licence]] has the attributes @licenceScope (mandatory, string), @licenceAbbr and @url (). Optionally, it is also possible to provide context using [[collectionContexts]] or add further information as [[comments]].

#### The labels

Each XML document includes only the information pertaining to the label (or label parts) pertaining to one wine. A collection typically contains more than one wine label. The labels (and their files) are hence always connected to their concerning collection (via the metadata).

#### The parts of a label

Any individual group of labels pertaining to one bottle can have more than one physically distinct label. In other words, all text-bearing objects found on a given bottle are considered to collectively make up the labeling of the bottle. Each of these text-bearing objects is considered to be a [label](#label) within a [labelGroup](#labelGroup). 

Typical examples are labeling that consists of a front and back label, or of a front label and a top banderole. Older labeling usually consisted of only one part. Label parts are numbered using the [partNumber](#partNumber) attribute and classified using the [partType](#partType) attribute. 

If only one label is present, the [labelGroup](#labelGroup) element is dropped. 

Each [label](#label) has three elements to describe it: [physical](#physical), [visual](#visual) and [textual](#textual). 

In addition, and optionally, each label or label group can have an optional description of its [provenance](#provenance). 

#### Physical aspects

The physical aspects of the label are encoded as part of the element [physical](#physical). They concern the [shape](#shape), size ([sizeV](#sizeV) and [sizeH](#sizeH)) and [material](#material) of the label as well as the [printingTechnique](#printingTechnique) used. 

#### Visual aspects

The visual aspects of the label concern any kind of visual representation, whether ornamental, symbolic or realistic. These visual elements are encoded in the element [visual](#visual) using the elements [frame](#frame), [background](#background) and [figure](#figure). 

#### Textual aspects

The textual aspects of the label concern any kind of written information that can be discerned, including text embedded within visual areas of the label. The top-level element for this domain is called [textual](#textual). (Note that the textual information present on the label is described, not the properties of the wine.)

A first main area of the textual domain are a set of elements pertaining to the factual description of the wine. This includes elements like [wineMillesime](#wineMillesime), [wineName](#wineName), often combined with [location](#location), [wineGrapes](#wineGrapes), [wineColor](#wineColor), [wineTaste](#wineTaste), [wineAging](#wineAging). 

A second major area concerns various indicators of the wine quality. This includes elements such as [qualityGrapes](#qualityGrapes), [qualityLevel](#qualityLevel), [qualityAward](#qualityAward), [qualityLabel](#qualityLabel), [qualityProduction](#qualityProduction) and [qualityHistorical](#qualityHistorical).  

A third major area of the textual domain pertains to the various kinds of agents and locations involved. This involves the [location](#location) and [agent](#agent) elements. Note that [location](#location) can be used as part of [wineName](#wineName) as well as separately. 

A fourth major area of the textual domain pertains to any numerical indications included on the label, such as the [alcohol](#alcohol) level the [volume](#volume) of the bottle, any official [controlNumber](#controlNumber) or [barrelNumber](#barrelNumber) as well as any [labelNumber](#labelNumber).  

Any other text found on a label can be encoded using the element [otherText](#otherText). In particular, any text discernible in the figures included on the label will be encoded here, with a reference back to the respective figure. 

In addition, there is a number of attributes that can be used on any of the elements in the textual domain, used to describe the script used for a given piece of information. This concerns aspects like [fontSize](#fontSize), [fontType](#fontType) and [fontStyle](#fontStyle) as well as [fontColor](#fontColor) and the treatment of [fontInitials](#fontInitials). 

#### Comments for a label

Any label can have a comment for notes, commentaries, annotations in prose. 

#### The provenance of a label

The provenance of a label describes several aspects concerning the history of the label as a collection item, using the [provenance](#provenance) element. This includes the estimated date of a label, when the indication of a [wineMillesime](#wineMillesime) is not present, using the [dating](#dating) element. 

Also, the collection, collector, wine maker or printer where the label was obtained can be noted using the [source](#source) element. The identifier of the scan that is the origin of the digital version of the label can also be included in the [scan](#scan) element. Finally, the state of conservation can be noted using the [conservation](#conservation) element. 

---


## WLV Schema Documentation

This document documents all elements and attributes included in the Wine Label Vocabulary (WLV) in a human-readable form. This document has been generated automatically from the Relax NG schema.

For more information on the WLV, see https://github.com/dh-trier/wlv

### Contents

1. [Quicklinks](#Quicklinks)
1. [Elements](#Elements)
2. [Attributes](#Attributes)

### Quicklinks

**Elements**: [agent](#agent), [alcohol](#alcohol), [background](#background), [barrelNumber](#barrelNumber), [collection](#collection), [collectionContext](#collectionContext), [comments](#comments), [conservation](#conservation), [controlNumber](#controlNumber), [curation](#curation), [dating](#dating), [figure](#figure), [figureItem](#figureItem), [frame](#frame), [label](#label), [labelGroup](#labelGroup), [labelNumber](#labelNumber), [licence](#licence), [location](#location), [metadata](#metadata), [otherText](#otherText), [physical](#physical), [provenance](#provenance), [qualityAward](#qualityAward), [qualityGrapes](#qualityGrapes), [qualityHistorical](#qualityHistorical), [qualityLabel](#qualityLabel), [qualityLevel](#qualityLevel), [qualityProduction](#qualityProduction), [scan](#scan), [source](#source), [textual](#textual), [visual](#visual), [volume](#volume), [wineAging](#wineAging), [wineColor](#wineColor), [wineGrapes](#wineGrapes), [wineMillesime](#wineMillesime), [wineName](#wineName), [wineOther](#wineOther), [wineTaste](#wineTaste), [wlv](#wlv)

**Attributes**: [agentRole](#agentRole), [alcoholNorm](#alcoholNorm), [backgroundStyle](#backgroundStyle), [certainty](#certainty), [collectionID](#collectionID), [conservationNorm](#conservationNorm), [controlNumberType](#controlNumberType), [curationDate](#curationDate), [curationUpdate](#curationUpdate), [curatorID](#curatorID), [figureNum](#figureNum), [figurePosition](#figurePosition), [figureType](#figureType), [fontColor](#fontColor), [fontInitials](#fontInitials), [fontManner](#fontManner), [fontSize](#fontSize), [fontStyle](#fontStyle), [fontType](#fontType), [frameColor](#frameColor), [frameStyle](#frameStyle), [frameType](#frameType), [itemData](#itemData), [labelID](#labelID), [labelPosition](#labelPosition), [labelType](#labelType), [licenceAbbr](#licenceAbbr), [licenceScope](#licenceScope), [locationNorm](#locationNorm), [locationRegNr](#locationRegNr), [locationRole](#locationRole), [locationType](#locationType), [material](#material), [notAfter](#notAfter), [notBefore](#notBefore), [pageID](#pageID), [printingTechnique](#printingTechnique), [qualityAwardNorm](#qualityAwardNorm), [qualityGrapesNorm](#qualityGrapesNorm), [qualityLabelType](#qualityLabelType), [qualityLevelNorm](#qualityLevelNorm), [qualityProductionNorm](#qualityProductionNorm), [ref](#ref), [scanID](#scanID), [shape](#shape), [sizeH](#sizeH), [sizeV](#sizeV), [tasteGroupNorm](#tasteGroupNorm), [textPosition](#textPosition), [textType](#textType), [uri](#uri), [volumeNorm](#volumeNorm), [wdw](#wdw), [wineAgingNorm](#wineAgingNorm), [wineColorNorm](#wineColorNorm), [wineGrapesNorm](#wineGrapesNorm), [wineMillesimeNorm](#wineMillesimeNorm), [wineNameNorm](#wineNameNorm), [wineNameType](#wineNameType), [wineOtherType](#wineOtherType), [year](#year)

### Elements
#### agent

Any agent, whether a person (like a wine-maker or trader) or an organization (like a wine trading company or a printing enterprise), mentioned on the label.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [agentRole](#agentRole), [ref](#ref), [uri](#uri).

#### alcohol

Information relevant to the alcohol content of the wine.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [alcoholNorm](#alcoholNorm).

#### background

Information about the background of the label. Needs to be filled in only if there is some special background, other than the blank paper, to the visual and/or textual information provided.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [visual](#visual).
- Contains element(s): This element has no children.
- Has attribute(s): [backgroundStyle](#backgroundStyle).

#### barrelNumber

The number of the barrel as mentioned on the label.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): This element has no attributes.

#### collection

The wine label collection the label belongs to.

- Status: Mandatory.
- Frequency: Exactly once.
- Contained by element(s): [metadata](#metadata).
- Contains element(s): This element has no children.
- Has attribute(s): [collectionID](#collectionID).

#### collectionContext

Any information that describes the individual label in the context of the collection, for example its location in the collection.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [metadata](#metadata).
- Contains element(s): This element has no children.
- Has attribute(s): [pageID](#pageID), [scanID](#scanID).

#### comments

Any comment on the label or the label description, written in prose by the curator(s).

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [metadata](#metadata), [labelGroup](#labelGroup), [label](#label).
- Contains element(s): This element has no children.
- Has attribute(s): This element has no attributes.

#### conservation

Information regarding the state of physical conservation of the label, in the form of a prose description.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [provenance](#provenance).
- Contains element(s): This element has no children.
- Has attribute(s): [conservationNorm](#conservationNorm).

#### controlNumber

The control number that is required for more recent labels.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ref](#ref), [controlNumberType](#controlNumberType).

#### curation

Information on the curation process of the wine label description.

- Status: Mandatory.
- Frequency: Exactly once.
- Contained by element(s): [metadata](#metadata).
- Contains element(s): This element has no children.
- Has attribute(s): [curatorID](#curatorID), [curationDate](#curationDate), [curationUpdate](#curationUpdate).

#### dating

Information regarding the supposed time of production of the label (especially relevant if no millesime is present.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [provenance](#provenance).
- Contains element(s): This element has no children.
- Has attribute(s): [year](#year), [notBefore](#notBefore), [notAfter](#notAfter), [certainty](#certainty).

#### figure

(figure) Any visual, figurative element on the label. The label is classified as to its type and position using the attributes. It can be described in the element content using a simple list of terms mentioning each recognizable element of the figure. (In a future iteration of WLV, a controlled vocabulary of visual elements commonly found on wine labels will be made available for this purpose.)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [visual](#visual).
- Contains element(s): [figureItem](#figureItem).
- Has attribute(s): [figureNum](#figureNum), [figureType](#figureType), [figurePosition](#figurePosition).

#### figureItem

(figure item) A visual element or depicted object that can be identified in the figure.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [figure](#figure).
- Contains element(s): This element has no children.
- Has attribute(s): [itemData](#itemData).

#### frame

Information about the frame of the label.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [visual](#visual).
- Contains element(s): This element has no children.
- Has attribute(s): [frameType](#frameType), [frameStyle](#frameStyle), [frameColor](#frameColor).

#### label

(label) Any single label or physically separate part of a label group.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [wlv](#wlv), [labelGroup](#labelGroup).
- Contains element(s): [physical](#physical), [visual](#visual), [textual](#textual), [comments](#comments), [provenance](#provenance).
- Has attribute(s): [labelPosition](#labelPosition).

#### labelGroup

A container element to group physically separate labels belonging to one bottle. A label group must have at least one label, but can contain several labels. (If only one label is present, it is recommended not to use labelGroup.)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [wlv](#wlv).
- Contains element(s): [comments](#comments), [label](#label), [provenance](#provenance).
- Has attribute(s): This element has no attributes.

#### labelNumber

The number or identifyer of the label usually assigned by the printer.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): This element has no attributes.

#### licence

The name of the licence used for the data.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [metadata](#metadata).
- Contains element(s): This element has no children.
- Has attribute(s): [uri](#uri), [licenceAbbr](#licenceAbbr), [licenceScope](#licenceScope).

#### location

Any location, such as the name of a region, city, village, or vineyard mentioned on the label.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [wineName](#wineName).
- Contains element(s): This element has no children.
- Has attribute(s): [locationType](#locationType), [locationRole](#locationRole), [locationNorm](#locationNorm), [locationRegNr](#locationRegNr), [figureNum](#figureNum), [ref](#ref), [uri](#uri).

#### metadata

One of two mandatory top-level elements. Contains metadata related to the label description itself.

- Status: Mandatory.
- Frequency: Exactly once.
- Contained by element(s): [wlv](#wlv).
- Contains element(s): [collection](#collection), [curation](#curation), [licence](#licence), [collectionContext](#collectionContext), [comments](#comments).
- Has attribute(s): [uri](#uri).

#### otherText

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [textType](#textType), [textPosition](#textPosition), [figureNum](#figureNum).

#### physical

Information regarding the physical aspects of the label, in particular shape, size and material.

- Status: Mandatory.
- Frequency: Exactly once.
- Contained by element(s): [label](#label).
- Contains element(s): This element has no children.
- Has attribute(s): [shape](#shape), [sizeH](#sizeH), [sizeV](#sizeV), [material](#material), [printingTechnique](#printingTechnique).

#### provenance

Information regarding the provenance of the label, in prose. This information can be derived either from the label itself, or from contextual or otherwise external information.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [labelGroup](#labelGroup), [label](#label).
- Contains element(s): [dating](#dating), [source](#source), [scan](#scan), [conservation](#conservation).
- Has attribute(s): This element has no attributes.

#### qualityAward

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ref](#ref), [wdw](#wdw), [qualityAwardNorm](#qualityAwardNorm).

#### qualityGrapes

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ref](#ref), [wdw](#wdw), [qualityGrapesNorm](#qualityGrapesNorm).

#### qualityHistorical

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [wdw](#wdw), [ref](#ref).

#### qualityLabel

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ref](#ref), [wdw](#wdw), [qualityLabelType](#qualityLabelType).

#### qualityLevel

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ref](#ref), [wdw](#wdw), [qualityLevelNorm](#qualityLevelNorm).

#### qualityProduction

Any information describing specific steps in or aspects of the production of the wine that are meant to positively influence the quality of the resulting wine. An example is the mention of the fact that the wine has been bottled at the property.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ref](#ref), [wdw](#wdw), [qualityProductionNorm](#qualityProductionNorm).

#### scan

(no data)

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [provenance](#provenance).
- Contains element(s): This element has no children.
- Has attribute(s): [scanID](#scanID).

#### source

(no data)

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [provenance](#provenance).
- Contains element(s): This element has no children.
- Has attribute(s): [year](#year).

#### textual

(no data)

- Status: Mandatory.
- Frequency: Exactly once.
- Contained by element(s): [label](#label).
- Contains element(s): [wineMillesime](#wineMillesime), [wineName](#wineName), [wineGrapes](#wineGrapes), [wineTaste](#wineTaste), [wineAging](#wineAging), [wineOther](#wineOther), [qualityGrapes](#qualityGrapes), [qualityLevel](#qualityLevel), [qualityAward](#qualityAward), [qualityLabel](#qualityLabel), [qualityProduction](#qualityProduction), [qualityHistorical](#qualityHistorical), [agent](#agent), [location](#location), [alcohol](#alcohol), [volume](#volume), [controlNumber](#controlNumber), [barrelNumber](#barrelNumber), [labelNumber](#labelNumber), [otherText](#otherText).
- Has attribute(s): This element has no attributes.

#### visual

Any visual and non-textual or non-linguistic elements discernible on the label.

- Status: Mandatory.
- Frequency: Exactly once.
- Contained by element(s): [label](#label).
- Contains element(s): [frame](#frame), [background](#background), [figure](#figure).
- Has attribute(s): This element has no attributes.

#### volume

Information regarding the volume of the wine.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [volumeNorm](#volumeNorm).

#### wineAging

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [wineAgingNorm](#wineAgingNorm), [ref](#ref), [wdw](#wdw).

#### wineColor

The color of the name as mentioned on the label.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [(no data)](#(no data)).
- Contains element(s): This element has no children.
- Has attribute(s): [wineColorNorm](#wineColorNorm), [ref](#ref), [wdw](#wdw).

#### wineGrapes

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [wineGrapesNorm](#wineGrapesNorm), [ref](#ref), [wdw](#wdw).

#### wineMillesime

The year that the wine was harvested in.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [wineMillesimeNorm](#wineMillesimeNorm).

#### wineName

The name of the wine. Typically printed in a somewhat larger font size than other information. For historical wine labels of the Mosel region, the wine name is typically composed of a location  (Ort, Gemeinde, Leitgemeinde) and the name or nickname of the specific vineyard belonging to that location. Note that the element 'wineName' has, as a consequence, an empty child element 'location' that can appear more than once and may hold information about the location and the vineyard separately.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): [location](#location).
- Has attribute(s): [wineNameType](#wineNameType), [wineNameNorm](#wineNameNorm), [ref](#ref), [uri](#uri), [wdw](#wdw).

#### wineOther

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [wineOtherType](#wineOtherType), [ref](#ref).

#### wineTaste

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ref](#ref), [wdw](#wdw).

#### wlv

The root element in a label description using the Wine Label Vocabulary.

- Status: (no data).
- Frequency: (no data).
- Contained by element(s): This is the root element.
- Contains element(s): [metadata](#metadata), [labelGroup](#labelGroup), [label](#label).
- Has attribute(s): [labelID](#labelID), [labelType](#labelType).

### Attributes


#### agentRole
The particular role of the agent, as far as it can be determined from the label itself or from contextual information. (TODO: authority data and definitions for these roles.)

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

#### alcoholNorm
The percentage of alcohol, expressed as number (float).

- Status: Mandatory.
- Contained by element: [alcohol](#alcohol).
- Possible values: This element has no default values.

#### backgroundStyle
(no data)

- Status: Mandatory.
- Contained by element: [background](#background).
- Possible values: pattern, color, none.

#### certainty
(no data)

- Status: Optional.
- Contained by element: [dating](#dating).
- Possible values: source, evidence, estimate, low.

#### collectionID
A unique identifier for the wine label collection.

- Status: Mandatory.
- Contained by element: [collection](#collection).
- Possible values: This element has no default values.

#### conservationNorm
Information regarding the state of physical conservation of the label, in short normed form.

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

#### controlNumberType
A legally-defined control number, for example the German "Amtliche Prüfnummer".

- Status: Optional.
- Contained by element: [controlNumber](#controlNumber).
- Possible values: Amtliche Prüfnummer (Q480240), Losnummer, other.

#### curationDate
The date (or year) when the wine label description was created.

- Status: Mandatory.
- Contained by element: [curation](#curation).
- Possible values: This element has no default values.

#### curationUpdate
The date (or year) when the wine label description was last updated.

- Status: Optional.
- Contained by element: [curation](#curation).
- Possible values: This element has no default values.

#### curatorID
A unique identifier for the person that has curated the wine label description.

- Status: Mandatory.
- Contained by element: [curation](#curation).
- Possible values: This element has no default values.

#### figureNum
(figure number) Allows to number several figures for better identification.

- Status: Mandatory.
- Contained by element: [figure](#figure).
- Possible values: This element has no default values.

#### figurePosition
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

#### figureType
(figure type) Allows a simple classification of figures into common types.

- Status: Mandatory.
- Contained by element: [figure](#figure).
- Possible values: 
    * symbolic
    * realistic
    * abstract
    * seal
    * coat-of-arms
    * other.

#### fontColor
(no data)

- Status: Optional.
- Contained by element: All elements contained by [textual](#textual).
- Possible values: This element has no default values.

#### fontInitials
(no data)

- Status: Optional.
- Contained by element: All elements contained by [textual](#textual).
- Possible values: This element has no default values.

#### fontManner
(no data)

- Status: Optional.
- Contained by element: All elements contained by [textual](#textual).
- Possible values: This element has no default values.

#### fontSize
(no data)

- Status: Optional.
- Contained by element: All elements contained by [textual](#textual).
- Possible values: This element has no default values.

#### fontStyle
(no data)

- Status: Optional.
- Contained by element: All elements contained by [textual](#textual).
- Possible values: This element has no default values.

#### fontType
(no data)

- Status: Optional.
- Contained by element: All elements contained by [textual](#textual).
- Possible values: This element has no default values.

#### frameColor
The color of the frame.

- Status: Mandatory.
- Contained by element: [frame](#frame).
- Possible values: 
    * black
    * grey
    * gold
    * red
    * green
    * blue
    * silver.

#### frameStyle
The visual style of the frame.

- Status: Mandatory.
- Contained by element: [frame](#frame).
- Possible values: 
    * lines
    * floral
    * pattern
    * band
    * other.

#### frameType
The type of frame, defined based on its position relative to other elements of the label. The value 'outer' means all other elements are within the frame. The value 'inner' means some of the other elements of the label are within, others are outside the frame.

- Status: Mandatory.
- Contained by element: [frame](#frame).
- Possible values: outer, inner, other.

#### itemData
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
    * Sonne (Sonstiges;Q525)
    * Trichter (Artefakte; Q29957)
    * Lampe, inkl. Laterne (Artefakte;Q1138737)
    * Stiefel (Artefakte;Q190868)
    * Siegel (Artefakte;Q162919)
    * Stempel (Artefakte;Q57305415)
    * Schnur (Artefakte;Q31029)
    * Hase (Fauna;Q46076)
    * Etikett (Artefakte;Q722218)
    * Minnesänger (Person;Q841192)
    * Gitarre, inkl. Mandoline (Artefakt;Q6607)
    * Kostüm, inkl. Tracht (Artefakte;Q1410477).

#### labelID
A unique identifier for the label.

- Status: Mandatory.
- Contained by element: [wlv](#wlv).
- Possible values: This element has no default values.

#### labelPosition
The position of the label on the bottle, used in particular as a way to disinguish the different labels in a label group.

- Status: Mandatory.
- Contained by element: [label](#label).
- Possible values: 
    * front
    * back
    * neck
    * wraparound
    * band.

#### labelType
This describes the label primarily with regard to its geographical scope.

- Status: Optional.
- Contained by element: [wlv](#wlv).
- Possible values: 
    * Lageetikett
    * Gutsetikett
    * Ortsetikett
    * tbc
    * other.

#### licenceAbbr
Abbreviation for the licence.

- Status: Optional.
- Contained by element: [licence](#licence).
- Possible values: CC BY, public domain.

#### licenceScope
The scope of the licence: The part or aspect of the label or label description to which the licence apply.

- Status: Mandatory.
- Contained by element: [licence](#licence).
- Possible values: 
    * all
    * markup
    * visual
    * metadata
    * textual.

#### locationNorm
The name of the location in a normalized form.

- Status: Optional.
- Contained by element: [location](#location).
- Possible values: This element has no default values.

#### locationRegNr
The numerical identifier of a vineyard contained in the official "Lagenliste".

- Status: Optional.
- Contained by element: [location](#location).
- Possible values: This element has no default values.

#### locationRole
The role of the location.

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

#### locationType
The type of the location, in particular with respect to the broader or narrower geographical scope. (Note that when this is part of the wine name, it is correlated, in German wine law, with quality levels.)

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

#### material
The material from which the label is made (in most cases, this is paper).

- Status: Mandatory.
- Contained by element: [physical](#physical).
- Possible values: paper, plastic, metal.

#### notAfter
(no data)

- Status: Optional.
- Contained by element: [dating](#dating).
- Possible values: This element has no default values.

#### notBefore
(no data)

- Status: Optional.
- Contained by element: [dating](#dating).
- Possible values: This element has no default values.

#### pageID
(no data)

- Status: Optional.
- Contained by element: [collectionContext](#collectionContext).
- Possible values: This element has no default values.

#### printingTechnique
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

#### qualityAwardNorm
(no data)

- Status: Optional.
- Contained by element: [qualityAward](#qualityAward).
- Possible values: Weinprämierung, Gütezeichen, other.

#### qualityGrapesNorm
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

#### qualityLabelType
(no data)

- Status: Optional.
- Contained by element: [qualityLabel](#qualityLabel).
- Possible values: vineyard, grapes, other.

#### qualityLevelNorm
(no data)

- Status: Optional.
- Contained by element: [qualityLevel](#qualityLevel).
- Possible values: 
    * Tafelwein/Wein
    * Landwein
    * Qualitätswein
    * Prädikatswein
    * other.

#### qualityProductionNorm
(no data)

- Status: Optional.
- Contained by element: [qualityProduction](#qualityProduction).
- Possible values: on-location, other.

#### ref
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

#### scanID
(no data)

- Status: Optional.
- Contained by element: [scan](#scan).
- Possible values: This element has no default values.

#### shape
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
    * circular
    * ellipsoid
    * other.

#### sizeH
The height of the label measured in millimeters. (This attribute is mandatory, but can also take the value "tbc" if the size data is not available.)

- Status: Mandatory.
- Contained by element: [physical](#physical).
- Possible values: tbc.

#### sizeV
The width of the label measured in millimeters. (This attribute is mandatory, but can also take the value "tbc" if the size data is not available.)

- Status: Mandatory.
- Contained by element: [physical](#physical).
- Possible values: tbc.

#### tasteGroupNorm
(no data)

- Status: Mandatory.
- Contained by element: .
- Possible values: This element has no default values.

#### textPosition
(no data)

- Status: Mandatory.
- Contained by element: [otherText](#otherText).
- Possible values: stand-alone, in-figure.

#### textType
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

#### uri
(uniform resource identifier) Für einen Link zu weiteren Informationen.

- Status: Optional.
- Contained by element: 
    * [metadata](#metadata)
    * [licence](#licence)
    * [wineName](#wineName)
    * [agent](#agent)
    * [location](#location).
- Possible values: https://creativecommons.org/licenses/by/4.0/, https://github.com/dh-trier/wlv.

#### volumeNorm
The indication of the volume of wine, expressed as a number (integer of milliliters).

- Status: Mandatory.
- Contained by element: [volume](#volume).
- Possible values: This element has no default values.

#### wdw
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

#### wineAgingNorm
(no data)

- Status: Mandatory.
- Contained by element: [wineAging](#wineAging).
- Possible values: barrique, other.

#### wineColorNorm
(no data)

- Status: Mandatory.
- Contained by element: [wineColor](#wineColor).
- Possible values: red (Rotwein), white (Weisswein), rose (Rosé/Rotling), other.

#### wineGrapesNorm
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

#### wineMillesimeNorm
(no data)

- Status: Mandatory.
- Contained by element: [wineMillesime](#wineMillesime).
- Possible values: This element has no default values.

#### wineNameNorm
The name of the wine in normalized form.

- Status: Optional.
- Contained by element: [wineName](#wineName).
- Possible values: This element has no default values.

#### wineNameType
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

#### wineOtherType
(no data)

- Status: Optional.
- Contained by element: [wineOther](#wineOther).
- Possible values: additives, usage, other.

#### year
(no data)

- Status: Optional.
- Contained by element: [dating](#dating), [source](#source).
- Possible values: This element has no default values.
