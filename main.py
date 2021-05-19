# Andrew McFadyen
# Roman Numeral Converter

# This function converts roman numerals into numbers.
# Accounts for caps/no caps
def numberify(x):
    if x == "I" or x == "i":
        x = 1
        return(x)
    if x == "V" or x == "v":
        x = 5
        return(x)
    if x == "X" or x == "x":
        x = 10
        return(x)
    if x == "L" or x == "l":
        x = 50
        return(x)
    if x == "C" or x == "c":
        x = 100
        return(x)
    if x == "D" or x == "d":
        x = 500
        return(x)
    if x == "M" or x == "m":
        x = 1000
        return(x)

# Declare empty arrays for later use
characterlist = []
numberslist = []

# Prompt user for Roman Numeral, create an array and turn that array into numbers.
input = input("Enter a Roman Numeral: ")
for i in input:
    characterlist.append(i)
for x in characterlist:
    numberslist.append(numberify(x))

# Declare iterator at 0
i = 0

# Handles numbers like 4, 9, etc where the 1 precedes the larger number
while i < len(numberslist) - 1:
    if numberslist[i] == 1 and numberslist[i + 1] > numberslist[i]:
        numberslist[i] = int(numberslist[i]) * -1
        i += 1
    else:
        i += 1

# Return iterator to 0
i = 0
# Final converted value saved as sum of constituent parts
sum = 0

# Sums final result
while i < len(numberslist):
    sum += numberslist[i]
    i += 1

print(sum)