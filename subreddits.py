subreddits = []

with open('unparsed_list.txt','r') as file:
    for line in file:
        for word in line.split():
            if(word[0] == '/'):
                subreddits.append(word)

outputFile = open("gaming_subreddits.txt", "w")
for i in subreddits:
    outputFile.write("%s\n" % i[3:].lower())
outputFile.close()

