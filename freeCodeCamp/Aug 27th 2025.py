################################
# freeCodeCamp daily challenge 8/27/2025
# Solution by Joshua Millman
# Given an array of integers and operators, repeat operators as needed to return a result ignorning operator conventions.
################################
def evaluate(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[(i-1) % len(operators)] == '+':
            result += numbers[i]
        if operators[(i-1) % len(operators)] == '-':
            result -= numbers[i]
        if operators[(i-1) % len(operators)] == '*':
            result *= numbers[i]
        if operators[(i-1) % len(operators)] == '/':
            result /= numbers[i]
        if operators[(i-1) % len(operators)] == '%':
            result %= numbers[i]
    return result