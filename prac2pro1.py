
startvalue = 1500
endvalue = 2700


result_numbers = []
for number in range(startvalue, endvalue + 1):
    if number % 7 == 0 and number % 5 == 0:
        result_numbers.append(number)

print("Numbers divisible by 7 and multiples of 5 between", startvalue, "and", endvalue, "are:")
print(result_numbers)
