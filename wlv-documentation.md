
# wlv
1, empty
@xml:id: 1, {string}, unconstrained
@url: 1, {url}

§deu: Weinetiketten-Sammlung


## metadata


#### title
1, {string}, unconstrained
@url: ?, {url}

§deu: Titel


#### editor
1, {string}, (lastname, firstname)
@email = {email}
@ref = (authority:identifier)

§deu: Herausgeber


#### institution
?, {string}, unconstrained
@url = (url)  

§deu: Institution


#### location
?, {string}, unconstrained
@ref: \*, {authority:identifier}

§deu: Ort


#### date
1, string
@when: 1, {yyyy-mm-dd}

§deu: Datum


#### licence
1, string
@url: 1, {url}
@abbr: ?, {string}, (short licence name)

§deu: Lizenz


#### curators
1, empty

§deu: Erschließende


##### curatorID
+, {string}, (lastname, firstname)
@xml:id = {string}
@email = {email}
@ref = (authority:identifier)

§deu: Identifikator der/des Erschließenden

## labels
1, empty


### label
+, empty
@curator = {#xml:id} (from curatorID)
@date = {yyyy-mm-dd}
@xml:id = {string}
@url: 1, {url}

§deu: Etikett


#### part, +
?, {string}
@n: 1, {int}
@type: 1, {string}, ["neck", "main", "back", "band"]
@positionH: ?, {string}, ["front","back"]
@positionV: ?,  {string}, ["top","bottom"]




###### physical
1, empty


####### shape
1, string: ["rectangle","square","oval","circle","trapezoid","other"]}
@sizeH = {int} (mm)
@sizeV = {int} (mm)


####### material
1, {string}, ["paper","plastic"]}


###### visual
1, empty


####### frame
?, empty
@position: 1, {string}, ["outer", "inner"]
@type: 1, {string}, ["lines", "band", "pattern", "other"]
@color: ?, {string}, [html color name]


####### background               # eventuell in "visual"?
1, empty
@type: ?, {string}, ["uniform", "pattern", "mixed", "other"]
@color: ?, {string} [(html color name)]


####### figure
\*, {string}, (short free mention of key visual elements)
@n = {int}
@positionH = {string: ["full", "left", "center", "right"]}
@positionV = {string: ["full", "top", "center", "bottom"]}
@shape = {string: ["square","circle","rectangle","oval","other"]}
@type = {string: ["symbol","realistic","coatofarms"]}

######## text
\*, {string}, unconstrained
@type: ?, {string}, ["motto", "signature", "other"]


###### textual
1, empty


####### origin
\*, {string}
originType: 1, {string}, ["vineyard", "wine-region", "country"]
@ref: ?, {authority:identifier} 
@@textual

§deu: Anbaugebiet, genauer: Lage, Anbaugebiet, Produktionsland



####### millesime
?, {string}
@millesimeNorm: 1, (yyyy)
@@textual

§deu: Jahrgang


####### wine-name
\*, {string}
@@textual

§deu: Bezeichnung des Weins


####### grape-variety
?, {string}
@norm: ?, {string}, (normalised designation)
@type: ?, {string}, ["single", "double", "triple", "other"]
@ref: \*, {authority:identifier} 
@@textual


####### quality-statement
\*, {string}
@type: 1, {string}, ["quality", "classification", "award", "bottling", "other"]
@ref: \*, {authority:identifier} 
@@textual



####### wineCharacter
\*, {string}, unconstrained
@type: ?, {string}, ["trocken","feinherb","lieblich"]


###### wineColor
\*, {string}, unconstrained
@type: ?, {string}, ["red", "white", "rosé", "rotling"]
@@textual



####### agent
?, {string}
@role: 1, {string}, ["producer","bottler","distributor","importer", "cooperative", "association", "printer", "other"]
@ref: \*, {authority:identifier} 
@@textual


####### location
?, {string}
@role: 1, {string}, ["producer", "bottler", "distributor","importer", "cooperative", "association", "printer", "other"]
@type: ?, {string}, ["country", "region", "city", "village"]
@ref: \*, {authority:identifier} 
@@textual


####### motto
?, {string}, unconstrained  ##Here or in figure?
@type: 1, {string}, ["standalone", "in-figure"] 
@infigure: ?, {int}, (use int in @n of figure)
@@textual



####### alcohol
?, {string}
@percentage: 1, {float}
@@textual


####### volume
?, {string}
@volume: 1, {int}, (ml)
@@textual


####### control-number
?, {string}
@type: ?, {string}, [""]
@@textual

§deu: "Amtliche Prüfnummer" See: wikidata:Q480240


####### barreNumber
?, {string}
@@textual



####### otherText
?, {string}
@otherTextType: ?, {"description" | "association" | "administrative" | "other" }
@@textual






@@textual 

@fonttype: ?, {string}, ["Antiqua-Sans","Antiqua-Serif","Fraktur","Cursive"]
@fontstyle: ?, {string}, ["recte", "italic", "bold", "smallcaps", "allcaps"]
@fontcolor: ?, {string}, (html color name)
@intialcolor: ?, {string}, (htmlcolor name)
@fontsize: ?, {string}, ["larger","normal","smaller"] -- relative to other text on label


