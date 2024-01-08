target_steps = 10000
command = input()
total_steps = 0

while command != "Going home":
    current_steps = int(input())
    total_steps += current_steps
    command = input()
total_steps = total_steps + int(input())
difference = abs(target_steps - total_steps)
if total_steps >= target_steps:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")