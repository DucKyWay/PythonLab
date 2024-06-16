money = [0, 0]
money_1 = int(input())
money_2 = int(input())
money[0] = money_1
money[1] = money_2

sum_money = [0, 0]

for i in range(2):
    if money_1 <= 20000 and money_2 <= 20000:
        if money[i] % 100 == 0:
            moneyCash = sum_money[i] / 1000
            moneyOver = moneyCash-20
            if moneyOver > 0:
                moneyCash -= moneyOver
            print(int(moneyCash))
            sum_money[i] %= 1000
            if moneyOver > 0:
                money_sum = sum_money[i] + (moneyOver * 1000)

            moneyCash = sum_money[i] / 500
            moneyOver = moneyCash - 20
            if moneyOver > 0:
                moneyCash -= moneyOver
            print(int(moneyCash))
            sum_money[i] %= 500
            if moneyOver > 0:
                sum_money_1 = sum_money[i] + (moneyOver * 500)

            moneyCash = sum_money[i] / 100
            moneyOver = moneyCash - 20
            if moneyOver > 0:
                moneyCash -= moneyOver
            print(int(moneyCash))
            sum_money[i] %= 100
            if moneyOver > 0:
                sum_money[i] = sum_money[i] + (moneyOver * 100)
            else:
                print("Input Error")
        else:
            print("Input Error")
    else:
        print("Input Error")