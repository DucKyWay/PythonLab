data = []

element = int(input("How many elements?: "))
if element > 0:
    for i in range(element):
        num = int(input("Enter Value: "))
        data.append(num)
    print(f"The list is:\n{data}")
    data.sort()
    print(f"Minimum value of this list is {data[0]}")
    print(f"Maximum value of this list is {data[element-1]}")