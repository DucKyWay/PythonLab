#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def main():
    data = input("Please enter context: ")
    split_text = data.split(" ")
    check = input("Please enter a number to search: ")
    if check in split_text:
        print(f"Found {check} at index {split_text.index(check)}")
    else:
        print("Not found")
main()