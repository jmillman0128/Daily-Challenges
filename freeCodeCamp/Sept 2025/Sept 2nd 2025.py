############################################
# freeCodeCamp 9/2/2025 daily challenge
# Solution by Joshua Millman
# Given a CSS rgb(r, g, b) color string, return the hexadecimal equivalent
############################################
def rgb_to_hex(rgb):
    hexDecode = "0123456789abcdef"
    rgbBreaker = rgb.split(",")
    colorList = [int(rgbBreaker[0][4:]), int(rgbBreaker[1][1:]), int(rgbBreaker[2][1:-1])] # Indexes split string array based on standard format of input, splicing the numbers out of their respective substrings.
    i = 0
    for item in colorList:
        colorList[i] = hexDecode[item // 16] + hexDecode[item % 16]
        i += 1
    return "#" + "".join(colorList)

test = rgb_to_hex("rgb(79, 123, 201)")
print(test)