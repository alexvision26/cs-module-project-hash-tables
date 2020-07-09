def no_dups(s):
    cache = {}
    s = s.split()
    # s = set(s)
    for x in s:
        if x not in cache:
            cache[x] = 0
        else:
            continue
    
    res = ' '.join(cache.keys())

    return res

# print(no_dups)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))