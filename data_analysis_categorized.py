import sys
import os
import json
import re
import math
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords

# dict of bad words, in the form of {category: [list/set of bad words]}
badwords_dict = {}

stops = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def main():
    # get data directory filepath
    datafolder_Path = os.path.join(os.getcwd(), "bad_words_by_category/")

    # for each .txt file in the directory
    for file_name in os.listdir(datafolder_Path):
        # get class type from doc name, and update classProb with counts for now
        regexMatch = re.search(r"(\w+)\.txt", file_name)
        classType = regexMatch.group(1)
        badwords_dict[classType] = badwords_dict.get(classType, set())

        with open(os.path.join(datafolder_Path, file_name), 'r', encoding='iso-8859-1') as file:
            data = json.load(file)
        for word in data["words"]:
            badwords_dict[classType].add(str(word))
            badwords_dict[classType].add(lemmatizer.lemmatize(str(word)))

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