#returns all potential matches
#given preferences

prefs = {
    's1': ["a", "b", "c", "d", "e"],
    's2': ["c", "d", "e", "a", "b"],
    's3': ["a", "b", "c", "d", "e"],
    's4': ["c", "d", "e", "b", "e"],
    's5': ["c", "d", "e", "a", "b"]
}

# Get all items of prefs and sort them by key. (Sorting might not be
# necessary, that's something you'll have to decide.)
items_a = sorted(prefs.items(), key=lambda item: item[0])

# Make a copy of the items where we can delete the processed items.
items_b = items_a.copy()

# Set the length for each compared slice.
slice_length = 3

# Calculate how many comparisons will be necessary per item.
max_shift = len(items_a[0][1]) - slice_length

# Create an empty result list for all matches.
matches = []

# Loop all items
print("Comparisons:")
for key_a, value_a in items_a:
    # We don't want to check items against themselves, so we have to
    # delete the first item of items_b every loop pass (which would be
    # the same as key_a, value_a).
    del items_b[0]
    # Loop remaining other items
    for key_b, value_b in items_b:
        print("- Compare {} to {}".format(key_a, key_b))
        # We have to shift the compared slice
        for shift in range(max_shift + 1):
            # Start the slice at 0, then shift it
            start = 0 + shift
            # End the slice at slice_length, then shift it
            end = slice_length + shift
            # Create the slices
            slice_a = value_a[start:end]
            slice_b = value_b[start:end]
            print("  - Compare {} to {}".format(slice_a, slice_b), end="")
            if slice_a == slice_b:
                print(" -> Match!", end="")
                matches += [(key_a, key_b, shift)]
            print("")

print("Matches:")
for key_a, key_b, shift in matches:
    print("- At positions {} to {} ({} elements), {} matches with {}".format(
        shift + 1, shift + slice_length, slice_length, key_a, key_b))
