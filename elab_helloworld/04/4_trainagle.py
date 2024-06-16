a = int(input("Enter Side A: "))
b = int(input("Enter Side B: "))
c = int(input("Enter Side C: "))

def check_can_triangle(a, b, c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

if check_can_triangle(a, b, c):
    print("Valid")
else:
    print("Invalid")