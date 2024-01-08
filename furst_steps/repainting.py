nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

price_nylon = (nylon + 2) * 1.50
price_paint = (paint * 1.1) * 14.50
price_thinner = thinner * 5

sum_materials = price_nylon + price_paint + price_thinner + 0.40
sum_workers = (sum_materials * 0.30) * hours

total_sum = sum_materials + sum_workers

print(total_sum)

