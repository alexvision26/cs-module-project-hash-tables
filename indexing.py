records = {
    ("Tim", "Texas"),
    ("Adam", "Florida"),
    ("Austin", "Florida"),
    ("Kai", "South Carolina"),
    ("Jud", "Phoebos"),
    ("Eric", "Utah"),
    ("Emma", "Florida"),
    ("Anna", "Texas"),
    ("Leo", "New York"),
    ("James", "New York"),
    ("Andrew", "Utah"),
    ("Alex", "Oregon"),
    ("Mandi", "Virginia"),
}

# given a list of records, build an index
# so we can quickly find everyone in a given state

# Plan
# iterate through the tuples in our list
# build a dictionary as we go
# use states as key, and names as values

### if state isn't in the dictionary, add it
### value: [name1, name2, name3]

### possible value data structures: list, set, nest hashtable
### {state: {name: lastName}}

def build_index(records):
    index = {}

    for name, state in records:
        if state in index:
            index[state].append(name)
        else:
            index[state] = []
            index[state].append(name)

    return index

idx = build_index(records)

print(idx["Oregon"])