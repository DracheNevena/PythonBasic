month = str(input())
nights = int(input())

apartment = 0
studio = 0

if month == "May" or month == "October":
    apartment = 65
    studio = 50
    if 14 > nights > 7:
        studio *= 0.95
    elif nights > 14:
        studio *= 0.70
        apartment *= 0.90
elif month == "June" or month == "September":
    apartment = 68.70
    studio = 75.20
    if nights > 14:
        studio *= 0.80
        apartment *= 0.90
elif month == "July" or month == "August":
    apartment = 77
    studio = 76
    if nights > 14:
        apartment *= 0.90

total_apartment = apartment * nights
total_studio = studio * nights
print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")