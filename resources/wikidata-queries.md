# Wikidata-Queries für Weinlagen

## Alle Weinlagen in Wikidata

https://query.wikidata.org/#%23Cats%0ASELECT%20%3Fitem%20%3FitemLabel%20%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20wdt%3AP31%20wd%3AQ1800229.%20%23%20Must%20be%20of%20a%20vineyard%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cde%22.%20%7D%20%23%20Helps%20get%20the%20label%20in%20your%20language%2C%20if%20not%2C%20then%20en%20language%0A%7D

## Alle Weinlagen in Deutschland

https://query.wikidata.org/#select%20distinct%20%3Fitem%20%3FitemLabel%20%3FitemDescription%20where%20%7B%0A%20%20%20%20%3Fitem%20wdt%3AP31%20wd%3AQ1800229%3B%20%20%23%20Any%20instance%20of%20a%20vineyard%0A%20%20%20%20%20%20%20%20%20%20wdt%3AP17%20wd%3AQ183%3B%20%20%23%20%20Located%20in%20Germany%0A%20%20%20%0A%20%20%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22de%22%20%7D%0A%7D
