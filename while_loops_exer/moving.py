width_of_free_space_m = int(input())
length_of_free_space_m = int(input())
height_of_free_space_m = int(input())
command = input()
no_free_space = False
volume_of_free_space_m = width_of_free_space_m  * length_of_free_space_m  * height_of_free_space_m

while command != "Done":
    number_of_cartons = int(command)
    volume_of_free_space_m -= number_of_cartons
    if volume_of_free_space_m < 0:
        no_free_space = True
        break
    command = input()
if no_free_space:
    print(f"No more free space! You need {abs(volume_of_free_space_m)} Cubic meters more.")
else:
    print(f"{volume_of_free_space_m} Cubic meters left.")

