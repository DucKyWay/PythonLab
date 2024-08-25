'''
Problem From: https://elabsheet.org/elab/taskpads/show/234bqw6z1v/
Code by: _ducky_way_
'''
import math
i = 1
failed = 0
time = 0
worst, best = 0, math.inf
while i <= 5:
    sec = input()
    if sec == "DNF" or sec == "DNS":
        failed += 1
    else:
        sec = float(sec)
        if sec >= worst:
            worst = sec
        if sec <= best:
            best = sec
        time += sec
    i += 1

if failed >= 2:
    result = "Sorry, that's a DNF."
elif failed == 1:
    result = f"{(time - best)/3:.2f}"
else:
    result = f"{(time - worst - best)/3:.2f}"
print(result)
#print(worst, best)
