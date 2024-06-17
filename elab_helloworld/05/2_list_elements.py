#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def main():
    state = int(input("Enter Number: "))
    num_list = []
    if state > 0:
        for i in range(state):
            num_list.append(i+1)
        for i in range(state):
            print(num_list[i], end=' ')
    else:
        print("ERROR")

main()