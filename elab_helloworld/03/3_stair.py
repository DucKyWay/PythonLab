#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def main():
    layer = int(input())
    if layer >= 1:
        for i in range(layer):
            print("*"*(i+1))
    else:
        print("ERROR")

main()