'''
Problem From: https://elabsheet.org/elab/taskpads/show/xtsvjymyag/
Code by: _ducky_way_
'''
def main():
    D = input()
    H, M = int(input()), int(input())
    S, T = float(input()), input()

    if D == "Sunday" or D == "Monday" or D == "Tuesday" or D == "Wednesday" or D == "Thursday" or D == "Friday" or D == "Saturday":
        if 0 <= H <= 24 and 0 <= M <= 60:

            if T == "No-meter":
                print("Let's go!")
            else:
                if D == "Friday":
                    if (H == 15 and M >= 30) or (H == 16 and M <= 30):
                        if S >= 10:
                            print("I need to return the car.")
                        else:
                            print("Let's go!")
                    elif (H == 16 and M >= 31) or (17 <= H <= 22) or (H == 23 and M <= 59):
                        print("I need to refuel.")
                else:
                    print("Let's go!")

        else:
            print("Invalid date!")
    else:
        print("Invalid date!")

main()
