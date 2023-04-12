import sys
import os
import json
import re
import math

# given the directory to the .txt files for Nintendo's censored word list (3DS, source is Reddit: https://www.reddit.com/r/3dshacks/comments/52ynpz/changes_to_the_bad_word_list_on_111034/)
def main():
    Nintendo_censor_list = set()
    
    # get data directory filepath
    datafolder_Path = os.path.join(os.getcwd(), "ctr_bad_word_list_v9217/")

    # for each .txt file in the directory
    for file_name in os.listdir(datafolder_Path):
        with open(os.path.join(datafolder_Path, file_name), 'r', encoding='iso-8859-1') as file:
            file_content = file.readlines()
            for file_line in file_content:
                # extracts only alphanumeric ASCII characters
                extracted = re.split(r'\W+', file_line)
                randomno = 0
                for word in extracted:
                    Nintendo_censor_list.add(word)
    
    OutputFile = open("NintendoCompiledCensoredList.txt", "w")
    for word in Nintendo_censor_list:
        OutputFile.write(word + '\n')


if __name__ == '__main__':
    main()