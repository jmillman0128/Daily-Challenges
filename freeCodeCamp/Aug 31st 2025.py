################################
# freeCodeCamp 8/31/2025 daily challenge
# Solution by Joshua Millman, ~O(1)
# Given one of the rgb as a string, return a hexcode with that as the dominant color
################################
import random as rand
def generate_hex(color):
    validColors = ["red", "green", "blue"]
    if color not in validColors:
        return "Invalid color"
    hexFormat = "0123456789ABCDEF"
    hexCap = rand.randint(0, 255) 
    hexMinor1 = rand.randint(0, hexCap - 1)
    hexMinor2 = rand.randint(0, hexCap - 1)
    hexCode = ["00", "00", "00"]
    hexCode[validColors.index(color)] = hexFormat[hexCap//16] + hexFormat[hexCap % 16]
    hexCode[validColors.index(color) - 1] = hexFormat[hexMinor1//16] + hexFormat[hexMinor1 % 16]
    hexCode[validColors.index(color) - 2] = hexFormat[hexMinor2//16] + hexFormat[hexMinor2 % 16]
    return "".join(hexCode)
test = generate_hex("blue") 
print(test)