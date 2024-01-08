destination = input()

while destination != "End":
    minimal_budget = float(input())
    current_budget = 0
    while current_budget < minimal_budget:
        current_sum = float(input())
        current_budget += current_sum
    print(f"Going to {destination}!")
    destination = input()
