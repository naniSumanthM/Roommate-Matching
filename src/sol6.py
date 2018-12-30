#need to iterate over a set of values whose type is list
#check to see if elements of one list prirorities exist in another list
#The list can have n number of elements upto 5 elements

prefs = {
    's1': ['a', 'b', 'c'],
    's2': ['a', 'b'],
    's3': ['d', 'c', 'a', 'e'],
    's4': ['a']
}

results = []
for ki,vi in prefs.items():
    for kj, vj in prefs.items():
        if ki == kj:
            continue
