# Enter field width: 10 
# Enter field length: 20 
# Enter price per square meter: 75.50
# Cleaning this 10 x 20 field cost 15100.00 THB

#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def main():
    w = input("Enter field width: ")
    l = input("Enter field length: ")
    ppm = float(input("Enter price per square meter: "))

    w_float = float(w)
    l_float = float(l)

    # w_str = f"{w_float:.0f}" if w_float.is_integer() else f"{w_float:.2f}"
    # l_str = f"{l_float:.0f}" if l_float.is_integer() else f"{l_float:.2f}"
    area = w_float * l_float

    print(f"Cleaning this {w_float} x {l_float} field cost {(area * ppm):.2f} THB")

main()
