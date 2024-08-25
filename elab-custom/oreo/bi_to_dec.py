num = int(input("Enter Binary digits: "))
i = 0
result = 0
while True:
    if num == 0:
        break
    result += (num % 10) * (2**i)
    num //= 10
    i += 1
print(result)