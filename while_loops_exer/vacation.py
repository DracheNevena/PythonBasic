needed_money = float(input())
money_on_hand = float(input())
total_money = money_on_hand
spending_counter = 0
day_counter = 0
vacation = True

while total_money < needed_money:
    action = input()
    current_money = float(input())
    day_counter += 1
    if action == "spend":
        spending_counter += 1
        if spending_counter == 5:
            vacation = False
            break
        total_money -= current_money
        if total_money < 0:
            total_money = 0
    else: # action == "save":
        total_money += current_money
        spending_counter = 0
if vacation:
    print(f"You saved the money for {day_counter} days.")
else:
    print("You can't save the money.")
    print(f"{day_counter}")
