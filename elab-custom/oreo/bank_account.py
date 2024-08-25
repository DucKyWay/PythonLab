'''
Problem From: https://elabsheet.org/elab/taskpads/show/vu7hq0ty1o/
Code by: _ducky_way_
'''
amount, command = float(input("Enter amount: ")), input("Enter command (w for withdraw, d for deposit, e for exit): ")
if amount >= 0:
    while True:
        
        if command == 'w':
            w_amount = float(input("Enter withdraw amount: "))
            if w_amount > 0:
                if w_amount > amount:
                    print("You cannot withdraw more than the amount in your account!")
                else: 
                    amount -= w_amount
                    print(f"Current balance = {amount:.2f}$")
                    command = input("Enter command (w for withdraw, d for deposit, e for exit): ")
            else:
                print("Incorrect transactions!")

        elif command == 'd':
            d_amount = float(input("Enter deposit amount: "))
            if d_amount > 0:
                amount += d_amount
                print(f"Current balance = {amount:.2f}$")
                command = input("Enter command (w for withdraw, d for deposit, e for exit): ")
            else:
                print("Incorrect transactions!")

        elif command == 'e':
            break
        else:
            print('Invalid Command!')
            command = input("Enter command (w for withdraw, d for deposit, e for exit): ")