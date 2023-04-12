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
    # GENERAL - reading in list of words
    bad_words = set()
    with open("list-of-bad-words.txt", 'r', encoding='iso-8859-1') as f:
        data = json.load(f)
    for word in data["words"]:
        bad_words.add(str(word))
        bad_words.add(lemmatizer.lemmatize(str(word)))

    # CATEGORIZED - reading in list of words by category
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


    # DATA ANALYSIS - Getting counts and return the data analyst statistics ----------------------------------------------------
    GamerResultFile = open("gamerSlurResults.txt", "w")
    GeneralResultFile = open("allSlurResults.txt", "w")

    # GAMER ---------------------------------------------------------------------
    words_gamer = 0
    slurs_gamer = 0
    slurs_count_by_category_gamer = {}
    with open('all_gamer_words.txt','r') as file:
        text = file.read().lower()
        text = removeSGML(text)
        text = tokenizeText(text)
        for word in text:
            if(word in stops):
                continue
            word = lemmatizer.lemmatize(word)
            words_gamer += 1
            # update general number of slurs
            if word in bad_words:
                slurs_gamer += 1
            # update count of slurs by category
            for category in badwords_dict:
                if word in badwords_dict[category]:
                    # print(str(word) + " in " + str(category))
                    slurs_count_by_category_gamer[category] = slurs_count_by_category_gamer.get(category, 0) + 1
                    break
    # OUTPUT 
    GamerResultFile.write("number of words: " + str(words_gamer) + "\n")
    GamerResultFile.write("number of slurs: " + str(slurs_gamer) +"\npercentage: "+ str(slurs_gamer/words_gamer * 100) + "% \n")
    for category in badwords_dict:
        GamerResultFile.write("\nnumber of slurs for category " + str(category) + ": " + str(slurs_count_by_category_gamer[category]) +"\npercentage: "+str(slurs_count_by_category_gamer[category]/words_gamer * 100)+"%")
    
    # GENERAL ---------------------------------------------------------------------
    words_general = 0
    slurs_general = 0
    slurs_count_by_category_general = {}
    with open('all_words.txt','r') as file:
        text = file.read().lower()
        text = removeSGML(text)
        text = tokenizeText(text)
        for word in text:
            if(word in stops):
                continue
            word = lemmatizer.lemmatize(word)
            words_general += 1
            # update general number of slurs
            if word in bad_words:
                slurs_general += 1
            # update count of slurs by category
            for category in badwords_dict:
                if word in badwords_dict[category]:
                    # print(str(word) + " in " + str(category))
                    slurs_count_by_category_general[category] = slurs_count_by_category_general.get(category, 0) + 1
                    break
    # OUTPUT 
    GeneralResultFile.write("number of words: " + str(words_general) + "\n")
    GeneralResultFile.write("number of slurs: " + str(slurs_general) +"\npercentage: "+ str(slurs_general/words_general * 100) + "% \n")
    for category in badwords_dict:
        GeneralResultFile.write("\nnumber of slurs for category " + str(category) + ": " + str(slurs_count_by_category_general[category]) +"\npercentage: "+str(slurs_count_by_category_general[category]/words_general * 100)+"%")
    
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