

cache = {}

def build_cache():
    whitelist = set("abcdefghijklmnopqrstuvwxyz '")
    f = open("c:/Users/alexm/Documents/CS23/Week5/Day1/cs-module-project-hash-tables/applications/histo/robin.txt", "r")
    words = f.read()
    words = words.lower()
    new_str = ''.join(filter(whitelist.__contains__, words))
    new_str = new_str.split()


    for word in new_str:
        if word not in cache:
            cache[word] = 1
        else:
            cache[word] += 1

    return cache

def display_words(s):
    count = list(s.values())
    word_count = 0
    for x in count:
        word_count += x

    s = sorted(s.items(), key=lambda x: x[1], reverse=True)
    print("Word Count: ",word_count)
    for k, v in s:
        print(k, "."*(20 - len(k)), '#'*v)

new_list = build_cache()

display_words(new_list)
