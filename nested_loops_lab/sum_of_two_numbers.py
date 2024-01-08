start_interval = int(input())
end_interval = int(input())
magik_number = int(input())
combination_counter = 0
combination_is_found = False

for number in range(start_interval, end_interval + 1):
    for number1 in range(start_interval, end_interval + 1):
        combination_counter += 1
        if number + number1 == magik_number:
            combination_is_found = True
            break
    if combination_is_found:
        break
if combination_is_found:
    print(f"Combination N:{combination_counter} ({number} + {number1} = {magik_number})")
else:
    print(f"{combination_counter} combinations - neither equals {magik_number}")


