#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def main():
    num = []
    while True:
        number = float(input())
        if number >= 0:
            num.append(number)
        else:
            break
    
    total_sum = 0
    if not num:
        total_sum = 0
        print(f"Average = 0.00")
    else:
        for i in range(len(num)):
            total_sum += num[i]
        print(f"Average = {total_sum/len(num):.2f}")

    

main()
