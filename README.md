# 486-datacollection



## datacollection.py

This is the python script that grabs usernames from the HuggingFace dataset and then grabs the last 25 comments that user has made. To run this code, make sure you modify reddit_info.txt with your Reddit login information in order to receive an access token for the Reddit API. Check comments in code.


## HuggingFace Dataset

Link: https://huggingface.co/datasets/reddit

Dataset format: 
author (string) - the username of the comment author
body (string) - the comment text
normalizedBody (string) - comment text but normalized
subreddit (string) - name of the subreddit the comment was posted in
subreddit_id (string) - the ID of the subreddit the comment was posted in 
id (string) - I don't know exactly what this is
content (string) - comment text but with the "tl;dr" sections removed
summary (string) - the "td;dr" text of the comment

You can visualize this by looking at the HF_SampleData.txt file where I grabbed the first 1,000 datapoints and used a json formatter on it.


## The Collected Data

This is the data I collected from the first 10,000 usernames in the HuggingFace dataset. 

You can visualize the format by looking at /Our_SampleData/. This folder contains the most recent 25 comments posted by that first 10 usernames in the HuggingFace dataset. I used a json formatter on all of the files so that they are more readable in order for us to better understand how to grab the necessary data we need from the dataset.
