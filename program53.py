set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Keep only items common to both sets in set1
set1.intersection_update(set2)

print("Updated set1:", set1)
