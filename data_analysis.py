import sys
import os
import json
import re
import math

def main():
    bad_words = []
    with open("list-of-bad-words.txt", 'r', encoding='iso-8859-1') as f:
        data = json.load(f)
    for word in data["words"]:
        bad_words.append(str(word))
    print(bad_words)

    GamerResultFile = open("gamerSlurResults.txt", "w")
    allResultFile = open("allSlurResults.txt", "w")
    slurs = 0
    words = 0
    with open('all_gamer_words.txt','r') as file:
        for line in file:
            for word in line.split(" "):
                words += 1
                if word in bad_words:
                    print(word)
                    slurs += 1
    GamerResultFile.write("number of words: " + str(words) +"\nnumber of Slurs: " +str(slurs) +"\npercentage: "+str(slurs/words * 100)+"%")
    
    slurs = 0
    words = 0
    with open('all_words.txt','r') as file:
        for line in file:
            for word in line.split(" "):
                words += 1
                if word in bad_words:
                    print(word)
                    slurs += 1
    allResultFile.write("number of words: " + str(words) +"\nnumber of Slurs: " +str(slurs) +"\npercentage: "+str(slurs/words * 100)+ "%")
    
    


if __name__ == '__main__':
    main()