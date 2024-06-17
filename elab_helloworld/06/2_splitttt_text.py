#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def main():
    txt = input("Enter text: ")
    t_list = list(txt)
    for i in range(len(txt)):
        for j in range(i+1):
            print(t_list[j], end="")
        print()
main()