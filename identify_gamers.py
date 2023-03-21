from datasets import load_dataset # needed to access the huggingface dataset

# grabs the dataset from huggingface
dataset = load_dataset("reddit")

subreddits = []
with open('gaming_subreddits.txt','r') as file:
    for line in file:
        subreddits.append(line[:-1])

print(subreddits)

identified_gamers = []
for i in range(10000):
    if(str(dataset['train'][i].get("subreddit")).lower() in subreddits):
        identified_gamers.append(i)

outputFile = open("identified_gamers.txt", "w")
for i in identified_gamers:
    outputFile.write(str(i) + "\n")
outputFile.close()
