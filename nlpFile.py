#Import required libraries
import string
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import  WordNetLemmatizer

#view the first 10 stopwords present in teh english corpus
stopwords_view=stopwords.words('english')[0:10]
print(stopwords_view)
print()

#Create a text sentence
text_sentence="This is the first text string!. Wow!!, this is amazing."



#sentence tokenize
print("After sentence tokenization")
sentence_tokenize=sent_tokenize(text_sentence)
print(sentence_tokenize)
print()



# word tokenize
print ("after word tokenization ")
for sent in sentence_tokenize:
    print(word_tokenize(sent))
print()


#eliminate the punctuation un front of the character and print
print("sentence without punctuations")
no_punctuation=" "

for c in text_sentence:
    if c not in string.punctuation:
        no_punctuation=no_punctuation+c

print (no_punctuation)
print()

#split each words present in the new sentence
print("spliited words without punctuations ")
print(no_punctuation.split())
print()



#Eliminate stopwords
print("elimnation of stopwords")
clean_sentence= ""

for word in no_punctuation.split():
    if word.lower() not in stopwords.words("english"):
        clean_sentence=clean_sentence+" "+word

print(clean_sentence)


#Stemming
print("Stemming the words")
porter=PorterStemmer()
split_Clean_sentence=clean_sentence.split()
print(split_Clean_sentence)

for i in split_Clean_sentence:
    print(porter.stem(i))

print()


#Lemmatization
print("lemmatization of words")
wnl=WordNetLemmatizer()
lemmitizeText=" "

for w in split_Clean_sentence:
    lemmitizeText=lemmitizeText+" "+ wnl.lemmatize(w)

print(lemmitizeText)

#POS tagging
print("pos tagged words")
tagged=nltk.pos_tag(lemmitizeText.split())
print(tagged)
