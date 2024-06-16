time = int(input("Enter time: "))
balance = time
day_left, hour_left, min_left, sec_left= 0, 0, 0, 0

if balance >= 84000: #day
    day_left = balance // 84000
    balance //= day_left
else:
    dayleft = 0

if balance >= 3600: #hour
    hour_left = balance // 3600
    balance //= hour_left
else:
    hour_left = 0

if balance >= 60: #min
    min_left = balance // 60
    balance //= min_left
else:
    min_left = 0

if balance < 60: #sec
    if balance != 0:
        sec_left = balance
    if balance == 0:
        sec_left = 0 
else:
    sec_left = 0

print(int(day_left))
print(int(hour_left))
print(int(min_left))
print(int(sec_left))