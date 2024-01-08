width = int(input())
length = int(input())
cake_is_enough = True
total_pieces = width * length
current_pieces = total_pieces
command = input()
while command != "STOP":
    command = int(command )
    current_pieces -= command
    if current_pieces < 0:
        cake_is_enough = False
        break
    command = input()

if cake_is_enough:
    print(f"{current_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(current_pieces)} pieces more.")





