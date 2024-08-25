'''
Problem From: https://elabsheet.org/elab/taskpads/show/herko41h0s/
Code by: _ducky_way_
'''

left = int(input())
can = 0
if left == 0 or left == 1:
    mid = int(input())
    if left == 1 and mid == 1:
        print("Rule has been break")
    elif left == 0 or mid == 0:
        if left == 0 and mid == 0:
            can += 1
        
        while True:
            now = int(input())
            if now == -1:
                if left == 0 and mid == 0:
                    can += 1
                print(can)
                break
            elif now >= 2 or now <= -2:
                print("Invalid state")
                break
            else:
                if left == 0 and now == 0:
                    if mid == 0:
                        can += 1
                elif mid == 1 and now == 1:
                    print("Rule has been break")
                    break
                left = mid
                mid = now
        
else:
    print("Invalid state")
