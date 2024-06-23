#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

def default_output(size, map):
    print("-" * (size[1] * 2 + 1))
    for i in range(len(map)):
        print("|", end="")
        for j in range(len(map[i])):
            if j < len(map[i]) - 1:
                print(f"{map[i][j]} ", end="")
            else:
                print(f"{map[i][j]}", end="")
        print("|")
    print("-" * (size[1] * 2 + 1))
    
def main():
    size_input = input()
    size = size_input.split(" ")
    size = [int(i) for i in size]
    map = []
    
    for _ in range(int(size[0])):
        row = input()
        map.append(row.split(" "))

    default_output(size, map)

main()