length = int (input())
width = int (input())
height= int (input())
percent = float (input())

volume = length * width * height / 1000
acc_lt = volume * (percent / 100)
result = volume- acc_lt

print(result)







