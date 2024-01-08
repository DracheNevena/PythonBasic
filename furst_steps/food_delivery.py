chicken = int(input())
fish = int(input())
vegan = int(input())

price_chicken = chicken * 10.35
price_fish = fish * 12.40
price_vegan = vegan * 8.15

price_menus = price_chicken + price_fish + price_vegan
desert = price_menus * 0.20

total_price = price_menus + desert + 2.50

print(total_price)