city = input()
sales_volume = float(input())
commissions = -1.0

if city == 'Sofia':
    if 0 <= sales_volume <= 500:
        commissions = 0.05
    elif 500 < sales_volume <= 1000:
        commissions = 0.07
    elif 1000 < sales_volume <= 10000:
        commissions = 0.08
    elif sales_volume > 10000:
        commissions = 0.12
elif city == 'Varna':
    if 0 <= sales_volume <= 500:
        commissions = 0.045
    elif 500 < sales_volume <= 1000:
        commissions = 0.075
    elif 1000 < sales_volume <= 10000:
        commissions = 0.10
    elif sales_volume > 10000:
        commissions = 0.13
elif city == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        commissions = 0.055
    elif 500 < sales_volume <= 1000:
        commissions = 0.08
    elif 1000 < sales_volume <= 10000:
        commissions = 0.12
    elif sales_volume > 10000:
        commissions = 0.145
if commissions >= 0:
    print(f'{sales_volume * commissions:.2f}')
else:
    print("error")