import spacy # provides an efficient NLP algorithm
import nltk #string processing library


#1
# nlp = spacy.load("en_core_web_sm") # en_core_web_sm is a pretrained model provided by spaCy
# doc = nlp ("I have started my AI learnings.Right now the focus is on NLP, I will focus on AI agent next")
# for sentense in doc.sents:
#     for word in sentense:
#         print(word)

#2
# from nltk.tokenize import sent_tokenize
# sent_tokenize("I have started my AI learnings.Right now the focus is on NLP, I will focus on AI agent next")

#3
# text = text='''
# Look for data to help you address the question. Governments are good
# sources because data from public research is often freely available. Good
# places to start include http://www.data.gov/, and http://www.science.
# gov/, and in the United Kingdom, http://data.gov.uk/.
# Two of my favorite data sets are the General Social Survey at http://www3.norc.org/gss+website/, 
# and the European Social Survey at http://www.europeansocialsurvey.org/.
# '''
# nlp = spacy.load("en_core_web_sm")
# doc = nlp(text)
# websitelist = [token.text for token in doc if token.like_url]
# print(websitelist)

#4
text =  "Tony gave two $ to Peter, Bruce gave 500 € to Steve"
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
currencySymbols = [token.text for token in doc if token.is_currency]
print(currencySymbols)
for token in doc:
    if token.like_num and doc[token.i+1].is_currency:
        print(token.text, doc[token.i+1].text)
