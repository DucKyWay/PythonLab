#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def main():
    data = input("Please enter context: ")
    split_text = data.split(" ")
    size = len(split_text)
    for i in range(size):
        print(f"Data member #{i} = {split_text[i]}")

main()