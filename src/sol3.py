# https://stackoverflow.com/questions/53935130/how-to-compare-elements-of-a-list-in-a-python-maps-value-and-check-to-see-if-a/53935340#53935340
#check to see if the first three elements match
#returns matching keys

prefs = {
    's1': ["c", "d", "a", "b", "c"],
    's2': ["c", "d", "e", "a", "b"],
    's3': ["d", "c", "a", "b", "c"],
    's4': ["c", "d", "e", "b", "e"],
    's5': ["c", "d", "e", "a", "b"]
}

results = []
for ki, vi in prefs.items():
    for kj, vj in prefs.items():
        # skip checking same values on same keys !
        if ki == kj:
            continue
            # slice the lists to test first 3 characters
        if vi[:3] == vj[:3]:
            # sort results to eliminate duplicates
            match = tuple(sorted([ki, kj]))
            results.append(match)

print(set(results))
