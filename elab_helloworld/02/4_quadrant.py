# Enter x: 5
# Enter y: 3
# point (5,3) is on quadrant I

#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def main():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))

    if x == 0 and y == 0:
        print(f"point (0,0) is an origin point")
    elif x == 0:
        print(f"point (0,{y}) is on y axis")
    elif y == 0:
        print(f"point ({x},0) is on x axis")
    elif x > 0 and y > 0:
        print(f"point ({x},{y}) is on quadrant I")
    elif x < 0 and y > 0:
        print(f"point ({x},{y}) is on quadrant II")
    elif x < 0 and y < 0:
        print(f"point ({x},{y}) is on quadrant III")
    elif x > 0 and y < 0:
        print(f"point ({x},{y}) is on quadrant IV")
      
main()