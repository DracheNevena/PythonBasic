number = int(input())
combinations_counter = 0
for number1 in range(number + 1):
    for number2 in range(number + 1):
        for number3 in range(number + 1):
            if number1 + number2 + number3 == number:
                combinations_counter += 1
print(combinations_counter)
