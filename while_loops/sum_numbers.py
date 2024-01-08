# number = int(input())
# sum_of_numbers = 0
#
# while sum_of_numbers < number:
#     current_number = int(input())
#     sum_of_numbers += current_number
#
# print(sum_of_numbers)


number = int(input())
sum_of_numbers = 0

while True:
    current_number = int(input())
    sum_of_numbers += current_number
    if sum_of_numbers >= number:
        break
print(sum_of_numbers)
