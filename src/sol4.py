from itertools import combinations


#iterates through all values, and checks to see if at least three elements match in a row in any location
prefs = {
    's1': ["a", "b", "c", "d", "e"],
    's2': ["e", "d", "a", "b", "c"],
    's3': ["a", "b", "c", "d", "e"],
    's4': ["c", "d", "e", "b", "e"],
    's5': ["c", "d", "e", "a", "b"]
}

results = []
for ki, vi in prefs.items():
    for kj, vj in prefs.items():
        # skip checking same values on same keys !
        if ki == kj:
            continue

        iCombinations = [vi[n:n+3] for n in range(len(vi)-2)]
        jCombinations = [vj[n:n+3] for n in range(len(vj)-2)]

        # checking all combinations
        if any([ic in jCombinations for ic in iCombinations]):
            match = tuple(sorted([ki, kj]))
            results.append(match)

# print a unique set
print(set(results))