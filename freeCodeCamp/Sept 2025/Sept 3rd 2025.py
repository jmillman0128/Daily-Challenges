#############################################
# freeCodeCamp 9/3/2025 daily challenge
# Solution by Joshua Millman
# Given a sentence and a string of letters, check to see if it is a pangram.
#############################################
def is_pangram(sentence, letters):
    sentenceSet = set(sentence.lower())
    pangramStr = ""
    for item in sentenceSet:
        if item.isalpha():
            pangramStr += item
    return sorted(pangramStr) == sorted(letters)
test = is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz")
print(test)