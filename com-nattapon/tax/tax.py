list = [0, 0, 0, 0]
list[0] = int(input())
list[1] = int(input())
list[2] = int(input())
list[3] = int(input())

tax = [0, 0, 0, 0]
i = 0

for i in range(4):
    if list[i] >= 0:
        if list[i] < 100000:
            tax[i] = 0
        elif list[i] >= 100000 and list[i] <= 500000:
            tax[i] = list[i] * (5/100)
        elif list[i] >= 500001 and list[i] <= 1000000:
            tax[i] = list[i] * (10/100)
        elif list[i] > 1000000:
            tax[i] = list[i] * (20/100)

total_tax = sum(tax)
print(f'{total_tax:.2f}')