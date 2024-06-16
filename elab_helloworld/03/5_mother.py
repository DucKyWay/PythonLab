#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def main():
    num = int(input())
    if num <= 0:
        print("Number must be more than 0")
    else:
        for i in range(12):
            print(f"{num} x {i+1} = {num * (i+1)}")

main()