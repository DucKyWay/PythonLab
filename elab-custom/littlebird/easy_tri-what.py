'''
Problem From: https://elabsheet.org/elab/taskpads/show/ixqfzh38m0/ 
Code by: _ducky_way_
'''
layer, mode = int(input()), input()
if (mode == "lower" or mode == "upper") and 0 <= layer <= 26:
    i = layer
    s = 0
    while i >= 1:
        j = 1
        k = 1
        print(" "*s, end="")
        while j <= i:
            if mode == "upper":
                print(f"{chr(ord('A') + j - 1 + s)}", end="")
            if mode == "lower":
                print(f"{chr(ord('a') + j - 1 + s)}", end="")        
            j += 1
        while k < i:
            if mode == "upper":
                print(f"{chr(ord('A') + layer + k - 1)}", end="")
            if mode == "lower":
                print(f"{chr(ord('a') + layer + k - 1)}", end="")        
            k += 1
        print()
        i -= 1
        s += 1
else:
    print("Invalid case.")