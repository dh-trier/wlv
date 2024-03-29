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
