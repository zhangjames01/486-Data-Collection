# 486-datacollection



## datacollection.py

This is the python script that grabs usernames from the HuggingFace dataset and then grabs the last 25 comments that user has made. To run this code, make sure you modify reddit_info.txt with your Reddit login information in order to receive an access token for the Reddit API and create your own CLIENT_ID and SECRET_KEY. To create your own CLIENT_ID and SECRET_KEY, go to this website: https://www.reddit.com/prefs/apps. I followed this tutorial to use the Reddit API: https://youtu.be/FdjVoOf9HN4. Here is the link to the Reddit API documentation: https://www.reddit.com/dev/api/. To access the HuggingFace dataset, you will need to run this command in the terminal: $ pip install datasets

Let me know if you have any questions.


## HuggingFace Dataset

Link: https://huggingface.co/datasets/reddit

Dataset format: 
- author (string) - the username of the comment author
- body (string) - the comment text
- normalizedBody (string) - comment text but normalized
- subreddit (string) - name of the subreddit the comment was posted in
- subreddit_id (string) - the ID of the subreddit the comment was posted in 
- id (string) - I don't know exactly what this is
- content (string) - comment text but with the "tl;dr" sections removed
- summary (string) - the "td;dr" text of the comment

You can visualize this by looking at the HF_SampleData.txt file where I grabbed the first 1,000 datapoints and used a json formatter on it.


## The Collected Data

The Gamer_Data/ folder contains the data I collected from the identified gamers of the first 10,000 comments in the HuggingFace dataset. The data is in the form of text files written in a json format. The text files names contain the index number pertaining to the index they are in the HuggingFace dataset.

I identified the users that are gamers by checking if the comment in the HuggingFace dataset was posted in a gaming related subreddit. I got the list of gaming related subreddits from this page: https://www.reddit.com/r/gaming/wiki/list-sorted-by-subscribers/.

The Data_10000/ folder contains the data I collected from the first 10,000 usernames in the HuggingFace dataset. The data is in the form of text files written in a json format.

You can visualize the format by looking at /Reddit_SampleData/. This folder contains the most recent 25 comments posted by that first 10 usernames in the HuggingFace dataset. I used a json formatter on all of the files so that they are more readable in order for us to better understand how to grab the necessary data we need from the dataset.
