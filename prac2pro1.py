
startvalue = 1500
endvalue = 2700


finalvalue = []
for number in range(startvalue, endvalue + 1):
    if number % 7 == 0 and number % 5 == 0:
        finalvalue.append(number)

print(finalvalue)
