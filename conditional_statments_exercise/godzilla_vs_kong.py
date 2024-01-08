budget = float(input())
count_statists = int(input())
cost_clothing_one = float(input())

decor_price = budget * 0.10
all_clothes_price = count_statists * cost_clothing_one

if count_statists > 150:
    all_clothes_price = all_clothes_price * 0.90

total_expenses = decor_price + all_clothes_price

diff = abs(total_expenses - budget)

if budget >= total_expenses:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")