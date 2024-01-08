n1 = int(input())
n2 = int(input())
operator = input()
result = 0
num = 0

if operator == "+" :
    result = n1 + n2
    if result % 2 == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")
elif operator == "-":
    result = n1 - n2
    if result % 2 == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")
elif operator == "*":
    result = n1 * n2
    if result % 2 == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")

elif operator == "/" and n2 != 0:
    result = n1 / n2
    print(f"{n1} / {n2} = {result:.2f}")

elif operator == "%" and n2 != 0:
    result = n1 % n2
    print(f"{n1} % {n2} = {result}")
if n2 ==0 and (operator == "/" or operator == "%"):
    print(f"Cannot divide {n1} by zero")



