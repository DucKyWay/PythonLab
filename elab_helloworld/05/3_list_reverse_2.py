#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def main():
    element = int(input("How many elements?: "))
    list_element = []
    for i in range(element):
        num = int(input("Enter Value: "))
        list_element.append(num)
    list_element.sort()
    list_element.reverse()
    for i in list_element:
        print(i, end=' ')

main()