##############################################
# freeCodeCamp 8/29/2025 daily challenge
# Solution by Joshua Millman
# Given a number of candles and the number of used candles needed to make a new candle, return the maximal amount of candles you burn.
##############################################
def burn_candles(candles, leftovers_needed):
    newCandles = candles//leftovers_needed
    leftoverStock = candles % leftovers_needed
    totalCandles = candles + newCandles
    while newCandles > 0:
        leftoverStock += newCandles
        newCandles = 0
        leftoverStock += newCandles
        if leftoverStock >= leftovers_needed:
            newCandles = leftoverStock//leftovers_needed
            leftoverStock = leftoverStock % leftovers_needed
            totalCandles += newCandles

    return totalCandles
test = burn_candles(2345, 3)
print(test)