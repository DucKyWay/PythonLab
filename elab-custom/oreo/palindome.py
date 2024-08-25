'''
Problem From: https://elabsheet.org/elab/taskpads/show/xo0ws61b6m/
Code by: _ducky_way_
'''
x = int(input("Please input number: "))
old = x
re_x = 0

while x > 0:
    digit = x % 10
    re_x = re_x * 10 + digit
    x = x // 10

if old == re_x:
    print(True)
else:
    print(False)
