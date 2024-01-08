number_of_lines = int(input())
left_sum = 0
right_sum = 0

for i in range(1, number_of_lines + 1):
    left_sum += int(input())
for p in range(2,number_of_lines + 2):
    right_sum += int(input())
if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(left_sum-right_sum)
    print(f'No, diff = {diff}')