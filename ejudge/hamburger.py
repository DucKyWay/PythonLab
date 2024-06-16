def main():
    left_value = int(input())
    right_value = int(input())

    left_hamburger = "|"*left_value
    right_hamburger = "|"*right_value

    meat = "*"*(left_value*2 + right_value*2)
    print(left_hamburger + meat + right_hamburger)

main()