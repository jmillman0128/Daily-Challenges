############################################
# freeCodeCamp 9/1/2025 daily challenge
# Solution by Joshua Millman
# Given an array of 3 numbers, compute the tribonacci sequence up to a given depth.
############################################
def tribonacci_sequence(start_sequence, length):
    triSeq = start_sequence
    if length < 3:
        return triSeq[:length]
    for i in range(3, length):
        triSeq.append(triSeq[i-3] + triSeq[i-2] + triSeq[i-1])
    return triSeq
test = tribonacci_sequence([123, 456, 789], 8)
print(test)