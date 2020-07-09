import random

# Read in all the words in one go
cache = {}

with open("c:/Users/alexm/Documents/CS23/Week5/Day1/cs-module-project-hash-tables/applications/markov/input.txt") as f:
    words = f.read()
    words = words.split()

    # print(len(words))

    for idx, word in enumerate(words):
        if word not in cache:
            cache[word] = []
            if idx < len(words) - 1:
                cache[word].append(words[idx+1])
        else:
            if idx < len(words) - 1:
                cache[word].append(words[idx+1])

    print(cache)


    # print(words)
# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here



