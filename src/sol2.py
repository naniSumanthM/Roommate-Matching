# checks to see if list type values match
# returns a pair of matching keys

from itertools import groupby
prefs = {
    's1': ["a", "b", "c", "d", "e"],
    's2': ["c", "d", "e", "a", "b"],
    's3': ["a", "b", "c", "d", "e"],
    's4': ["c", "d", "e", "b", "e"],
    's5': ["c", "d", "e", "a", "b"]
}

matches = [[t[0] for t in g] for k, g in groupby(
    sorted(prefs.items(), key=lambda x:x[1]), lambda x:x[1])]

print(matches)
