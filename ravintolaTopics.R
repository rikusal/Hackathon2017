#Näin esikäsittelet ja teet datasta topic modelin
#Aluksi prosessoi käsiteltävää teksti textProcessor funktiolla
# Oikean kielen valinta tärkeää! Samoin stemmaamisen esto (sanat on jo lemmatisoitu)
# Myös omien stoppisanojen lisääminen (lisättävä vektorimuodossa)
# processedFi <- textProcessor("KANSIONNIMI", language = "fi"/"en", stem = FALSE, customstopwords = "stopwords")

# preppaa data prepDocuments funktiolla
# preppedFi <- prepDocuments(processedFi$documents, processedFi$vocab, processedFi$meta)

# Ja sitten pÃ¤Ã¤see luomaa topic modeleja!
# stmFi <- stm(documents = preppedFi$documents, vocab = preppedFi$vocab, K = 10)


#luodaan poistettavien sanojen stopword-lista
stopwords <- c('nãmã', 'vãli', 'hinta', 'yksi', 'tehdã', 'tarjolla', 'tarjoilla', 'tarjota', 'mikã', 'sekã', 'â€“', 'food', 'offer', 'our', 'for', 'you', 'tãmã', 'kerta', 'jãlleen', 'tyhjÃ¤', 'kpl', 'the', 'and', 'och', 'fÃ¥rr', 'with', 'ravi', 'ruoka',  'pii', 'muu','klo', 'tulla', 'mennÃ¤', 'euro', 'eur', 'yes', 'tervetuloa', 'koko', 'your', 'tasty', 'maku', 'maukas', 'maistaa', 'med', 'fÃ¶r', 'som', 'per', 'moni', 'myydÃ¤', 'myÃ¶dÃ¤', 'myãdã', 'restaurant', 'kui', 'vasen', 'syÃ¶dÃ¤', 'det', 'voida', 'tehdÃ¤', 'welcome', 'will', 'from', 'day', 'also', 'come', 'are', 'have')

#prosessoidaan ravintolakuvaukset (poistetaan stopword-listalla olevat sanat sekä duplikaatit) ja prepataan ne topic modelin muodostusta varten
processedFi <- textProcessor("fi", language = "fi", stem = FALSE, customstopwords = stopwords)
preppedFi <- prepDocuments(processedFi$documents, processedFi$vocab, processedFi$meta)

#itse topic modelin muodostaminen. inittype = spectral, jotta useita malleja helpompi vertailla
stmFi <- stm(documents = preppedFi$documents, vocab = preppedFi$vocab, init.type = c("Spectral"), K = 20)

#visualisoidaan tulokset
labelTopics(stmFi, n = 10)
plot(stmFi, n=5)

#sama englanniksi
stopwordsEn <- c('will', 'food', 'restaurant', 'come', 'euro', 'make', 'day', 'eur', 'taste', 'welcome', 'sold', 'kiitos', 'also')
processedEn <- textProcessor("en", language = "en", stem = FALSE, customstopwords = stopwordsEn)
preppedEn <- prepDocuments(processedEn$documents, processedEn$vocab, processedEn$meta)
stmEn <- stm(documents = preppedEn$documents, vocab = preppedEn$vocab, init.type = c("Spectral"), K = 20)
labelTopics(stmEn, n=10)
plot(stmEn, n=5)

#findThoughts eli mitkä kuvaukset edustavat parhaiten mitäkin aihetta
#aluksi muodostetaan character vector kaikista kuvauksista

kuvausVektori <- vector()

vektoriFiles <- list.files()
for (text in vektoriFiles) {
  kuvausVektori <- c(kuvausVektori, read_file(text))
}

#ja sitten itse varsinainen findThoughts funktio
findThoughts(stmEn,texts = kuvausVektori, topics=topicsList3, n=5)
