pac_pens = int(input())
pac_marker= int(input())
liters_chalkboard_cleaner = int(input())
percent_discount = int(input())

price_pac_pens = pac_pens * 5.80
price_pac_marker = pac_marker * 7.20
price_liters_chalkboard_cleaner = liters_chalkboard_cleaner * 1.20
price_materials = price_pac_pens + price_pac_marker + price_liters_chalkboard_cleaner

discount = price_materials * (percent_discount / 100)
total_price = price_materials - discount

print(total_price)

