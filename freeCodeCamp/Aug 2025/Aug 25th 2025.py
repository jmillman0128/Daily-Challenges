#################################
# freeCodeCamp challenge 8/25/2025
# solution by Joshua Millman, O(n)
# Task: Convert a string to camel case, remove spaces, dashes, underscores
#################################
def to_camel_case(s):
    camelStr = ""
    spaces = " -_"
    workArray = list(s)
    isWord = True
    for item in workArray:
        if item in spaces:
            isWord = False
        elif item not in spaces and isWord == False and camelStr != "":
            isWord = True
            camelStr = camelStr + item.upper()
        elif item not in spaces:
            camelStr = camelStr + item.lower()
    return camelStr