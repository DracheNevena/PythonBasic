hour = int(input())
day = input()

if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' , 'Saturday'] and hour in range(10, 19):
    print("open")
else:
    day == "Sunday"
    print("closed")
