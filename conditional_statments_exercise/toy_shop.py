price_excursion = float (input())
puzzels_count = int(input())
dolls_count = int(input())
teddy_count =  int(input())
minions_count = int(input())
trucks_count = int(input())

total_sum = (puzzels_count * 2.60) + (dolls_count * 3) + (teddy_count * 4.10 ) + (minions_count * 8.20) + (trucks_count * 2)
total_count = puzzels_count + dolls_count + teddy_count + minions_count + trucks_count

if total_count >= 50:
    total_sum = total_sum * 0.75

total_sum = total_sum - (total_sum * 0.10)

diff = abs(price_excursion - total_sum)

if price_excursion <= total_sum:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")

