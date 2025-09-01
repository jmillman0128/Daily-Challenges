##########################################
# freeCodeCamp 8/30/2025 daily challenge
# Solution by Joshua Millman, O(n - nlog(n))
# Given an array of numbers, return a sorted array of the dupes.
##########################################
def find_duplicates(arr):
    seenAlready = set()
    dupeArr = set()
    for item in arr:
        if item in seenAlready:
            dupeArr.add(item)
        else:
            seenAlready.add(item)
    return sorted(dupeArr)
test = find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4])
print(test)