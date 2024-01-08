budget = float(input())
season = input()

destination = ""
place = ""
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        price = budget * 0.30
    else:
        place = "Hotel"
        price = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        price = budget * 0.40
    else:
        place = "Hotel"
        price = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    place = "Hotel"
    price = budget * 0.90
print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")