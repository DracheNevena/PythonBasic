days = int(input())
room = str(input())
rating = str(input())
price = 0

if room == "room for one person":
    nights = days - 1
    price = nights * 18
    if rating == "positive":
        total_price = price * 1.25
    else:
        total_price = price * 0.90
elif room == "apartment":
    nights = days - 1
    price = nights * 25
    if nights <= 9:
        price = price * 0.70
    elif 9 < nights <= 14:
        price = price * 0.65
    elif nights > 14:
        price = price * 0.50
    if rating == "positive":
        total_price = price * 1.25
    else:
        total_price = price * 0.90
elif room == "president apartment":
    nights = days - 1
    price = nights * 35
    if nights < 9:
        price = price * 0.90
    elif 9 < nights <= 14:
        price = price * 0.85
    else:
        price = price * 0.80
    if rating == "positive":
        total_price = price * 1.25
    else:
        total_price = price * 0.90
print(f"{total_price:.2f}")