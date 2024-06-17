#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def main():
    state = int(input("Enter Number: "))
    num_list = []
    if state > 0:
        for i in range(state):
            num_list.append(i+1)
        print(num_list)
    else:
        print("ERROR")

main()