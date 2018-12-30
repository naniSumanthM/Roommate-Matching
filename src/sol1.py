# checks to see if list type values match
# returns a pair of matching keys

prefs = {
    's1': ["a", "b", "c", "d", "e"],
    's2': ["c", "d", "b", "a", "e"],
    's3': ["a", "b", "c", "d", "e"],
    's4': ["c", "d", "e", "b", "e"],
    's5': ["c", "d", "e", "b", "e"],
    's6': ["c", "d", "b", "a", "e"],
    's7': ["e", "b", "a", "c", "d"],
    's8': ["e", "b", "a", "c", "d"],
    's9': ["e", "b", "a", "d", "c"],
    's10': ["e", "b", "a", "d", "c"]
}

matches = {}

for key, value in prefs.items():
    value = tuple(value)
    if value not in matches:
        matches[value] = []
    matches[value].append(key)

print(matches.values())
