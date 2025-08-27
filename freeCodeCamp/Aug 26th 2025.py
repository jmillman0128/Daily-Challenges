#########################################
# freeCodeCamp 8/26/2025 Daily Challenge
# Solution by Joshua Millman (O(n) - O(n**2))
# Given a string with properly nested parenthesis, reverse the string starting from the innermost parenthesis
#########################################
def decode(s):
    if '(' in s:
        firstPIndex = s.find('(')
        lastPIndex = 0
        level = 1
        i = firstPIndex + 1
        while level != 0:
            if s[i] == '(':
                level += 1
            if s[i] == ')':
                level -= 1
            i += 1
        lastPIndex = i
        return decode(s[:firstPIndex]) + decode(s[firstPIndex + 1: lastPIndex - 1])[::-1] + decode(s[lastPIndex:])
    return s
test = decode("f(Ce(re))o((e(aC)m)d)p")
print(test)