import sys
import os
import json
import re
import math

# TODO - dict of users, in the form of { "user_id" : [{ attribute: value }] }
# probably best to store posts within the dict of users, like a dict of dict

# Stopgap - list of posts dicts
posts = []

# TODO - break up data analysis into helper functions

# main function, to be run with cmd arguments
def main():
    # get data directory filepath
    datafolder_Path = os.path.join(os.getcwd(), "Gamer_Data/")

    # iterate through user data files
    for user_filename in os.listdir(datafolder_Path):
        # get user_id from file name and initialize 
        regexMatch = re.search(r"(\d+)\.txt", user_filename)
        user_id = regexMatch.group(1)

        # parse through file as json
        with open(os.path.join(datafolder_Path, user_filename), 'r', encoding='iso-8859-1') as user_file:
            userdata_json = json.load(user_file)
            print(user_id)

            # parses to internal posts dict (based on debug state)
            # continues to next user file if entry does not exists (im looking at you, user_id 102)
            posts_dict_parent = userdata_json.get("data", None)
            if (posts_dict == None): 
                continue
            posts_dict = posts_dict_parent.get("children", None)
            if (posts_dict == None): 
                continue

            # extract relevant post information
            for post_dict in posts_dict:
                post_data = post_dict.get("data", None)
                if post_data == None:
                    continue
                
                # extracted info for each post
                subreddit_name = post_data.get("subreddit", None)
                post_title = post_data.get("link_title", None)
                post_content = post_data.get("body", None)

if __name__ == '__main__':
    main()