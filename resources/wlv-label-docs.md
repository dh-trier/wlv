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

### The metadata

The metadata for a label names the collection the label belongs to, provides information about the curation of the label description, and indicates the licence of the label description. Accordingly, the [metadata](#metadata) element contains three mandatory elements: [collection](#collection), [curation](#curation) and [licence](#licence): (1) [collection](#collection) has a sole attribute [@collectionID](#collectionID) that indicates the identifier of the label's collection. The collection itself is described in a separate document. (2) The empty element [curation](#curation) is used to indicate when the label description was created and by whom, using [@curationDate](#curationData) and [@curator](#curator). Optionally, the date of an update to the description can be added as well. (3) The element [licence](#licence) serves to indicate the scope (e.g. label description or label itself) and the kind of the licence (e.g. Creative Commons Zero or Attribution) as well as a link to the licence, using the attributes [@licenceScope](#licenceScope), [@licenceAbbr](#licenceAbbr) and [@url](#url). Optionally, it is also possible to provide context using [collectionContexts](#collectionContexts) or to add further general information on the label or the curation as [comments](#comments).

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

**Elements**: [agent](#agent), [alcohol](#alcohol), [background](#background), [barrelNumber](#barrelNumber), [collection](#collection), [collectionContext](#collectionContext), [comments](#comments), [conservation](#conservation), [controlNumber](#controlNumber), [curation](#curation), [dating](#dating), [figure](#figure), [figureItem](#figureItem), [frame](#frame), [label](#label), [labelGroup](#labelGroup), [labelNumber](#labelNumber), [licence](#licence), [location](#location), [metadata](#metadata), [otherText](#otherText), [physical](#physical), [provenance](#provenance), [qualityAward](#qualityAward), [qualityGrapes](#qualityGrapes), [qualityHistorical](#qualityHistorical), [qualityLabel](#qualityLabel), [qualityLevel](#qualityLevel), [qualityProduction](#qualityProduction), [relation](#relation), [relations](#relations), [scan](#scan), [source](#source), [textual](#textual), [visual](#visual), [volume](#volume), [wineAging](#wineAging), [wineColor](#wineColor), [wineGrapes](#wineGrapes), [wineMillesime](#wineMillesime), [wineName](#wineName), [wineOther](#wineOther), [wineTaste](#wineTaste), [wlv](#wlv)

**Attributes**: [ID](#ID), [agentRole](#agentRole), [alcoholNorm](#alcoholNorm), [backgroundColor](#backgroundColor), [backgroundStyle](#backgroundStyle), [certainty](#certainty), [collectionID](#collectionID), [conservationNorm](#conservationNorm), [controlNumberType](#controlNumberType), [curationDate](#curationDate), [curationUpdate](#curationUpdate), [curatorID](#curatorID), [figureNum](#figureNum), [figurePosition](#figurePosition), [figureType](#figureType), [fontColor](#fontColor), [fontInitials](#fontInitials), [fontManner](#fontManner), [fontSize](#fontSize), [fontStyle](#fontStyle), [fontType](#fontType), [frameColor](#frameColor), [frameStyle](#frameStyle), [frameType](#frameType), [labelID](#labelID), [labelPosition](#labelPosition), [labelType](#labelType), [licenceAbbr](#licenceAbbr), [licenceScope](#licenceScope), [locationNorm](#locationNorm), [locationRegNr](#locationRegNr), [locationRole](#locationRole), [locationType](#locationType), [material](#material), [norm](#norm), [notAfter](#notAfter), [notBefore](#notBefore), [pageID](#pageID), [printingTechnique](#printingTechnique), [qualityAwardNorm](#qualityAwardNorm), [qualityLabelType](#qualityLabelType), [qualityProductionNorm](#qualityProductionNorm), [relItems](#relItems), [relType](#relType), [scanID](#scanID), [shape](#shape), [sizeH](#sizeH), [sizeV](#sizeV), [textPosition](#textPosition), [textType](#textType), [uri](#uri), [volumeNorm](#volumeNorm), [wdw](#wdw), [wineNameType](#wineNameType), [wineOtherType](#wineOtherType), [year](#year)

### Elements
#### agent

Any agent, whether a person (like a wine-maker or trader) or an organization (like a wine trading company or a printing enterprise), mentioned on the label.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [wineName](#wineName).
- Contains element(s): This element has no children.
- Has attribute(s): [agentRole](#agentRole), [norm](#norm), [uri](#uri), [ID](#ID).

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
- Has attribute(s): [backgroundStyle](#backgroundStyle), [backgroundColor](#backgroundColor).

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
- Has attribute(s): [norm](#norm), [controlNumberType](#controlNumberType).

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
- Has attribute(s): [figureNum](#figureNum), [figureType](#figureType), [figurePosition](#figurePosition), [ID](#ID).

#### figureItem

(figure item) A visual element or depicted object that can be identified in the figure.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [figure](#figure).
- Contains element(s): This element has no children.
- Has attribute(s): [norm](#norm), [ID](#ID).

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
- Contains element(s): [physical](#physical), [visual](#visual), [textual](#textual), [relations](#relations), [comments](#comments), [provenance](#provenance).
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
- Has attribute(s): [locationType](#locationType), [locationRole](#locationRole), [locationNorm](#locationNorm), [locationRegNr](#locationRegNr), [figureNum](#figureNum), [norm](#norm), [uri](#uri), [ID](#ID).

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

Indications referring to an award obtained by the wine.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [norm](#norm), [wdw](#wdw), [qualityAwardNorm](#qualityAwardNorm).

#### qualityGrapes

Indications referring to the quality of the grapes, like "Spätlese",  "Auslese" or "Trockenbeerenauslese".

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [wineName](#wineName).
- Contains element(s): This element has no children.
- Has attribute(s): [norm](#norm), [wdw](#wdw).

#### qualityHistorical

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [wdw](#wdw), [norm](#norm).

#### qualityLabel

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [wineName](#wineName).
- Contains element(s): This element has no children.
- Has attribute(s): [norm](#norm), [wdw](#wdw), [qualityLabelType](#qualityLabelType).

#### qualityLevel

Indications referring to the official quality level of the wine, like "Qualitätswein" or "Prädikatswein".

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [wineName](#wineName).
- Contains element(s): This element has no children.
- Has attribute(s): [norm](#norm), [wdw](#wdw).

#### qualityProduction

Any information describing specific steps in or aspects of the production of the wine that are meant to positively influence the quality of the resulting wine. An example is the mention of the fact that the wine has been bottled at the property. (For the quality specifically of the grapes, including the selection process of the grapes, use 'qualityGrapes' instead.)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [norm](#norm), [wdw](#wdw), [qualityProductionNorm](#qualityProductionNorm).

#### relation

(no data)

- Status: Mandatory.
- Frequency: Once or several times.
- Contained by element(s): [relations](#relations).
- Contains element(s): This element has no children.
- Has attribute(s): [relType](#relType), [relItems](#relItems), [ID](#ID).

#### relations

(no data)

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [label](#label).
- Contains element(s): [relation](#relation).
- Has attribute(s): This element has no attributes.

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
- Has attribute(s): [norm](#norm), [wdw](#wdw).

#### wineColor

The color of the name as mentioned on the label.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [(no data)](#(no data)).
- Contains element(s): This element has no children.
- Has attribute(s): [norm](#norm), [wdw](#wdw).

#### wineGrapes

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [wineName](#wineName).
- Contains element(s): This element has no children.
- Has attribute(s): [norm](#norm), [wdw](#wdw).

#### wineMillesime

The year that the wine was harvested in.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [norm](#norm), [ID](#ID).

#### wineName

The name of the wine. Typically printed in a somewhat larger font size than other information. For historical wine labels of the Mosel region, the wine name is typically composed of a location  (Ort, Gemeinde, Leitgemeinde) and the name or nickname of the specific vineyard belonging to that location. Note that the element 'wineName' has, as a consequence, an empty child element 'location' that can appear more than once and may hold information about the location and the vineyard separately.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): [agent](#agent), [location](#location), [qualityGrapes](#qualityGrapes), [qualityLabel](#qualityLabel), [qualityLevel](#qualityLevel), [wineGrapes](#wineGrapes).
- Has attribute(s): [wineNameType](#wineNameType), [norm](#norm), [uri](#uri), [wdw](#wdw), [ID](#ID).

#### wineOther

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [wineOtherType](#wineOtherType), [norm](#norm).

#### wineTaste

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [norm](#norm), [wdw](#wdw).

#### wlv

The root element in a label description using the Wine Label Vocabulary.

- Status: (no data).
- Frequency: (no data).
- Contained by element(s): This is the root element.
- Contains element(s): [metadata](#metadata), [labelGroup](#labelGroup), [label](#label).
- Has attribute(s): [labelID](#labelID), [labelType](#labelType).

### Attributes


#### ID
(no data)

- Status: Optional.
- Contained by element: 
    * [figure](#figure)
    * [figureItem](#figureItem)
    * [wineMillesime](#wineMillesime)
    * [wineName](#wineName)
    * [agent](#agent)
    * [location](#location)
    * [relation](#relation).
- Possible values: This element has no default values.

#### agentRole
The particular role of the agent, as far as it can be determined from the label itself or from contextual information. (TODO: authority data and definitions for these roles.)

- Status: Optional.
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

#### backgroundColor
The dominant color tone, whether it is strong or faint.

- Status: Optional.
- Contained by element: [background](#background).
- Possible values: 
    * red
    * blue
    * green
    * yellow
    * grey
    * white
    * black
    * gold.

#### backgroundStyle
The kind of background, whether a pattern, a flat color plane, or an absence of any pattern or color.

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
This describes the label primarily with regard to the agent issuing it and the geographical scope.

- Status: Optional.
- Contained by element: [wlv](#wlv).
- Possible values: 
    * Lageetikett
    * Gutsetikett
    * Ortsetikett
    * Weingutsetikett
    * Händleretikett
    * Musteretikett
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
The name of the location in a normalized form, with its type, and (if available) with authority data (Wikidata ID and/or Reg-Nr.).

- Status: Optional.
- Contained by element: [location](#location).
- Possible values: 
    * Bernkastel-Kues (Leitgemeinde;Q643228)
    * Brauneberg (Leitgemeinde;Q567156)
    * Wiltingen (Leitgemeinde;Q161930)
    * Winningen (Leitgemeinde;Q822358)
    * Zell (Leitgemeinde;Q187500)
    * Leitgemeinde: Zell (Q187500)
    * Filzen (Ort;Q47087896)
    * Freudenberg am Main (Ort;Q61827)
    * Graach (Ort;Q648808)
    * Ober-Ingelheim (Ort;Q2008825)
    * Trittenheim (Ort;Q662479)
    * Schwarze Katz (Großlage;Q2253665)
    * Großlage: Schwarze Katz (Q2253665)
    * Vollmühle (Parzelle)
    * other.

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

- Status: Optional.
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

#### norm
(normalized data) Contains authority file data and other stable and unique identifiers. Sources include: Wikidata, Register-Nummer der Weinlagen, Gemeinsame Normdaten-Datei, and others. Can relate to locations, agents, vineyards, items depicted in visual form, and other standardized vocabulary. 

- Status: Optional.
- Contained by element: 
    * [figureItem](#figureItem)
    * [wineMillesime](#wineMillesime)
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
    * Artefakt: Banderole (Q2689628)
    * Artefakt: Becher (Q81727)
    * Artefakt: Brezel (Q160525)
    * Artefakt: Boot (Q35872)
    * Artefakt: Globus (Q133792)
    * Artefakt: Gemälde (Q3305213)
    * Artefakt: Fahrzeug (Q42889)
    * Artefakt: Harfe (Q47369)
    * Artefakt: Harpune (Q207574)
    * Artefakt: Helm (Q910873)
    * Artefakt: Hut (Q80151)
    * Artefakt: Krone (Q170984)
    * Artefakt: Krug (Q766983)
    * Artefakt: Medaille (Q131647)
    * Artefakt: Musikinstrument (Q)
    * Artefakt: Ornament (Q335261)
    * Artefakt: Pfeil (Q45922)
    * Artefakt: Rad (Q446)
    * Artefakt: Säule (Q4817)
    * Artefakt: Schiff (Q11446)
    * Artefakt: Siegel (Q162919)
    * Artefakt: Schild (Q131559)
    * Artefakt: Schlüssel (Q132041)
    * Artefakt: Schwert (Q12791)
    * Artefakt: Sockel/Podest (Q12014132)
    * Artefakt: Stoff (Q5849500)
    * Artefakt: Vase (Q191851)
    * Artefakt: Wage (Q134566)
    * Artefakt: Wappen (Q14659)
    * Artefakt: Weinglas (Q1531435)
    * Artefakt: Weinflasche (Q23490)
    * Artefakt: Weinfass (Q10289)
    * Artefakt: Trichter ( Q29957)
    * Artefakt: Lampe, inkl. Laterne (Q1138737)
    * Artefakt: Stiefel (Q190868)
    * Artefakt: Siegel (Q162919)
    * Artefakt: Stempel (Q57305415)
    * Artefakt: Schnur (Q31029)
    * Artefakt: Etikett (Q722218)
    * Artefakt: Gitarre, inkl. Mandoline (Q6607)
    * Artefakt: Kostüm, inkl. Tracht (Q1410477)
    * Fauna: Hase (Q46076)
    * Fauna: Adler (Q2092297)
    * Fauna: Bär (Q30090244)
    * Fauna: Feder (Q81025)
    * Fauna: Flügel (Q161358)
    * Fauna: Hund (Q144)
    * Fauna: Katze (Q146)
    * Fauna: Katze (Q146)
    * Fauna: Löwe (Q140)
    * Fauna: Pferd (Q726)
    * Fauna: Ochse (Q473194)
    * Fauna: Reh/Hirsch (Q29838690)
    * Fauna: Schaf (Q7368)
    * Fauna: Spinne (Q1357)
    * Fauna: Vogel (Q5113)
    * Flora: Baum (Q10884)
    * Flora: Blume (Q886167)
    * Flora: Blüte (Q506)
    * Flora: Pflanze (Q756)
    * Flora: Weintraube (Q10978)
    * Flora: Weinblätter (Q33971)
    * Flora: Weinstock (Q2135068)
    * Flora: Wurzel (Q41500)
    * Bauwerk: Burg (Q23413)
    * Bauwerk: Brücke (Q12280)
    * Bauwerk: Dock (Q124282)
    * Bauwerk: Dorf (Q532)
    * Bauwerk: Gebäude (Q41176)
    * Bauwerk: Fenster (Q35473)
    * Bauwerk: Interieur (Q2998430)
    * Bauwerk: Keller (Q43275450)
    * Bauwerk: Kirchengebäude (Q16970)
    * Bauwerk: Mauer (Q42948)
    * Bauwerk: Stadt (Q532)
    * Bauwerk: Straße (Q34442)
    * Bauwerk: Tor/Türe (Q36794)
    * Bauwerk: Treppe (Q12511)
    * Bauwerk: Turm (Q12518)
    * Bauwerk: Zaun (Q148571)
    * Landschaft: Ufer (Q468756)
    * Landschaft: Fluss (Q4022)
    * Landschaft: Hügel (Q54050)
    * Landschaft: Weinberg (Q22715)
    * Person: Mann (Q8441)
    * Person: Frau (Q467)
    * Person: Kind (Q7569)
    * Person: Mensch (Q5)
    * Person: Minnesänger (Q841192)
    * Person: Personengruppe (Q16334295)
    * Sonstiges: Ritter (Q102083)
    * Sonstiges: Satyr (Q163709)
    * Sonstiges: Engel (Q235113)
    * Sonstiges: Drache (Q7559)
    * Sonstiges: Stern (Q523)
    * Sonstiges: Mond (Q405)
    * Sonstiges: Sonne (Q525)
    * Sonstiges: Schatten (Q160020)
    * QualityGrapes: Kabinett
    * QualityGrapes: Spätlese
    * QualityGrapes: Auslese
    * QualityGrapes: Beerenauslese
    * QualityGrapes: Trockenbeerenauslese (Q1639847)
    * QualityGrapes: Eiswein
    * QualityGrapes: other
    * Bereich: Mosel-Saar-Ruwer (Q672776)
    * Leitgemeinde: Bernkastel-Kues (Q643228)
    * Leitgemeinde: Brauneberg (Q567156)
    * Leitgemeinde: Wiltingen (Q161930)
    * Leitgemeinde: Winningen (Q822358)
    * Leitgemeinde: Zell (Q187500)
    * Ort: Filzen (Q47087896)
    * Ort: Freudenberg am Main (Q61827)
    * Ort: Graach (Q648808)
    * Ort: Ober-Ingelheim (Q2008825)
    * Ort: Trittenheim (Q662479)
    * Großlage: Schwarze Katz (Q2253665)
    * Parzelle: Vollmühle
    * Einzellage: Deutschherrenberg
    * Jahrgang: ####
    * Rebsorte (weiss): Riesling (Q456471)
    * Rebsorte (weiss): Müller-Thurgau / Rivaner (Q681670)
    * Rebsorte (weiss): Sauvignon Blanc
    * Rebsorte (weiss): Elbling
    * Rebsorte (weiss): Grauburgunder
    * Rebsorte (weiss): Chardonnay
    * Rebsorte (weiss): Auxerrois
    * Rebsorte (weiss): Weißburgunder
    * Rebsorte (weiss): other
    * Rebsorte (rot): Spätburgunder
    * Rebsorte (rot): other
    * Weinfarbe: Rotwein
    * Weinfarbe: Weisswein
    * Weinfarbe: Rosé/Rotling
    * Weinfarbe: other
    * Geschmack: dry (trocken)
    * Geschmack: semi-dry (halbtrocken / feinherb)
    * Geschmack: semi-sweet (lieblich)
    * Geschmack: sweet (süß)
    * Geschmack: other
    * WineAging: Barrique-Ausbau
    * WineAging: Flaschengärung
    * Weinqualität: Prädikatswein
    * Weinqualität: Tafelwein/Wein
    * Weinqualität: Landwein
    * Weinqualität: Qualitätswein
    * other
    * Traubenqualität: Kabinett
    * Traubenqualität: Spätlese
    * Traubenqualität: Auslese
    * Traubenqualität: Beerenauslese
    * Traubenqualität: Trockenbeerenauslese
    * Traubenqualität: Eiswein
    * Traubenqualität: other
    * Weingut: Weingut Maximin Grünhaus (Q2556072)
    * Weingut: #### (Q)
    * Vertrieb: Karl Ziegler.

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

#### qualityLabelType
(no data)

- Status: Optional.
- Contained by element: [qualityLabel](#qualityLabel).
- Possible values: vineyard, grapes, other.

#### qualityProductionNorm
(no data)

- Status: Optional.
- Contained by element: [qualityProduction](#qualityProduction).
- Possible values: on-location, other.

#### relItems
(no data)

- Status: Mandatory.
- Contained by element: [relation](#relation).
- Possible values: This element has no default values.

#### relType
(no data)

- Status: Mandatory.
- Contained by element: [relation](#relation).
- Possible values: equivalence, similarity, contrast, other.

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
    * polygon
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

#### wineNameType
(no data)

- Status: Optional.
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
    * composite
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
