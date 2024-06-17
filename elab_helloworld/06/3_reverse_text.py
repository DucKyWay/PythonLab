#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def main():
    txt = input("Enter text: ")
    txt_m = list(txt[::-1])
    txt_m.pop(0)
    print(txt, end="")
    for i in txt_m:
        print(i, end="")
    
main()