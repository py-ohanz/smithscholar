#We might have to use the "require" cmd in place of library

library(tm)
df<-read.csv(myfile)

corpus<-Corpus(VectorSource(df$text))
corpus<-tm_map(corpus, content_transformer(tolower))
corpus<-tm_map(corpus, removeNumbers)
corpus<-tm_map(corpus, removeWords, stopwords('english'))
#corpus<-tm_map(corpus, stemDocument, language = "english") 
corpus<-tm_map(corpus, removePunctuation)

tdm<-TermDocumentMatrix(corpus)

tdmatrix<-as.matrix(tdm)
wordfreq<-sort(rowSums(tdmatrix), decreasing = TRUE)