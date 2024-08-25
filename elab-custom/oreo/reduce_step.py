'''
Problem From: https://elabsheet.org/elab/taskpads/show/deppb18i9s/
Code by: _ducky_way_
'''
def main():
    x = int(input("Please input number: "))
    print(x)
    i = 0
    if x > 0:
        while True:
            if x == 0:
                break
            if x % 2 == 0:
                x /= 2
                print(int(x))
            elif x % 2 != 0:
                x -= 1
                print(int(x))
            i += 1
        print(i, "step", end ="")
        if i >= 2: print("s") 
main()