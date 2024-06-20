#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def main():
    txt = input("Please input string: ")
    alphabet = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 
                'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    vowel = ["a", "e", "i", "o", "u", 
            "A", "E", "I", "O", "U"]
    split_txt = list(txt)
    chk_alp, chk_num, chk_vol = [], [], []

    for i in split_txt:
        if i in alphabet:
            chk_alp.append(i)
        elif i in number:
            chk_num.append(i)
        elif i in vowel:
            chk_vol.append(i)

    if chk_vol != []:
        print("Vowel(s):")
        for i in range(len(chk_vol)):
            if i != len(chk_vol)-1:
                print(chk_vol[i], end=" ")
            else:
                print(chk_vol[i])
                
    if chk_alp != []:
        print("Alphabet(s):")
        for i in range(len(chk_alp)):
            if i != len(chk_alp)-1:
                print(chk_alp[i], end=" ")
            else:
                print(chk_alp[i])

    if chk_num != []:
        print("Number(s):")
        for i in range(len(chk_num)):
            if i != len(chk_num)-1:
                print(chk_num[i], end=" ")
            else:
                print(chk_num[i])

main()