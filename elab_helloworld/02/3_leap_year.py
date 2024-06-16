#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def main():
    year = int(input("Input year: "))
    if year >= 400:
        if year % 400 == 0 and year % 100 == 0:
            print(year, "is a leap year.")
        elif year % 4 == 0 and year % 100 != 0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print("Invalid year.")

main()