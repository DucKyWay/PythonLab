#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def to_u(txt_1, txt_2):
    txt_1_u = txt_1.upper()
    txt_2_u = txt_2.upper()
    return f"{txt_1_u} and {txt_2_u}"

def to_l(txt_1, txt_2):
    txt_1_l = txt_1.lower()
    txt_2_l = txt_2.lower()
    return f"{txt_1_l} and {txt_2_l}"

def swap(txt_1, txt_2):
    txt_1_s = txt_1.swapcase()
    txt_2_s = txt_2.swapcase()
    return f"{txt_1_s} and {txt_2_s}"

def reverse(txt_1, txt_2):
    txt_1_r = txt_1[::-1]
    txt_2_r = txt_2[::-1]
    return f"{txt_1_r} and {txt_2_r}"

def concatenate(txt_1, txt_2):
    txt = txt_1 + txt_2
    return f"is {txt}"

def main():
    txt_1 = input("Enter text 1: ")
    txt_2 = input("Enter text 2: ")

    print("=====\nAll lowercase:")
    print(to_l(txt_1, txt_2))
    print("=====\nAll uppercase:")
    print(to_u(txt_1, txt_2))
    print("=====\nSwap lower and upper case:")
    print(swap(txt_1, txt_2))
    print("=====\nReverse text:")
    print(reverse(txt_1, txt_2))
    print("=====\nText1 concatenate with Text2:")
    print(concatenate(txt_1, txt_2))
    print("=====")

main()