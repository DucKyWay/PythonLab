#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def main():
    element = int(input("How many elements?: "))
    list_e = []
    if element > 0:
        for i in range(element):
            num = int(input("Enter Value: "))
            list_e.append(num)
        list_e.sort()
        for i in range(element):
            print(list_e[element-(i+1)], end=' ')

main()