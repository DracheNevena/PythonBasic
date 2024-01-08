age = int(input())
price_washing_machine = float(input())
price_one_toy = int(input())

brother_count = 0
count_toys = 0
total_sum = 0
money = 0
for i in range(1,age + 1):
    if i % 2 != 0:
        count_toys += 1
    else:
        brother_count += 1
        money += 10
        total_sum += money
result = (count_toys * price_one_toy) + total_sum - brother_count
diff = abs(result - price_washing_machine)
if result >= price_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No {diff:.2f}")
