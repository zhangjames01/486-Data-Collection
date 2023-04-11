import sys
import os
import json
import re
import math
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords


stops = set(stopwords.words('english'))
# print(stops)
lemmatizer = WordNetLemmatizer()

def main():
    bad_words = set()
    with open("list-of-bad-words.txt", 'r', encoding='iso-8859-1') as f:
        data = json.load(f)
    for word in data["words"]:
        bad_words.add(str(word))
        bad_words.add(lemmatizer.lemmatize(str(word)))
    
    print(bad_words)

    GamerResultFile = open("gamerSlurResults.txt", "w")
    allResultFile = open("allSlurResults.txt", "w")
    slurs = 0
    words = 0
    with open('all_gamer_words.txt','r') as file:
        text = file.read().lower()
        text = removeSGML(text)
        text = tokenizeText(text)
        for word in text:
            if(word in stops):
                continue
            word = lemmatizer.lemmatize(word)
            words += 1
            if word in bad_words:
                print(word)
                slurs += 1
    GamerResultFile.write("number of words: " + str(words) +"\nnumber of Slurs: " +str(slurs) +"\npercentage: "+str(slurs/words * 100)+"%")
    
    slurs = 0
    words = 0
    with open('all_words.txt','r') as file:
        text = file.read().lower()
        text = removeSGML(text)
        text = tokenizeText(text)
        for word in text:
            if(word in stops):
                continue
            word = lemmatizer.lemmatize(word)
            words += 1
            if word in bad_words:
                print(word)
                slurs += 1
    allResultFile.write("number of words: " + str(words) +"\nnumber of Slurs: " +str(slurs) +"\npercentage: "+str(slurs/words * 100)+ "%")
    
def removeSGML(text):
    return re.sub(r'<.*?>', '', text)

def tokenizeText(text):
    # Account for acronyms and abbreviations
    text = re.sub(r"([A-Za-z]\.)+", r"\1", text)
    # Account for numbers
    text = re.sub(r"(\d+)([,/.])(\d+)", r"\1\2\3", text)
    # Account for dates
    text = re.sub(r"(\d{1,2}[/-]){2}\d{4}", r"\1", text)
    # Account for possessive
    text = re.sub(r"(\w+)(')(s)", r"\1 \2\3", text)
    # Account for hyphenated words
    text = re.sub(r"(\w+)(-)(\w+)", r"\1 \2 \3", text)
    # Tokenize text
    tokens = re.findall(r"[\w']+(?:[-.']\w+)*|[.,!?;]", text)
    tokens = [token for token in tokens if token not in ",.!?;"]
    return tokens
    


if __name__ == '__main__':
    main()