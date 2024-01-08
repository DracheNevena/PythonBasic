import left_and_right_sum

number_of_lines = int(input())
max_num = -left_and_right_sum.maxsize
min_num = left_and_right_sum.maxsize

for num in range(number_of_lines):
    current_number = int(input())
    if current_number > max_num:
        max_num = current_number
    if current_number < min_num:
        min_num = current_number
print(f'Max number: {max_num}')
print(f'Min number: {min_num}')