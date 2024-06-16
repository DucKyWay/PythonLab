#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def check_type(num):
    if (num % 2) == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")

def main():
    inputNum = int(input("Enter number: "))
    check_type(inputNum)
main()