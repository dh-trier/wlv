# The Wine Label Vocabulary: Documentation

The following document has two parts: First, a prose description of collections and labels intended to provide an overview of the data model. Second, a documentation of all elements and labels generated from the schema file. 

The Wine Label Vocabulary (WLV) is formally defined in a Relax NG Schema, where all definitions of elements and attributes, with their rules of location and frequency of occurrence, their datatypes, their rules for acceptable values and similar information are documented. This document notably also includes a rather extensive list of names of relevant vineyards and localities with their authority data. 

Generally speaking, a collection of wine labels described using the WLV has two groups of files: One single file describing the collection of labels (see: element [collection](#collection)), and a set of individual files each describing one label (see: element [label](#label)) or a group of labels (see: element [labelGroup](#labelGroup)). 

## Coding the collection file

The collection file describes the collection and lists its contents, i.e. label descriptions. The root element of an XML-WLV file for the collections is called [wlv](#wlv) (see also for wine-labels). For a collection, it contains two main sections: the metadata and the list of labels. 

### The collection metadata

In the collection-level [metadata](#metadata), basic information is provided about the collection at hand. We collect the data about the collection title in the element [title](#title) (which itself is attributed with text). Another element forms the [editor](#editor) who is the person that created the file for the collection. Further elements include the [owner](#owner) and [institution](#institution). 

To specify the collection, one can also add an address and a date for where the collection comes from and when it was collected. It is also important to mark the [license](#licence). Other elements are the [curator(s)](#curator) who are responsible for describing the collection as a file. Finally, the description element provides the possibility to add a textual description of the wine label collection.

### The list of labels

The collection metadata also lists the labels that are included in the collection. Therefore, we add the [labels](#labels) element, with one [label](#label) entry per label containing the label's identifier: [labelID](#labelID). 


## Coding the label descriptions

The labels are encoded separately from the collection metadata, and each label is encoded in a separate file. The root element of a XML-WLV file for labels is again called [wlv](#wlv). Each WLV file contains the description of one wine label, with three main sections: the metadata, the label description, and information on provenance or other comments. The `wlv` element only has one attribute: [@labelID](#labelID).

### The metadata

The metadata for a label names the collection the label belongs to, provides information about the curation of the label description, and indicates the licence of the label description. Accordingly, the [metadata](#metadata) element contains three mandatory elements: [collection](#collection), [curation](#curation) and [licence](#licence): (1) [collection](#collection) has a sole attribute [@collectionID](#collectionID) that indicates the identifier of the label's collection. The collection itself is described in a separate document. (2) The empty element [curation](#curation) is used to indicate when the label description was created and by whom, using [@curationDate](#curationData) and [@curator](#curator). Optionally, the date of an update to the description can be added as well. (3) The element [licence](#licence) serves to indicate the scope (e.g. label description or label itself) and the kind of the licence (e.g. Creative Commons Zero or Attribution) as well as a link to the licence, using the attributes [@licenceScope](#licenceScope), [@licenceAbbr](#licenceAbbr) and [@url](#url). Optionally, it is also possible to provide context using [collectionContexts](#collectionContexts) or to add further general information on the label or the curation as [comments](#comments).

#### The labels

Each XML document includes only the information pertaining to the label (or label parts) pertaining to one wine. A collection typically contains more than one wine label. The labels (and their files) are hence always connected to their concerning collection (via the metadata). 

The data model for the wine labels follows a small number of general assumptions or principles. 

* First, the assumption that a label can be usefully described at three distinct levels, namely the physical, visual and textual properties. (In addition, relations between multiple elements at the same or at different levels can be described.) 
* Second, the idea to provide each piece of information with a standardized label and/or authority data to make it clearly identifiable and machine-readable. (This can either be a fix textual label with an identifier, or a standardized numerical indicator, depending on the element concerned.)
* Third, the principle that element content is only included when that (textual) content is visible on the label described. (All other information is recorded using attributes. This principle does not apply to the comments element.) 
* Fourth, the principle that only very few pieces of information are mandatory, but that a lot of details can optionally be recorded, if that is desired. (This also means simple descriptions can be expanded progressively.)
* Finally, the principle that although the WLV is currently used only for labels from the German Mosel wine region, the WLV should be sufficiently flexible and expressive enough to be easily used also for labels from other regions. (A limitation to this rule lies in the authority data, which is currently only provided for the Mosel region.)   

#### The parts of a label

Any individual group of labels pertaining to one bottle can have more than one physically distinct label. In other words, all text-bearing objects found on a given bottle are considered to collectively make up the labeling of the bottle. Each of these text-bearing objects is considered to be a [label](#label) within a [labelGroup](#labelGroup). If only one label is present, the [labelGroup](#labelGroup) element is dropped. 

Typical examples are labeling that consists of a front and back label, or of a front label and a top banderole. Older labeling usually consisted of only one label. Labels are described using the [labelPosition](#labelPosition) attribute. 

Each [label](#label) has four elements to describe it: [physical](#physical), [visual](#visual), [textual](#textual) and [relations](#relations). 

In addition, and optionally, each label or label group can have an optional description of its [provenance](#provenance) as well as optional [comments](#comments).  

#### Physical aspects

The physical aspects of the label are encoded as part of the element [physical](#physical). They concern the [shape](#shape), size ([sizeV](#sizeV) and [sizeH](#sizeH)) and [material](#material) of the label as well as the [printingTechnique](#printingTechnique) used. 

#### Visual aspects

The visual aspects of the label concern any kind of visual representation, whether ornamental, symbolic or realistic. These visual elements are encoded in the element [visual](#visual) using the elements [frame](#frame), [background](#background) and [figure](#figure). Notably, each figure contains one or several [figureItem](#figureItem)s for different, distinguishable visual elements or depicted objects in the figure. 

#### Textual aspects

The textual aspects of the label concern any kind of written information that can be discerned, including text embedded within visual areas of the label. The top-level element for this domain is called [textual](#textual). (Note that the textual information present on the label is described, not the properties of the wine.)

A first main area of the textual domain are a set of elements pertaining to the factual description of the wine. This includes elements like [wineMillesime](#wineMillesime), [wineName](#wineName), often consisting of one or several [location](#location) elements as well as, more rarely, information on the [wineGrapes](#wineGrapes), the [qualityGrapes](#qualityGrapes), the [wineColor](#wineColor), the [wineTaste](#wineTaste) or the [wineAging](#wineAging). 

A second major area concerns various indicators of the wine quality. This includes elements such as [qualityGrapes](#qualityGrapes), [qualityLevel](#qualityLevel), [qualityAward](#qualityAward), [qualityLabel](#qualityLabel), [qualityProduction](#qualityProduction) and [qualityHistorical](#qualityHistorical).  

A third major area of the textual domain pertains to the various kinds of agents and related locations involved. This involves the [location](#location) and [agent](#agent) elements. Note that [location](#location) can be used as part of [wineName](#wineName) as well as separately. 

A fourth major area of the textual domain pertains to any numerical indications included on the label, such as the [alcohol](#alcohol) level, the [volume](#volume) of the bottle, any official [controlNumber](#controlNumber) or [barrelNumber](#barrelNumber) as well as any [labelNumber](#labelNumber).  

Any other text found on a label can be encoded using the element [otherText](#otherText). In particular, any text discernible in the figures included on the label will be encoded here, with a reference back to the respective figure. 

In addition, there is a number of attributes that can be used on any of the elements in the textual domain, used to describe the script used for a given piece of information. This concerns aspects like [fontSize](#fontSize), [fontType](#fontType) and [fontStyle](#fontStyle) as well as [fontColor](#fontColor) and the treatment of [fontInitials](#fontInitials). 

#### Relations

The [relations](#relations) element is used to encode relations between elements of the label description, in particular relations between visual and textual elements. 

#### Comments for a label

Any label can have a [comments](#comments) section for notes, commentaries, annotations in free prose, using one [comment](#coment) per issue.  

#### The provenance of a label

The provenance of a label describes several aspects concerning the history of the label as a collection item, using the [provenance](#provenance) element. This includes the estimated date of a label, when the indication of a [wineMillesime](#wineMillesime) is not present, using the [dating](#dating) element. 

Also, the collection, collector, wine maker, printer, collector of other venue where the label was obtained can be noted using the [source](#source) element. Finally, the state of conservation can be noted using the [conservation](#conservation) element. 

---


## WLV Schema Documentation

This document documents all elements and attributes included in the Wine Label Vocabulary (WLV) in a human-readable form. This document has been generated automatically from the Relax NG schema.

For more information on the WLV, see https://github.com/dh-trier/wlv

### Contents

1. [Quicklinks](#Quicklinks)
1. [Elements](#Elements)
2. [Attributes](#Attributes)

### Quicklinks

**Elements**: [agent](#agent), [alcohol](#alcohol), [background](#background), [barrelNumber](#barrelNumber), [collection](#collection), [collectionContext](#collectionContext), [comment](#comment), [comments](#comments), [conservation](#conservation), [controlNumber](#controlNumber), [curation](#curation), [dating](#dating), [figure](#figure), [figureItem](#figureItem), [frame](#frame), [label](#label), [labelGroup](#labelGroup), [labelNumber](#labelNumber), [licence](#licence), [location](#location), [metadata](#metadata), [otherText](#otherText), [physical](#physical), [provenance](#provenance), [qualityAward](#qualityAward), [qualityGrapes](#qualityGrapes), [qualityHistorical](#qualityHistorical), [qualityLabel](#qualityLabel), [qualityLevel](#qualityLevel), [qualityProduction](#qualityProduction), [relation](#relation), [relations](#relations), [scan](#scan), [source](#source), [textual](#textual), [visual](#visual), [volume](#volume), [wineAging](#wineAging), [wineColor](#wineColor), [wineGrapes](#wineGrapes), [wineMillesime](#wineMillesime), [wineName](#wineName), [wineOther](#wineOther), [wineTaste](#wineTaste), [wlv](#wlv)

**Attributes**: [ID](#ID), [agentRole](#agentRole), [backgroundColor](#backgroundColor), [backgroundStyle](#backgroundStyle), [certainty](#certainty), [collectionID](#collectionID), [conservationNorm](#conservationNorm), [controlNumberType](#controlNumberType), [curationDate](#curationDate), [curationUpdate](#curationUpdate), [curatorID](#curatorID), [figureType](#figureType), [fontColor](#fontColor), [fontInitials](#fontInitials), [fontManner](#fontManner), [fontSize](#fontSize), [fontStyle](#fontStyle), [fontType](#fontType), [frameColor](#frameColor), [frameStyle](#frameStyle), [frameType](#frameType), [labelID](#labelID), [labelPosition](#labelPosition), [labelPosition](#labelPosition), [labelType](#labelType), [licenceAbbr](#licenceAbbr), [licenceScope](#licenceScope), [locationRole](#locationRole), [locationType](#locationType), [material](#material), [norm](#norm), [notAfter](#notAfter), [notBefore](#notBefore), [numNorm](#numNorm), [pageID](#pageID), [position](#position), [printingTechnique](#printingTechnique), [qualityAwardNorm](#qualityAwardNorm), [qualityLabelType](#qualityLabelType), [relItems](#relItems), [relType](#relType), [scanID](#scanID), [shape](#shape), [sizeH](#sizeH), [sizeV](#sizeV), [textPosition](#textPosition), [textType](#textType), [uri](#uri), [wdw](#wdw), [wineNameType](#wineNameType), [wineOtherType](#wineOtherType), [year](#year)

### Elements
#### agent

Any agent, whether a person (like a wine-maker or trader) or an organization (like a wine trading company or a printing enterprise), mentioned on the label.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual), [wineName](#wineName).
- Contains element(s): This element has no children.
- Has attribute(s): [agentRole](#agentRole), [position](#position), [norm](#norm), [uri](#uri), [ID](#ID).

#### alcohol

Information relevant to the alcohol content of the wine.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ID](#ID), [position](#position), [numNorm](#numNorm).

#### background

Information about the background of the label. Needs to be filled in only if there is some special background, other than the blank paper, to the visual and/or textual information provided.

- Status: Mandatory.
- Frequency: Once or several times.
- Contained by element(s): [visual](#visual).
- Contains element(s): This element has no children.
- Has attribute(s): [backgroundColor](#backgroundColor), [ID](#ID), [backgroundStyle](#backgroundStyle).

#### barrelNumber

The number of the barrel as mentioned on the label.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ID](#ID), [position](#position), [numNorm](#numNorm).

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

#### comment

Any comment on the label or the label description, written in prose by the curator(s).

- Status: Mandatory.
- Frequency: Once or several times.
- Contained by element(s): [comments](#comments).
- Contains element(s): This element has no children.
- Has attribute(s): [ID](#ID).

#### comments

Groups comment on the label or the label description, written in prose by the curator(s).

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [wlv](#wlv), [metadata](#metadata), [labelGroup](#labelGroup).
- Contains element(s): [comment](#comment).
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
- Has attribute(s): [ID](#ID), [position](#position), [numNorm](#numNorm), [controlNumberType](#controlNumberType).

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
- Has attribute(s): [figureType](#figureType), [position](#position), [ID](#ID).

#### figureItem

(figure item) A visual element or depicted object that can be identified in the figure.

- Status: Mandatory.
- Frequency: Once or several times.
- Contained by element(s): [figure](#figure).
- Contains element(s): This element has no children.
- Has attribute(s): [norm](#norm), [ID](#ID).

#### frame

Information about the frame of the label.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [visual](#visual).
- Contains element(s): This element has no children.
- Has attribute(s): [ID](#ID), [position](#position), [frameType](#frameType), [frameStyle](#frameStyle), [frameColor](#frameColor).

#### label

(label) Any single label or physically separate part of a label group.

- Status: Mandatory.
- Frequency: Once or several times.
- Contained by element(s): [wlv](#wlv), [labelGroup](#labelGroup).
- Contains element(s): [physical](#physical), [visual](#visual), [textual](#textual), [relations](#relations).
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
- Has attribute(s): [ID](#ID), [position](#position), [numNorm](#numNorm).

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
- Contained by element(s): [textual](#textual), [wineName](#wineName).
- Contains element(s): This element has no children.
- Has attribute(s): [locationType](#locationType), [locationRole](#locationRole), [norm](#norm), [uri](#uri), [ID](#ID), [position](#position).

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
- Has attribute(s): [ID](#ID), [textType](#textType), [position](#position), [textPosition](#textPosition).

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
- Contained by element(s): [wlv](#wlv), [labelGroup](#labelGroup).
- Contains element(s): [dating](#dating), [source](#source), [scan](#scan), [conservation](#conservation).
- Has attribute(s): This element has no attributes.

#### qualityAward

Indications referring to an award obtained by the wine.

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [position](#position), [norm](#norm), [wdw](#wdw), [qualityAwardNorm](#qualityAwardNorm).

#### qualityGrapes

Indications referring to the quality of the grapes, like "Spätlese",  "Auslese" or "Trockenbeerenauslese".

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual), [wineName](#wineName).
- Contains element(s): This element has no children.
- Has attribute(s): [position](#position), [norm](#norm), [wdw](#wdw).

#### qualityHistorical

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ID](#ID), [position](#position), [norm](#norm), [wdw](#wdw).

#### qualityLabel

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual), [wineName](#wineName).
- Contains element(s): This element has no children.
- Has attribute(s): [position](#position), [norm](#norm), [wdw](#wdw), [qualityLabelType](#qualityLabelType).

#### qualityLevel

Indications referring to the official quality level of the wine, like "Qualitätswein" or "Prädikatswein".

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual), [wineName](#wineName).
- Contains element(s): This element has no children.
- Has attribute(s): [position](#position), [norm](#norm), [wdw](#wdw).

#### qualityProduction

Any information describing specific steps in or aspects of the production of the wine that are meant to positively influence the quality of the resulting wine. An example is the mention of the fact that the wine has been bottled at the property. (For the quality specifically of the grapes, including the selection process of the grapes, use 'qualityGrapes' instead.)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [ID](#ID), [position](#position), [norm](#norm), [wdw](#wdw).

#### relation

Information regarding the type of relation between two or more elements of the label description, where these elements are specified using their identifiers.

- Status: Mandatory.
- Frequency: Once or several times.
- Contained by element(s): [relations](#relations).
- Contains element(s): This element has no children.
- Has attribute(s): [relType](#relType), [relItems](#relItems), [ID](#ID).

#### relations

Contains one or several statements regarding a relationship between elements of the label description.

- Status: Optional.
- Frequency: Once at most.
- Contained by element(s): [wlv](#wlv), [label](#label).
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
- Has attribute(s): [ID](#ID), [position](#position), [numNorm](#numNorm).

#### wineAging

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [norm](#norm), [position](#position), [wdw](#wdw).

#### wineColor

The color of the name as mentioned on the label.

- Status: Mandatory.
- Frequency: Exactly once.
- Contained by element(s): [(no data)](#(no data)).
- Contains element(s): This element has no children.
- Has attribute(s): [norm](#norm), [position](#position), [wdw](#wdw).

#### wineGrapes

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual), [wineName](#wineName).
- Contains element(s): This element has no children.
- Has attribute(s): [norm](#norm), [position](#position), [wdw](#wdw).

#### wineMillesime

The year that the wine was harvested in.

- Status: Mandatory.
- Frequency: Exactly once.
- Contained by element(s): [wineName](#wineName).
- Contains element(s): This element has no children.
- Has attribute(s): [numNorm](#numNorm), [ID](#ID), [position](#position).

#### wineName

The name of the wine. Typically printed in a somewhat larger font size than other information. For historical wine labels of the Mosel region, the wine name is typically composed of a location  (Ort, Gemeinde, Leitgemeinde) and the name or nickname of the specific vineyard belonging to that location. Note that the element 'wineName' has, as a consequence, an empty child element 'location' that can appear more than once and may hold information about the location and the vineyard separately.

- Status: Mandatory.
- Frequency: Exactly once.
- Contained by element(s): [(no data)](#(no data)).
- Contains element(s): [agent](#agent), [location](#location), [wineMillesime](#wineMillesime), [qualityGrapes](#qualityGrapes), [qualityLabel](#qualityLabel), [qualityLevel](#qualityLevel), [wineGrapes](#wineGrapes).
- Has attribute(s): [wineNameType](#wineNameType), [norm](#norm), [position](#position), [uri](#uri), [wdw](#wdw), [ID](#ID).

#### wineOther

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [wineOtherType](#wineOtherType), [norm](#norm), [position](#position).

#### wineTaste

(no data)

- Status: Optional.
- Frequency: Zero, once or several times.
- Contained by element(s): [textual](#textual).
- Contains element(s): This element has no children.
- Has attribute(s): [norm](#norm), [position](#position), [wdw](#wdw).

#### wlv

The root element in a label description using the Wine Label Vocabulary.

- Status: (no data).
- Frequency: (no data).
- Contained by element(s): This is the root element.
- Contains element(s): [metadata](#metadata), [labelGroup](#labelGroup), [label](#label), [comments](#comments), [provenance](#provenance), [relations](#relations).
- Has attribute(s): [labelID](#labelID), [labelType](#labelType).

### Attributes


#### ID
(no data)

- Status: Optional.
- Contained by element: 
    * [comment](#comment)
    * [frame](#frame)
    * [background](#background)
    * [figure](#figure)
    * [figureItem](#figureItem)
    * [wineMillesime](#wineMillesime)
    * [qualityProduction](#qualityProduction)
    * [qualityHistorical](#qualityHistorical)
    * [agent](#agent)
    * [location](#location)
    * [alcohol](#alcohol)
    * [volume](#volume)
    * [controlNumber](#controlNumber)
    * [barrelNumber](#barrelNumber)
    * [labelNumber](#labelNumber)
    * [otherText](#otherText)
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

#### backgroundColor
The dominant color tone, whether it is strong or faint.

- Status: Mandatory.
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

- Status: Optional.
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

#### figureType
(figure type) Allows a simple classification of figures into common types.

- Status: Optional.
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

- Status: Optional.
- Contained by element: [frame](#frame).
- Possible values: 
    * black
    * grey
    * gold
    * red
    * orange
    * green
    * blue
    * silver.

#### frameStyle
The visual style of the frame.

- Status: Optional.
- Contained by element: [frame](#frame).
- Possible values: 
    * line(s)
    * band(s)
    * floral
    * pattern
    * ornamental line(s)
    * ornamental band(s)
    * other.

#### frameType
The type of frame, defined based on its position relative to other elements of the label. The value 'outer' means all other elements are within the frame. The value 'inner' means some of the other elements of the label are within, others are outside the frame.

- Status: Optional.
- Contained by element: [frame](#frame).
- Possible values: outer, inner, other.

#### labelID
A unique identifier for the label.

- Status: Mandatory.
- Contained by element: [wlv](#wlv).
- Possible values: This element has no default values.

#### labelPosition
The position of the label on the bottle, used in particular as a way to disinguish the different labels in a label group.

- Status: Optional.
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
    * vineyard / Lage
    * vineyard / Parzelle
    * other.

#### material
The material from which the label is made (in most cases, this is paper).

- Status: Optional.
- Contained by element: [physical](#physical).
- Possible values: 
    * paper
    * plastic
    * metal
    * mixed
    * undetermined
    * other.

#### norm
(normalized data) Contains authority file data and other stable and unique identifiers. Sources include: Wikidata, Register-Nummer der Weinlagen, Gemeinsame Normdaten-Datei, and others. Can relate to locations, agents, vineyards, items depicted in visual form, and other standardized vocabulary. 

- Status: Mandatory.
- Contained by element: [figureItem](#figureItem).
- Possible values: 
    * Bild: Banderole [Artefakt] (Q2689628)
    * Bild: Becher [Artefakt] (Q81727)
    * Bild: Brezel [Artefakt] (Q160525)
    * Bild: Boot [Artefakt] (Q35872)
    * Bild: Globus [Artefakt] (Q133792)
    * Bild: Gemälde [Artefakt] (Q3305213)
    * Bild: Fahrzeug [Artefakt] (Q42889)
    * Bild: Harfe [Artefakt] (Q47369)
    * Bild: Harpune [Artefakt] (Q207574)
    * Bild: Helm [Artefakt] (Q910873)
    * Bild: Hut [Artefakt] (Q80151)
    * Bild: Krone [Artefakt] (Q170984)
    * Bild: Krug [Artefakt] (Q766983)
    * Bild: Medaille [Artefakt] (Q131647)
    * Bild: Musikinstrument [Artefakt] (Q)
    * Bild: Ornament [Artefakt] (Q335261)
    * Bild: Pfeil [Artefakt] (Q45922)
    * Bild: Rad [Artefakt] (Q446)
    * Bild: Säule [Artefakt] (Q4817)
    * Bild: Schiff [Artefakt] (Q11446)
    * Bild: Siegel [Artefakt] (Q162919)
    * Bild: Schild [Artefakt] (Q131559)
    * Bild: Schlüssel [Artefakt] (Q132041)
    * Bild: Schwert [Artefakt] (Q12791)
    * Bild: Sockel/Podest [Artefakt] (Q12014132)
    * Bild: Stoff [Artefakt] (Q5849500)
    * Bild: Vase [Artefakt] (Q191851)
    * Bild: Wage [Artefakt] (Q134566)
    * Bild: Wappen [Artefakt] (Q14659)
    * Bild: Weinglas [Artefakt] (Q1531435)
    * Bild: Weinflasche [Artefakt] (Q23490)
    * Bild: Weinfass [Artefakt] (Q10289)
    * Bild: Trichter [Artefakt] (Q29957)
    * Bild: Uhr [Artefakt] (Q376)
    * Bild: Lampe, inkl. Laterne [Artefakt] (Q1138737)
    * Bild: Stiefel [Artefakt] (Q190868)
    * Bild: Siegel [Artefakt] (Q162919)
    * Bild: Stempel [Artefakt] (Q57305415)
    * Bild: Schnur [Artefakt] (Q31029)
    * Bild: Etikett [Artefakt] (Q722218)
    * Bild: Gitarre, inkl. Mandoline [Artefakt] (Q6607)
    * Bild: Kostüm, inkl. Tracht [Artefakt] (Q1410477)
    * Bild: Hase [Fauna] (Q46076)
    * Bild: Adler [Fauna] (Q2092297)
    * Bild: Bär [Fauna] (Q30090244)
    * Bild: Feder [Fauna] (Q81025)
    * Bild: Flügel [Fauna] (Q161358)
    * Bild: Hund [Fauna] (Q144)
    * Bild: Katze [Fauna] (Q146)
    * Bild: Katze [Fauna] (Q146)
    * Bild: Löwe [Fauna] (Q140)
    * Bild: Pferd [Fauna] (Q726)
    * Bild: Ochse [Fauna] (Q473194)
    * Bild: Reh/Hirsch [Fauna] (Q29838690)
    * Bild: Schaf [Fauna] (Q7368)
    * Bild: Spinne [Fauna] (Q1357)
    * Bild: Vogel [Fauna] (Q5113)
    * Bild: Baum [Flora] (Q10884)
    * Bild: Blume [Flora] (Q886167)
    * Bild: Blüte [Flora] (Q506)
    * Bild: Pflanze [Flora] (Q756)
    * Bild: Weintraube [Flora] (Q10978)
    * Bild: Weinblätter [Flora] (Q33971)
    * Bild: Weinstock [Flora] (Q2135068)
    * Bild: Wurzel [Flora] (Q41500)
    * Bild: Burg [Bauwerk] (Q23413)
    * Bild: Brücke [Bauwerk] (Q12280)
    * Bild: Dock [Bauwerk] (Q124282)
    * Bild: Dorf [Bauwerk] (Q532)
    * Bild: Gebäude [Bauwerk] (Q41176)
    * Bild: Fenster [Bauwerk] (Q35473)
    * Bild: Interieur [Bauwerk] (Q2998430)
    * Bild: Keller [Bauwerk] (Q43275450)
    * Bild: Kirchengebäude [Bauwerk] (Q16970)
    * Bild: Mauer [Bauwerk] (Q42948)
    * Bild: Stadt [Bauwerk] (Q532)
    * Bild: Straße [Bauwerk] (Q34442)
    * Bild: Tor/Türe [Bauwerk] (Q36794)
    * Bild: Treppe [Bauwerk] (Q12511)
    * Bild: Turm [Bauwerk] (Q12518)
    * Bild: Zaun [Bauwerk] (Q148571)
    * Bild: Ufer [Landschaft] (Q468756)
    * Bild: Fluss [Landschaft] (Q4022)
    * Bild: Hügel [Landschaft] (Q54050)
    * Bild: Weinberg [Landschaft] (Q22715)
    * Bild: Mann [Person] (Q8441)
    * Bild: Frau [Person] (Q467)
    * Bild: Kind [Person] (Q7569)
    * Bild: Mensch [Person] (Q5)
    * Bild: Minnesänger [Person] (Q841192)
    * Bild: Personengruppe [Person] (Q16334295)
    * Bild: Ritter [Sonstiges] (Q102083)
    * Bild: Satyr [Sonstiges] (Q163709)
    * Bild: Engel [Sonstiges] (Q235113)
    * Bild: Drache [Sonstiges] (Q7559)
    * Bild: Stern [Sonstiges] (Q523)
    * Bild: Mond [Sonstiges] (Q405)
    * Bild: Sonne [Sonstiges] (Q525)
    * Bild: Schatten [Sonstiges] (Q160020)
    * Bild: Abstrakte Form [Sonstiges]
    * Bild: Barcode [Sonstiges] (Q856)
    * Bild: QR-Code [Sonstiges] (Q12203)
    * qualityGrapes: Kabinett
    * qualityGrapes: Spätlese
    * qualityGrapes: Auslese (Q426856)
    * qualityGrapes: Beerenauslese
    * qualityGrapes: Trockenbeerenauslese (Q1639847)
    * qualityGrapes: Eiswein
    * qualityGrapes: other
    * Land: Deutschland (Q183)
    * Bereich: Mosel-Saar-Ruwer (Q672776)
    * Ort: Alf (Q568556)
    * Ort: Alken (Q305288)
    * Ort: Andel (Q155622)
    * Ort: Ayl (Q186199)
    * Ort: Bausendorf (Q569296)
    * Ort: Beilstein (Q652238)
    * Ort: Bekond (Q569708)
    * Ort: Bernkastel (Q155622)
    * Ort: Biewer (Q245974)
    * Ort: Brauneberg (Q567156)
    * Ort: Bremm (Q113378)
    * Ort: Briedel (Q565192)
    * Ort: Briedern (Q1517)
    * Ort: Brodenbach (Q168070)
    * Ort: Bruttig-Fankel (Q574161)
    * Ort: Bruttig (Q574161)
    * Ort: Bullay (Q546257)
    * Ort: Burgen (Q679415)
    * Ort: Burg (Q658530)
    * Ort: Cochem (Q502749)
    * Ort: Cond (Q502749)
    * Ort: Detzem (Q553394)
    * Ort: Dhron (Q572352)
    * Ort: Dieblich (Q565313)
    * Ort: Dreis (Q563974)
    * Ort: Ediger (Q547805)
    * Ort: Eitelsbach (Q316811)
    * Ort: Ellenz-Polterdorf (Q566958)
    * Ort: Ellenz (Q566958)
    * Ort: Eller (Q547805)
    * Ort: Enkirch (Q553838)
    * Ort: Ensch (Q660477)
    * Ort: Erden (Q565749)
    * Ort: Ernst (Q567608)
    * Ort: Falkenstein (Q818576)
    * Ort: Fankel (Q574161)
    * Ort: Fellerich (Q1404048)
    * Ort: Fell (Q659890)
    * Ort: Filzen (Q47087896)
    * Ort: Gondorf (Q553347)
    * Ort: Graach (Q648808)
    * Ort: Güls (Q1777938)
    * Ort: Hatzenport (Q554243)
    * Ort: Helfant (Q636128)
    * Ort: Hupperath (Q565320)
    * Ort: Igel (Q543497)
    * Ort: Kaimt (Q187500)
    * Ort: Kanzem (Q569862)
    * Ort: Karden (Q656110)
    * Ort: Kasel (Q659935)
    * Ort: Kastel-Staadt (Q553490)
    * Ort: Kattenes (Q1736818)
    * Ort: Kenn (Q174435)
    * Ort: Kernscheid (Q650102)
    * Ort: Kesten (Q569300)
    * Ort: Kinheim (Q656236)
    * Ort: Klotten (Q269397)
    * Ort: Klüsserath (Q569589)
    * Ort: Kobern (Q553347)
    * Ort: Könen (Q1795916)
    * Ort: Konz (Q503185)
    * Ort: Kövenig (Q1796794)
    * Ort: Köwerich (Q657740)
    * Ort: Krettnach (Q503185)
    * Ort: Kreuzweiler (Q636128)
    * Ort: Kröv (Q553171)
    * Ort: Kues (Q155622)
    * Ort: Kürenz (Q883351)
    * Ort: Langsur (Q610893)
    * Ort: Lay (Q1328018)
    * Ort: Lehmen (Q567585)
    * Ort: Leiwen (Q681047)
    * Ort: Liersberg (Q20820333)
    * Ort: Lieser (Q646892)
    * Ort: Löf (Q553970)
    * Ort: Longuich (Q569606)
    * Ort: Lösnich (Q510820)
    * Ort: Maring-Noviand (Q566744)
    * Ort: Matthias (Q877660)
    * Ort: Maximin Grünhaus (Q659878)
    * Ort: Mehring (Q543574)
    * Ort: Merl (Q1921880)
    * Ort: Mertesdorf (Q659878)
    * Ort: Mesenich (Q610893)
    * Ort: Minheim (Q524796)
    * Ort: Monzel (Q648793)
    * Ort: Morscheid (Q656840)
    * Ort: Moselkern (Q651263)
    * Ort: Müden (Q680967)
    * Ort: Mühlheim (Q667192)
    * Ort: Neef (Q572494)
    * Ort: Nehren (Q572471)
    * Ort: Nennig (Q316804)
    * Ort: Neumagen (Q572352)
    * Ort: Niederemmel (Q375762)
    * Ort: Niederfell (Q553445)
    * Ort: Niederleuken (Q543639)
    * Ort: Niedermennig (Q503185)
    * Ort: Nittel (Q594609)
    * Ort: Oberbillig (Q636185)
    * Ort: Oberemmel (Q47037444)
    * Ort: Oberfell (Q647068)
    * Ort: Ockfen (Q643198)
    * Ort: Olewig (Q885323)
    * Ort: Osann (Q648793)
    * Ort: Palzem (Q636128)
    * Ort: Pellingen (Q655962)
    * Ort: Perl (Q662505)
    * Ort: Piesport (Q375762)
    * Ort: Pölich (Q553412)
    * Ort: Pommern (Q665867)
    * Ort: Pünderich (Q567287)
    * Ort: Rehlingen (Q594609)
    * Ort: Reil (Q656264)
    * Ort: Riol (Q553441)
    * Ort: Rivenich (Q552448)
    * Ort: Ruwer (Q316811)
    * Ort: Saarburg (Q543639)
    * Ort: Schleich (Q660583)
    * Ort: Schoden (Q646456)
    * Ort: Schweich (Q212570)
    * Ort: Sehl (Q502749)
    * Ort: Sehndorf (Q2266381)
    * Ort: Senheim (Q653097)
    * Ort: Serrig (Q656819)
    * Ort: Sommerau (Q631137)
    * Ort: Springiersbach (Q547805)
    * Ort: St. Aldegund (Q653902)
    * Ort: Starkenburg (Q682031)
    * Ort: Tarforst (Q328287)
    * Ort: Temmels (Q636175)
    * Ort: Thörnich (Q591473)
    * Ort: Traben (Q540919)
    * Ort: Trais (Q6566110)
    * Ort: Trarbach (Q540919)
    * Ort: Trier (Q3138)
    * Ort: Trittenheim (Q662479)
    * Ort: Ürzig (Q335018)
    * Ort: Valwig (Q656297)
    * Ort: Veldenz (Q569812)
    * Ort: Waldrach (Q569807)
    * Ort: Wasserliesch (Q553357)
    * Ort: Wawern (Q565310)
    * Ort: Wehlen (Q155622)
    * Ort: Wehr (Q636128)
    * Ort: Wellen (Q636208)
    * Ort: Wiltingen (Q161930)
    * Ort: Wincheringen (Q543611)
    * Ort: Winningen (Q822358)
    * Ort: Wintrich (Q373778)
    * Ort: Wittlich (Q559514)
    * Ort: Wolf (Q1563313)
    * Ort: Zell (Q187500)
    * Ort: Zeltingen (Q189241)
    * Ort: Bernkastel-Kues (Q643228)
    * Ort: Brauneberg (Q567156)
    * Ort: Wiltingen (Q161930)
    * Ort: Winningen (Q822358)
    * Ort: Zell (Q187500)
    * Ort: Trittenheim (Q662479)
    * Ort: Filzen (Q47087896)
    * Ort: Freudenberg am Main (Q61827)
    * Ort: Ober-Ingelheim (Q2008825)
    * Ort: Trittenheim (Q662479)
    * Ort: Pünderich (Q567287)
    * Lage: Abteiberg [Rosenhang] (6.3.3.073)
    * Lage: Abtei Kloster Stuben [Rosenhang] (6.3.3.059)
    * Lage: Abtei [Münzlay] (6.1.4.090)
    * Lage: Abtsberg [großlagenfrei] (6.4.1.009)
    * Lage: Abtsberg [Münzlay] (6.1.4.079)
    * Lage: Adler [Schwarze Katz] (6.3.4.097)
    * Lage: Agritiusberg [Scharzberg] (6.5.1.025)
    * Lage: Albachtaler [Gipfel] (6.2.1.015)
    * Lage: Altarberg [Goldbäumchen] (6.3.1.011)
    * Lage: Altärchen [Michelsberg] (6.1.3.072)
    * Lage: Alte Badstube am Doktorberg [Badstube] (6.1.1.006)
    * Lage: Altenberg [Gipfel] (6.2.1.018)
    * Lage: Altenberg [Römerlay] (6.1.10.189)
    * Lage: Altenberg [Scharzberg / Kanzem] (6.5.1.013)
    * Lage: Altenberg [Scharzberg / Krettnach] (6.5.1.021)
    * Lage: Altenberg [Scharzberg / Oberemmel] (6.5.1.026)
    * Lage: Amtgarten [Kurfürstenlay] (6.1.2.028)
    * Lage: Andreasberg [Römerlay] (6.1.10.190)
    * Lage: Annaberg [Propstberg] (6.1.6.104)
    * Lage: Antoniusberg [Scharzberg] (6.5.1.042)
    * Lage: Antoniusbrunnen [Scharzberg] (6.5.1.033)
    * Lage: Apotheke [Michelsberg] (6.1.3.073)
    * Lage: Arzlay [Rosenhang] (6.3.3.068)
    * Lage: Auf der Heide [Schwarzlay] (6.1.8.153)
    * Lage: Auf der Wiltinger Kupp [Scharzberg] (6.5.1.017)
    * Lage: Augenscheiner [Römerlay] (6.1.10.191)
    * Lage: Ausoniusstein [Weinhex] (6.3.5.124)
    * Lage: Badstube (Großlage) (6.1.1)
    * Lage: Batterieberg [Schwarzlay] (6.1.8.135)
    * Lage: Benediktinerberg [Römerlay] (6.1.10.192)
    * Lage: Bergschlößchen [Scharzberg] (6.5.1.034)
    * Lage: Bienengarten [Rosenhang] (6.3.3.076)
    * Lage: Bienengarten [Weinhex] (6.3.5.108)
    * Lage: Bienenlay [Grafschaft] (6.3.2.042)
    * Lage: Bischofsstuhl [Goldbäumchen] (6.3.1.003)
    * Lage: Bischofstein [Weinhex] (6.3.5.106)
    * Lage: Blattenberg [St. Michael] (6.1.7.114)
    * Lage: Bleidenberg [Weinhex] (6.3.5.103)
    * Lage: Blümchen [Gipfel] (6.2.1.005)
    * Lage: Bockstein [Scharzberg] (6.5.1.031)
    * Lage: Bottchen [Schwarzlay] (6.1.8.170)
    * Lage: Bratenhöfchen [Badstube] (6.1.1.001)
    * Lage: Brauneberg [Goldbäumchen] (6.3.1.014)
    * Lage: Brauneberg [Michelsberg] (6.1.3.068)
    * Lage: Brauneberg [St. Michael] (6.1.7.107)
    * Lage: Brauneberg [Weinhex] (6.3.5.133)
    * Lage: Braune Kupp [Scharzberg] (6.5.1.054)
    * Lage: Braunfels [Scharzberg] (6.5.1.055)
    * Lage: Brautrock [Grafschaft] (6.3.2.038)
    * Lage: Brückstück [Weinhex] (6.3.5.135)
    * Lage: Bruderberg [großlagenfrei] (6.4.1.010)
    * Lage: Brüderberg [Königsberg] (6.2.2.022)
    * Lage: Bruderschaft [St. Michael] (6.1.7.112)
    * Lage: Burgberg [Römerlay] (6.1.10.193)
    * Lage: Burgberg [Schwarzlay] (6.1.8.150)
    * Lage: Burgberg [Schwarzlay] (6.1.8.154)
    * Lage: Burgberg [Weinhex] (6.3.5.104)
    * Lage: Burg Bischofstein [Weinhex] (6.3.5.111)
    * Lage: Burg Coreidelsteiner [Goldbäumchen] (6.3.1.015)
    * Lage: Burggraf [Grafschaft] (6.3.2.028)
    * Lage: Burglay-Felsen [Schwarze Katz] (6.3.4.087)
    * Lage: Burglay [Michelsberg] (6.1.3.050)
    * Lage: Burglay [Nacktarsch] (6.1.5.092)
    * Lage: Burgmauer [Propstberg] (6.1.6.105)
    * Lage: Burg Warsberg [Gipfel] (6.2.1.019)
    * Lage: Busslay [Schwarzlay] (6.1.8.143)
    * Lage: Calmont [Grafschaft] (6.3.2.034)
    * Lage: Carlsberg [Kurfürstenlay] (6.1.2.036)
    * Lage: Carlsfelsen [Gipfel] (6.2.1.011)
    * Lage: Dechantsberg [Goldbäumchen] (6.3.1.023)
    * Lage: Deuslay [Rosenhang] (6.3.3.074)
    * Lage: Deutschherrenberg [Münzlay] (6.1.4.085)
    * Lage: Deutschherrenberg [Römerlay] (6.1.10.194)
    * Lage: Deutschherrenköpfchen [Römerlay] (6.1.10.195)
    * Lage: Doctor [Badstube] (6.1.1.002)
    * Lage: Domgarten [Weinhex] (6.3.5.136)
    * Lage: Domherrenberg [Goldbäumchen] (6.3.1.010)
    * Lage: Domherrenberg [Römerlay] (6.1.10.196)
    * Lage: Domherrenberg [Schwarze Katz] (6.3.4.088)
    * Lage: Domherr [Michelsberg] (6.1.3.061)
    * Lage: Dominikanerberg [großlagenfrei] (6.4.1.001)
    * Lage: Domprobst [Münzlay] (6.1.4.080)
    * Lage: Dullgärten [Königsberg] (6.2.2.021)
    * Lage: Edelberg [Schwarzlay] (6.1.8.136)
    * Lage: Ehrenberg [großlagenfrei] (6.4.1.015)
    * Lage: Elisenberg [Kurfürstenlay] (6.1.2.029)
    * Lage: Ellergrub [Schwarzlay] (6.1.8.137)
    * Lage: Elzhofberg [Grafschaft] (6.3.2.043)
    * Lage: Engelgrube [Michelsberg] (6.1.3.053)
    * Lage: Engelströpfchen [Grafschaft] (6.3.2.044)
    * Lage: Enggaß [St. Michael] (6.1.7.120)
    * Lage: Euchariusberg [Scharzberg] (6.5.1.018)
    * Lage: Euchariusberg [Scharzberg] (6.5.1.022)
    * Lage: Fächern [Weinhex] (6.3.5.130)
    * Lage: Fahrberg [Weinhex] (6.3.5.115)
    * Lage: Fahrberg [Weinhex] (6.3.5.116)
    * Lage: Falkenberg [Michelsberg] (6.1.3.062)
    * Lage: Falklay [Schwarzlay] (6.1.8.129)
    * Lage: Falklay [Vom heißen Stein] (6.1.9.185)
    * Lage: Felsenkopf [Michelsberg] (6.1.3.074)
    * Lage: Felsentreppchen [Schwarzlay] (6.1.8.171)
    * Lage: Felslay [großlagenfrei] (6.4.1.007)
    * Lage: Fels [Scharzberg] (6.5.1.015)
    * Lage: Fettgarten [Schwarze Katz] (6.3.4.098)
    * Lage: Feuerberg [Goldbäumchen] (6.3.1.012)
    * Lage: Feuerberg [Grafschaft] (6.3.2.045)
    * Lage: Frauenberg [Grafschaft] (6.3.2.037)
    * Lage: Fuchshöhle [Weinhex] (6.3.5.117)
    * Lage: Fuchs [Scharzberg] (6.5.1.036)
    * Lage: Funkenberg [Goldbäumchen] (6.3.1.019)
    * Lage: Fürsterlay [Schwarzlay] (6.1.8.151)
    * Lage: Gaispfad [Schwarzlay] (6.1.8.155)
    * Lage: Gäns [Weinhex] (6.3.5.118)
    * Lage: Gärtchen [Michelsberg] (6.1.3.063)
    * Lage: Geierslay [Kurfürstenlay] (6.1.2.044)
    * Lage: Geisberg [Michelsberg] (6.1.3.069)
    * Lage: Geisberg [Scharzberg] (6.5.1.032)
    * Lage: Geisberg [Schwarze Katz] (6.3.4.089)
    * Lage: Gipfel (unbenannte Einzellage) (6.2.1.003)
    * Lage: Gipfel (Großlage / Nittel) (6.2.1)
    * Lage: Goldbäumchen (Großlage) (6.3.1.001)
    * Lage: Goldberg [Goldbäumchen] (6.3.1.021)
    * Lage: Goldberg [Scharzberg] (6.5.1.050)
    * Lage: Goldblume [Weinhex] (6.3.5.128)
    * Lage: Goldgrübchen [Rosenhang] (6.3.3.075)
    * Lage: Goldgrube [Schwarzlay] (6.1.8.156)
    * Lage: Goldkupp [St. Michael] (6.1.7.115)
    * Lage: Goldlay [Vom heißen Stein] (6.1.9.181)
    * Lage: Goldlay [Vom heißen Stein] (6.1.9.186)
    * Lage: Goldlay [Weinhex] (6.3.5.131)
    * Lage: Goldschatz [Kurfürstenlay] (6.1.2.048)
    * Lage: Goldtröpfchen [Michelsberg] (6.1.3.064)
    * Lage: Goldwingert [Schwarzlay] (6.1.8.174)
    * Lage: Götterlay [Goldbäumchen] (6.3.1.002)
    * Lage: Gottesfuß [Scharzberg] (6.5.1.056)
    * Lage: Graben [Badstube] (6.1.1.003)
    * Lage: Graf Beyßel-Herrenberg [Grafschaft] (6.3.2.039)
    * Lage: Grafenberg [Michelsberg] (6.1.3.054)
    * Lage: Grafschafter Sonnenberg [Kurfürstenlay] (6.1.2.037)
    * Lage: Grafschaft (Großlage) (6.3.2.056)
    * Lage: Grafschaft (Großlage) (6.3.2)
    * Lage: Greth [Rosenhang] (6.3.3.080)
    * Lage: Großer Hengelberg [Michelsberg] (6.1.3.055)
    * Lage: Großer Herrgott [Kurfürstenlay] (6.1.2.040)
    * Lage: großlagenfrei (Großlage) (6.4.1.)
    * Lage: Günterslay [Michelsberg] (6.1.3.065)
    * Lage: Hahnenschrittchen [Schwarzlay] (6.1.8.130)
    * Lage: Hälle [Grafschaft] (6.3.2.030)
    * Lage: Hammerstein [Römerlay] (6.1.10.197)
    * Lage: Hamm [Weinhex] (6.3.5.122)
    * Lage: Hamm [Weinhex] (6.3.5.137)
    * Lage: Häs'chen [Michelsberg] (6.1.3.077)
    * Lage: Hasenberg [Schloß Bübingen] (6.6.1.525)
    * Lage: Hasenläufer [Kurfürstenlay] (6.1.2.017)
    * Lage: Heilgraben [Weinhex] (6.3.5.107)
    * Lage: Heiligenborn [Scharzberg] (6.5.1.043)
    * Lage: Held [Königsberg] (6.2.2.024)
    * Lage: Held [Propstberg] (6.1.6.099)
    * Lage: Held [St. Michael] (6.1.7.117)
    * Lage: Held [St. Michael] (6.1.7.125)
    * Lage: Helenenkloster [Kurfürstenlay] (6.1.2.030)
    * Lage: Herrenberger [Scharzberg] (6.5.1.051)
    * Lage: Herrenberg [Goldbäumchen] (6.3.1.004)
    * Lage: Herrenberg [Grafschaft] (6.3.2.029)
    * Lage: Herrenberg [großlagenfrei] (6.4.1.002)
    * Lage: Herrenberg [großlagenfrei] (6.4.1.011)
    * Lage: Herrenberg [Kurfürstenlay] (6.1.2.020)
    * Lage: Herrenberg [Nacktarsch] (6.1.5.093)
    * Lage: Herrenberg [Propstberg] (6.1.6.106)
    * Lage: Herrenberg [Römerlay] (6.1.10.198)
    * Lage: Herrenberg [Rosenhang] (6.3.3.083)
    * Lage: Herrenberg [Scharzberg] (6.5.1.001)
    * Lage: Herrenberg [Scharzberg] (6.5.1.004)
    * Lage: Herrenberg [Scharzberg] (6.5.1.023)
    * Lage: Herrenberg [Scharzberg] (6.5.1.040)
    * Lage: Herrenberg [Scharzberg] (6.5.1.044)
    * Lage: Herrenberg [Schwarzlay] (6.1.8.138)
    * Lage: Herrenberg [Schwarzlay] (6.1.8.144)
    * Lage: Herrgottsrock [Scharzberg] (6.5.1.064)
    * Lage: Herzchen [Vom heißen Stein] (6.1.9.176)
    * Lage: Herzlay [Schwarzlay] (6.1.8.128)
    * Lage: Himmelreich [Grafschaft] (6.3.2.053)
    * Lage: Himmelreich [Münzlay] (6.1.4.081)
    * Lage: Himmelreich [Münzlay] (6.1.4.086)
    * Lage: Hirschlay [Propstberg] (6.1.6.101)
    * Lage: Hirtengarten [Gipfel] (6.2.1.008)
    * Lage: Hitzlay [großlagenfrei] (6.4.1.003)
    * Lage: Hochlay [Goldbäumchen] (6.3.1.005)
    * Lage: Hofberger [Michelsberg] (6.1.3.056)
    * Lage: Hofberg [Scharzberg] (6.5.1.019)
    * Lage: Hölle [Scharzberg] (6.5.1.057)
    * Lage: Höll [Grafschaft] (6.3.2.046)
    * Lage: Honigberg [Kurfürstenlay] (6.1.2.024)
    * Lage: Hörecker [Scharzberg] (6.5.1.010)
    * Lage: Hubertusberg [Gipfel] (6.2.1.010)
    * Lage: Hubertusborn [Weinhex] (6.3.5.123)
    * Lage: Hubertuslay [Schwarzlay] (6.1.8.148)
    * Lage: Hühnerberg [Schwarzlay] (6.1.8.157)
    * Lage: Hunnenstein [Weinhex] (6.3.5.105)
    * Lage: Hütte [Scharzberg] (6.5.1.027)
    * Lage: Jesuitenberg [Scharzberg] (6.5.1.052)
    * Lage: Jesuitengarten [großlagenfrei] (6.4.1.016)
    * Lage: Jesuitenwingert [Römerlay] (6.1.10.199)
    * Lage: Johannisberg [Schwarzlay] (6.1.8.134)
    * Lage: Johannisbrünnchen [Kurfürstenlay] (6.1.2.008)
    * Lage: Josephshöfer [Münzlay] (6.1.4.082)
    * Lage: Juffer [Kurfürstenlay] (6.1.2.012)
    * Lage: Juffermauer [Goldbäumchen] (6.3.1.024)
    * Lage: Juffer Sonnenuhr [Kurfürstenlay] (6.1.2.013)
    * Lage: Kahllay [Weinhex] (6.3.5.132)
    * Lage: Kammer [Kurfürstenlay] (6.1.2.014)
    * Lage: Känigsberg [Schwarzlay] (6.1.8.159)
    * Lage: Kapellchen [Michelsberg] (6.1.3.051)
    * Lage: Kapellenberg [Gipfel] (6.2.1.002)
    * Lage: Kapellenberg [Gipfel] (6.2.1.013)
    * Lage: Kapellenberg [Grafschaft] (6.3.2.031)
    * Lage: Kapellenberg [Rosenhang] (6.3.3.060)
    * Lage: Kapellenberg [Rosenhang] (6.3.3.063)
    * Lage: Kapellenberg [Rosenhang] (6.3.3.081)
    * Lage: Kapplay [Grafschaft] (6.3.2.057)
    * Lage: Kardinalsberg [Kurfürstenlay] (6.1.2.009)
    * Lage: Karlsberg [Scharzberg] (6.5.1.028)
    * Lage: Karthäuserhofberg [großlagenfrei] (6.4.1.021)
    * Lage: Karthäuser Klosterberg [Scharzberg] (6.5.1.020)
    * Lage: Kätzchen [Kurfürstenlay] (6.1.2.032)
    * Lage: Katzenkopf [Grafschaft] (6.3.2.032)
    * Lage: Kehrberg [Weinhex] (6.3.5.119)
    * Lage: Kehrnagel [großlagenfrei] (6.4.1.004)
    * Lage: Kirchberg [Kurfürstenlay] (6.1.2.018)
    * Lage: Kirchberg [Kurfürstenlay] (6.1.2.038)
    * Lage: Kirchberg [Scharzberg] (6.5.1.016)
    * Lage: Kirchberg [Weinhex] (6.3.5.112)
    * Lage: Kirchlay [Goldbäumchen] (6.3.1.013)
    * Lage: Kirchlay [Kurfürstenlay] (6.1.2.033)
    * Lage: Kirchlay [Nacktarsch] (6.1.5.094)
    * Lage: Klosterberg [Kurfürstenlay] (6.1.2.025)
    * Lage: Klosterberg [Münzlay] (6.1.4.089)
    * Lage: Klosterberg [Scharzberg] (6.5.1.037)
    * Lage: Klosterberg [Scharzberg] (6.5.1.058)
    * Lage: Klosterberg [Schloß Bübingen] (6.6.1.522)
    * Lage: Klosterberg [Schwarze Katz] (6.3.4.099)
    * Lage: Klosterberg [Schwarzlay] (6.1.8.152)
    * Lage: Klosterberg [Schwarzlay] (6.1.8.158)
    * Lage: Klosterberg [St. Michael] (6.1.7.118)
    * Lage: Klosterberg [Weinhex] (6.3.5.125)
    * Lage: Klostergarten [Goldbäumchen] (6.3.1.006)
    * Lage: Klostergarten [Kurfürstenlay] (6.1.2.015)
    * Lage: Klostergarten [St. Michael] (6.1.7.126)
    * Lage: Klosterkammer [Grafschaft] (6.3.2.054)
    * Lage: Klosterweg [Schwarzlay] (6.1.8.147)
    * Lage: Königsberg (Großlage) (6.2.2.020)
    * Lage: Königsberg (Großlage) (6.2.2)
    * Lage: Königsberg [historische Lage / Detzem]
    * Lage: Königsfels [Weinhex] (6.3.5.109)
    * Lage: Königslay-Terrassen [Schwarze Katz] (6.3.4.100)
    * Lage: Kräuterhaus [Schwarzlay] (6.1.8.160)
    * Lage: Kreuzlay [Schwarze Katz] (6.3.4.090)
    * Lage: Kreuzwingert [Michelsberg] (6.1.3.076)
    * Lage: Kroneberg [Grafschaft] (6.3.2.040)
    * Lage: Krone [großlagenfrei] (6.4.1.017)
    * Lage: Kronenberg [Grafschaft] (6.3.2.033)
    * Lage: Kupp [Scharzberg] (6.5.1.002)
    * Lage: Kupp [Scharzberg] (6.5.1.038)
    * Lage: Kupp [Scharzberg] (6.5.1.045)
    * Lage: Kupp [Scharzberg] (6.5.1.059)
    * Lage: Kurfürstenhofberg [Römerlay] (6.1.10.200)
    * Lage: Kurfürstenlay (Großlage) (6.1.2.047)
    * Lage: Kurfürstenlay (Großlage) (6.1.2)
    * Lage: Kurfürst [Goldbäumchen] (6.3.1.026)
    * Lage: Lambertuslay [Kurfürstenlay] (6.1.2.049)
    * Lage: Laudamusberg [Michelsberg] (6.1.3.057)
    * Lage: Laurentiusberg [Grafschaft] (6.3.2.035)
    * Lage: Laurentiusberg [großlagenfrei] (6.4.1.018)
    * Lage: Laurentiusberg [Scharzberg] (6.5.1.065)
    * Lage: Laurentiuslay [St. Michael] (6.1.7.113)
    * Lage: Laurentiuslay [St. Michael] (6.1.7.127)
    * Lage: Lay [Badstube] (6.1.1.004)
    * Lage: Layenberg [Rosenhang] (6.3.3.064)
    * Lage: Lay [Gipfel] (6.2.1.012)
    * Lage: Lay [Rosenhang] (6.3.3.086)
    * Lage: Lay [Schwarzlay] (6.1.8.172)
    * Lage: Lay [Weinhex] (6.3.5.126)
    * Lage: Leiterchen [Gipfel] (6.2.1.006)
    * Lage: Leiterchen [Michelsberg] (6.1.3.075)
    * Lage: Letterlay [Nacktarsch] (6.1.5.095)
    * Lage: Mandelgraben [Kurfürstenlay] (6.1.2.016)
    * Lage: Marienberg [Schloß Bübingen] (6.2.1.164)
    * Lage: Marienberg [Weinhex] (6.3.5.110)
    * Lage: Marienburger [Schwarze Katz] (6.3.4.094)
    * Lage: Marienburg [Vom heißen Stein] (6.1.9.182)
    * Lage: Marienholz [Römerlay] (6.4.1.013)
    * Lage: Matheisbildchen [Badstube] (6.1.1.005)
    * Lage: Mäuerchen [großlagenfrei] (6.4.1.008)
    * Lage: Maximiner Burgberg [Propstberg] (6.1.6.098)
    * Lage: Maximiner [großlagenfrei] (6.4.1.014)
    * Lage: Maximiner Herrenberg [Propstberg] (6.1.6.102)
    * Lage: Maximiner Hofgarten [Propstberg] (6.1.6.100)
    * Lage: Maximiner Klosterlay [St. Michael] (6.1.7.123)
    * Lage: Maximiner Prälat [Scharzberg] (6.5.1.014)
    * Lage: Meisenberg [Römerlay] (6.4.1.019)
    * Lage: Michelsberg (Großlage) (6.1.3)
    * Lage: Monteneubel [Schwarzlay] (6.1.8.139)
    * Lage: Moullay-Hofberg [Vom heißen Stein] (6.1.9.187)
    * Lage: Mühlberg [Kurfürstenlay] (6.1.2.039)
    * Lage: Mühlenberg [St. Michael] (6.1.7.109)
    * Lage: Münsterberg [Goldbäumchen] (6.3.1.025)
    * Lage: Münzlay (Großlage) (6.1.4)
    * Lage: Nacktarsch (Großlage) (6.1.5)
    * Lage: Neuwingert [Weinhex] (6.3.5.139)
    * Lage: Niederberg-Helden [Kurfürstenlay] (6.1.2.046)
    * Lage: Niederberg [Michelsberg] (6.1.3.070)
    * Lage: Nies'chen [großlagenfrei] (6.4.1.005)
    * Lage: Nikolausberg [Rosenhang] (6.3.3.069)
    * Lage: Nonnenberg [Münzlay] (6.1.4.083)
    * Lage: Nonnengarten [Vom heißen Stein] (6.1.9.177)
    * Lage: Nonnengarten [Vom heißen Stein] (6.1.9.183)
    * Lage: Nussberg [Schwarze Katz] (6.3.4.091)
    * Lage: Nußwingert [Michelsberg] (6.1.3.078)
    * Lage: Ohligsberg [Kurfürstenlay] (6.1.2.041)
    * Lage: Osterlämmchen [Grafschaft] (6.3.2.047)
    * Lage: Palmberg-Terrassen [Grafschaft] (6.3.2.055)
    * Lage: Paradies [Nacktarsch] (6.1.5.096)
    * Lage: Paulinsberg [Kurfürstenlay] (6.1.2.021)
    * Lage: Paulinshofberger [Kurfürstenlay] (6.1.2.022)
    * Lage: Paulinslay [Kurfürstenlay] (6.1.2.034)
    * Lage: Petersberg [Grafschaft] (6.3.2.050)
    * Lage: Petersborn-Kabertchen [Schwarze Katz] (6.3.4.092)
    * Lage: Pfarrgarten [Rosenhang] (6.3.3.067)
    * Lage: Pfirsichgarten [Grafschaft] (6.3.2.048)
    * Lage: Pilgerberg [Königsberg] (6.2.2.023)
    * Lage: Pinnerkreuzberg [Goldbäumchen] (6.3.1.007)
    * Lage: Pommerell [Schwarze Katz] (6.3.4.093)
    * Lage: Portnersberg [Schwarzlay] (6.1.8.173)
    * Lage: Prälat [Schwarzlay] (6.1.8.145)
    * Lage: Propstberg (Großlage) (6.1.6)
    * Lage: Pulchen [Scharzberg] (6.5.1.005)
    * Lage: Quiriniusberg [Schloß Bübingen] (6.6.1.524)
    * Lage: Rathausberg [Rosenhang] (6.3.3.065)
    * Lage: Raul [Scharzberg] (6.5.1.029)
    * Lage: Rausch [Scharzberg] (6.5.1.039)
    * Lage: Reinig auf der Burg [Gipfel] (6.2.1.016)
    * Lage: Ritsch [St. Michael] (6.1.7.121)
    * Lage: Ritterpfad [Scharzberg] (6.5.1.053)
    * Lage: Rochusfels [Gipfel] (6.2.1.007)
    * Lage: Römerberg [Gipfel] (6.2.1.009)
    * Lage: Römerberg [Grafschaft] (6.3.2.052)
    * Lage: Römerberg [Kurfürstenlay] (6.1.2.019)
    * Lage: Römerberg [Propstberg] (6.1.6.103)
    * Lage: Römerberg [Schloß Bübingen] (6.6.1.521)
    * Lage: Römergarten [Rosenhang] (6.3.3.061)
    * Lage: Römerhang [Schwarzlay] (6.1.8.175)
    * Lage: Römerlay (Großlage) (6.1.10.208)
    * Lage: Römerlay (Großlage) (6.1.10)
    * Lage: Römerpfad [Kurfürstenlay] (6.1.2.026)
    * Lage: Römerquelle [Schwarze Katz] (6.3.4.095)
    * Lage: Rosenberg [Gipfel] (6.2.1.017)
    * Lage: Rosenberg [Goldbäumchen] (6.3.1.016)
    * Lage: Rosenberg [Goldbäumchen] (6.3.1.017)
    * Lage: Rosenberg [Grafschaft] (6.3.2.051)
    * Lage: Rosenberg [Kurfürstenlay] (6.1.2.010)
    * Lage: Rosenberg [Kurfürstenlay] (6.1.2.035)
    * Lage: Rosenberg [Michelsberg] (6.1.3.052)
    * Lage: Rosenberg [Michelsberg] (6.1.3.071)
    * Lage: Rosenberg [Münzlay] (6.1.4.091)
    * Lage: Rosenberg [Rosenhang] (6.3.3.066)
    * Lage: Rosenberg [Rosenhang] (6.3.3.070)
    * Lage: Rosenberg [Rosenhang] (6.3.3.077)
    * Lage: Rosenberg [Scharzberg] (6.5.1.030)
    * Lage: Rosenberg [Scharzberg] (6.5.1.060)
    * Lage: Rosenberg [Schwarzlay] (6.1.8.149)
    * Lage: Rosenberg [Vom heißen Stein] (6.1.9.184)
    * Lage: Rosenberg [Weinhex] (6.3.5.134)
    * Lage: Rosenborn [Schwarze Katz] (6.3.4.096)
    * Lage: Rosengärtchen [Michelsberg] (6.1.3.058)
    * Lage: Rosengarten [Schwarzlay] (6.1.8.161)
    * Lage: Rosenhang (Großlage) (6.3.3)
    * Lage: Rosenlay [Kurfürstenlay] (6.1.2.045)
    * Lage: Roterd [Michelsberg] (6.1.3.059)
    * Lage: Röttgen [Weinhex] (6.3.5.138)
    * Lage: Saarfeilser Marienberg [Scharzberg] (6.5.1.041)
    * Lage: Schäferlay [Vom heißen Stein] (6.1.9.178)
    * Lage: Scharzberg (Großlage) (6.5.1.061)
    * Lage: Scharzberg (Großlage) (6.5.1)
    * Lage: Schatzgarten [Schwarzlay] (6.1.8.162)
    * Lage: Scheidterberg [Scharzberg] (6.5.1.003)
    * Lage: Schelm [Vom heißen Stein] (6.1.9.179)
    * Lage: Schießlay [St. Michael] (6.1.7.122)
    * Lage: Schlangengraben [Scharzberg] (6.5.1.062)
    * Lage: Schleidberg [Gipfel] (6.2.1.001)
    * Lage: Schlemmertröpfchen [Grafschaft] (6.3.2.036)
    * Lage: Schloßberg [Goldbäumchen] (6.3.1.008)
    * Lage: Schloßberg [großlagenfrei] (6.4.1.012)
    * Lage: Schloßberg [Kurfürstenlay] (6.1.2.007)
    * Lage: Schloßberg [Kurfürstenlay] (6.1.2.023)
    * Lage: Schloßberg [Münzlay] (6.1.4.087)
    * Lage: Schloßberg [Rosenhang] (6.3.3.058)
    * Lage: Schloßberg [Scharzberg] (6.5.1.011)
    * Lage: Schloßberg [Scharzberg] (6.5.1.035)
    * Lage: Schloßberg [Scharzberg] (6.5.1.063)
    * Lage: Schloßberg [Schloß Bübingen] (6.6.1.520)
    * Lage: Schloßberg [Schwarzlay] (6.1.8.131)
    * Lage: Schloßberg [Schwarzlay] (6.1.8.163)
    * Lage: Schloßberg [St. Michael] (6.1.7.108)
    * Lage: Schloßberg [Weinhex] (6.3.5.120)
    * Lage: Schloß Bübingen (Großlage) (6.6.1.)
    * Lage: Schloß Saarsteiner [Scharzberg] (6.5.1.046)
    * Lage: Schloß Saarsteiner Schloßberg [Scharzberg] (6.5.1.047)
    * Lage: Schloß Thorner Kupp [Gipfel] (6.2.1.004)
    * Lage: Schubertslay [Michelsberg] (6.1.3.066)
    * Lage: Schützenlay [Grafschaft] (6.3.2.049)
    * Lage: Schwarze Katz (Großlage) (6.3.4)
    * Lage: Schwarzenberg [Rosenhang] (6.3.3.084)
    * Lage: Schwarzlay (Großlage) (6.1.8)
    * Lage: Servatiusberg [Rosenhang] (6.3.3.062)
    * Lage: Silberberg [Rosenhang] (6.3.3.071)
    * Lage: Sonneck [Grafschaft] (6.3.2.041)
    * Lage: Sonneck [Schwarze Katz] (6.3.4.102)
    * Lage: Sonnenberg [Goldbäumchen] (6.3.1.009)
    * Lage: Sonnenberg [großlagenfrei] (6.4.1.020)
    * Lage: Sonnenberg [Scharzberg] (6.5.1.009)
    * Lage: Sonnenberg [Scharzberg] (6.5.1.012)
    * Lage: Sonnenberg [Scharzberg] (6.5.1.024)
    * Lage: Sonnenberg [St. Michael] (6.1.7.119)
    * Lage: Sonnenlay [Kurfürstenlay] (6.1.2.031)
    * Lage: Sonnenlay [Schwarzlay] (6.1.8.164)
    * Lage: Sonnenlay [St. Michael] (6.1.7.111)
    * Lage: Sonnenring [Weinhex] (6.3.5.129)
    * Lage: Sonnenuhr [Goldbäumchen] (6.3.1.022)
    * Lage: Sonnenuhr [Kurfürstenlay] (6.1.2.027)
    * Lage: Sonnenuhr [Michelsberg] (6.1.3.060)
    * Lage: Sonnenuhr [Münzlay] (6.1.4.084)
    * Lage: Sonnenuhr [Münzlay] (6.1.4.088)
    * Lage: Sorentberg [Vom heißen Stein] (6.1.9.188)
    * Lage: St. Castorhöhle [Goldbäumchen] (6.3.1.020)
    * Lage: Stefanslay [Kurfürstenlay] (6.1.2.042)
    * Lage: Steffensberg [Nacktarsch] (6.1.5.097)
    * Lage: Steffensberg [Schwarzlay] (6.1.8.140)
    * Lage: Steinberger [Scharzberg] (6.5.1.006)
    * Lage: Steinchen [Weinhex] (6.3.5.114)
    * Lage: Stephansberg [Schwarze Katz] (6.3.4.101)
    * Lage: Stephanus-Rosengärtchen [Kurfürstenlay] (6.1.2.043)
    * Lage: St. Georgshof [Gipfel] (6.2.1.014)
    * Lage: Stirn [Scharzberg] (6.5.1.066)
    * Lage: St. Martiner Hofberg [Römerlay] (6.1.10.201)
    * Lage: St. Martiner Klosterberg [Römerlay] (6.1.10.207)
    * Lage: St. Martin [St. Michael] (6.1.7.110)
    * Lage: St. Matheiser [Römerlay] (6.1.10.202)
    * Lage: St. Maximiner Kreuzberg [Römerlay] (6.1.10.203)
    * Lage: St. Michael (Großlage) (6.1.7)
    * Lage: Stolzenberg [Weinhex] (6.3.5.113)
    * Lage: St. Petrusberg [Römerlay] (6.1.10.204)
    * Lage: Stubener Klostersegen [Rosenhang] (6.3.3.085)
    * Lage: Taubenhaus [Schwarzlay] (6.1.8.165)
    * Lage: Thiergarten Felsköpfchen [Römerlay] (6.1.10.206)
    * Lage: Thiergarten Unterm Kreuz [Römerlay] (6.1.10.205)
    * Lage: Thomasberg [Schwarzlay] (6.1.8.132)
    * Lage: Timpert [großlagenfrei] (6.4.1.006)
    * Lage: Treppchen [Michelsberg] (6.1.3.067)
    * Lage: Treppchen [Rosenhang] (6.3.3.082)
    * Lage: Treppchen [Schwarzlay] (6.1.8.146)
    * Lage: Übereltzer [Goldbäumchen] (6.3.1.018)
    * Lage: Uhlen [Weinhex] (6.3.5.140)
    * Lage: Ungsberg [Schwarzlay] (6.1.8.166)
    * Lage: Unterberg [Scharzberg] (6.5.1.007)
    * Lage: Urbelt [Scharzberg] (6.5.1.008)
    * Lage: Vogelsang [Scharzberg] (6.5.1.048)
    * Lage: Vogteiberg [Rosenhang] (6.3.3.078)
    * Lage: Vom heißen Stein (Großlage) (6.1.9)
    * Lage: Wahrsager [Rosenhang] (6.3.3.079)
    * Lage: Weinhex (Großlage) (6.3.5)
    * Lage: Weinkammer [Schwarzlay] (6.1.8.141)
    * Lage: Weisenstein [Kurfürstenlay] (6.1.2.011)
    * Lage: Weißenberg [Weinhex] (6.3.5.121)
    * Lage: Weisser Berg [Vom heißen Stein] (6.1.9.180)
    * Lage: Wendelstück [Schwarzlay] (6.1.8.133)
    * Lage: Woogberg [Rosenhang] (6.3.3.072)
    * Lage: Würtzberg [Scharzberg] (6.5.1.049)
    * Lage: Würzgarten [Schwarzlay] (6.1.8.167)
    * Lage: Würzgarten [Schwarzlay] (6.1.8.169)
    * Lage: Würzgarten [St. Michael] (6.1.7.124)
    * Lage: Würzlay [Weinhex] (6.3.5.127)
    * Lage: Zeisel [Goldbäumchen] (6.3.1.027)
    * Lage: Zellerberg [St. Michael] (6.1.7.116)
    * Lage: Zeppwingert [Schwarzlay] (6.1.8.142)
    * Lage: Zollturm [Schwarzlay] (6.1.8.168)
    * Rebsorte: Riesling [weiss] (Q456471)
    * Rebsorte: Müller-Thurgau / Rivaner [weiss] (Q681670)
    * Rebsorte: Sauvignon Blanc [weiss] (Q44542)
    * Rebsorte: Elbling [weiss] (Q1325364)
    * Rebsorte: Grauburgunder / Ruländer / Pinot Gris [weiss] (Q778601)
    * Rebsorte: Chardonnay [weiss] (Q213332)
    * Rebsorte: Auxerrois / Malbec [weiss] (Q1414045)
    * Rebsorte: Weißburgunder / Pinot blanc [weiss] (Q950514)
    * Rebsorte: Spätburgunder / Pinot noir [rot] (Q223701)
    * Rebsorte: other [weiss]
    * Rebsorte: other [rot]
    * Farbe: Rotwein
    * Farbe: Weisswein
    * Farbe: Rosé/Rotling
    * Farbe: other
    * Taste: dry (trocken)
    * Taste: semi-dry (halbtrocken / feinherb)
    * Taste: semi-sweet (lieblich)
    * Taste: sweet (süß)
    * Taste: other
    * Taste: historical
    * Aging: Barrique-Ausbau
    * Aging: Flaschengärung
    * qualityLevel: Landwein
    * qualityLevel: Tafelwein/Wein
    * qualityLevel: Qualitätswein
    * qualityLevel: Prädikatswein
    * qualityLevel: historical
    * qualityProduction: Erzeugerabfüllung
    * qualityProduction: Gutsabfüllung
    * qualityProduction: Händische Weinlese
    * qualityProduction: other
    * qualityGrapes: Kabinett
    * qualityGrapes: Spätlese
    * qualityGrapes: Auslese
    * qualityGrapes: Beerenauslese
    * qualityGrapes: Trockenbeerenauslese
    * qualityGrapes: Eiswein
    * qualityGrapes: historical
    * qualityGrapes: other
    * Weingut: Weingut Maximin Grünhaus (Q2556072)
    * Weingut: #### (Q)
    * Vertrieb: Karl Ziegler
    * other.

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

#### numNorm
A normalized expression of the number present on the label, as float (or an integer).

- Status: Optional.
- Contained by element: 
    * [wineMillesime](#wineMillesime)
    * [alcohol](#alcohol)
    * [volume](#volume)
    * [controlNumber](#controlNumber)
    * [barrelNumber](#barrelNumber)
    * [labelNumber](#labelNumber).
- Possible values: This element has no default values.

#### pageID
(no data)

- Status: Optional.
- Contained by element: [collectionContext](#collectionContext).
- Possible values: This element has no default values.

#### position
(position) The position of a visual or textual element on the label surface, in a grid of nine quadrants. The quadrants are numbered like on the number-pad of a phone, starting at the top left with 1 and ending at the bottom right with 9. Any quadrant that the figure covers to a significant extent is included in the position description. 

- Status: Optional.
- Contained by element: 
    * [frame](#frame)
    * [figure](#figure)
    * [wineMillesime](#wineMillesime)
    * [wineColor](#wineColor)
    * [wineGrapes](#wineGrapes)
    * [wineTaste](#wineTaste)
    * [wineAging](#wineAging)
    * [qualityGrapes](#qualityGrapes)
    * [qualityLevel](#qualityLevel)
    * [qualityAward](#qualityAward)
    * [qualityLabel](#qualityLabel)
    * [qualityProduction](#qualityProduction)
    * [qualityHistorical](#qualityHistorical)
    * [agent](#agent)
    * [location](#location)
    * [alcohol](#alcohol)
    * [volume](#volume)
    * [controlNumber](#controlNumber)
    * [barrelNumber](#barrelNumber)
    * [labelNumber](#labelNumber)
    * [otherText](#otherText).
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
    * undetermined
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

#### relItems
(no data)

- Status: Mandatory.
- Contained by element: [relation](#relation).
- Possible values: This element has no default values.

#### relType
(no data)

- Status: Mandatory.
- Contained by element: [relation](#relation).
- Possible values: 
    * equivalence
    * similarity
    * contrast
    * text-in-image
    * text-in-frame
    * text-as-frame
    * image-in-text
    * image-in-image
    * image-in-frame
    * other.

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
    * free-form
    * other.

#### sizeH
The height of the label measured in millimeters. (This attribute is mandatory, but can also take the value "tbc" if the size data is not available.)

- Status: Optional.
- Contained by element: [physical](#physical).
- Possible values: This element has no default values.

#### sizeV
The width of the label measured in millimeters. (This attribute is mandatory, but can also take the value "tbc" if the size data is not available.)

- Status: Optional.
- Contained by element: [physical](#physical).
- Possible values: This element has no default values.

#### textPosition
(no data)

- Status: Optional.
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
    * typography
    * website
    * recommendation
    * warning
    * other.

#### uri
(uniform resource identifier) Für einen Link zu weiteren Informationen.

- Status: Optional.
- Contained by element: [metadata](#metadata), [licence](#licence), [agent](#agent), [location](#location).
- Possible values: https://creativecommons.org/licenses/by/4.0/, https://github.com/dh-trier/wlv.

#### wdw
(no data)

- Status: Optional.
- Contained by element: 
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
    * vineyard / Lage
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
