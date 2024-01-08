kind_of_flowers = input()
quantity = int(input())
budget = int(input())
price = 0

if kind_of_flowers == "Roses":
    price = quantity * 5
    if quantity > 80:
        price = price * 0.90
elif kind_of_flowers == "Dahlias":
    price = quantity * 3.80
    if quantity > 90:
        price = price * 0.85
elif kind_of_flowers == "Tulips":
    price = quantity * 2.80
    if quantity > 80:
        price = price * 0.85
elif kind_of_flowers == "Narcissus":
    price = quantity * 3
    if quantity < 120:
        price = price * 1.15
elif kind_of_flowers == "Gladiolus":
    price = quantity * 2.50
    if quantity < 80:
        price = price * 1.20
diff = abs(budget - price)
if budget >= price:
    print(f"Hey, you have a great garden with {quantity} {kind_of_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
