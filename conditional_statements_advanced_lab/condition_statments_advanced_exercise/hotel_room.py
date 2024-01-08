month = str(input())
number_of_overnight_stays = int(input())
price_studio = 0
price_apartment= 0

if month == "May" or month == "October":
    price_studio = number_of_overnight_stays * 50
    price_apartment = number_of_overnight_stays * 65
    if 7 < number_of_overnight_stays <= 14:
        price_studio = price_studio * 0.95
    elif number_of_overnight_stays > 14:
        price_studio = price_studio * 0.70
        price_apartment = price_apartment - (price_apartment * 0.10)
elif month == "June" or month == "September":
    price_studio = number_of_overnight_stays * 75.20
    price_apartment = number_of_overnight_stays * 68.70
    if number_of_overnight_stays > 14:
        price_studio = price_studio * 0.80
        price_apartment = price_apartment - (price_apartment * 0.10)
elif month == "Juli" or month == "August":
    price_studio = number_of_overnight_stays * 76
    price_apartment = number_of_overnight_stays * 77
    if number_of_overnight_stays > 14:
        price_apartment = price_apartment - (price_apartment * 0.10)
print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")