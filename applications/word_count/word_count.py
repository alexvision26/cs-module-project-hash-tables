

def word_count(s):
    cache = {}
    whitelist = set("abcdefghijklmnopqrstuvwxyz '")
    s = s.lower()
    s = s.replace('\t', " ")
    s = s.replace('\r', " ")
    s = s.replace('\n', " ")
    # s = s.strip("")
    new_str = ''.join(filter(whitelist.__contains__, s))
    new_str = new_str.split()

    print(new_str)
    
    for word in new_str:
        if word in cache:
            cache[word] += 1
        else:
            cache[word] = 1
    
    return cache

# word_count

print('a a\ra\na\ta \t\r\n')


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('a a\ra\na\ta \t\r\n'))