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
