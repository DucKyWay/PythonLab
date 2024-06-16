Station = int(input()) #Station
money = int(input()) #money
moneyCoin = 0
fare = [27, 35, 42]

def CountCoin(money):
    moneyCoin = money/10
    print(int(moneyCoin))
    money %= 10

    moneyCoin = money/5
    print(int(moneyCoin))
    money %= 5
        
    moneyCoin = money/2
    print(int(moneyCoin))
    money %= 2
        
    moneyCoin = money/1
    print(int(moneyCoin))
    money %= 1

if Station == 1:
    change = money - fare[0]
    if change >= 0:
        CountCoin(change)
    elif change < 0:
        print("จำนวนเงินไม่เพียงพอ")
if Station == 2:
    change = money - fare[1]
    if change >= 0:
        CountCoin(change)
    elif change < 0:
        print("จำนวนเงินไม่เพียงพอ")
if Station == 3:
    change = money - fare[2]
    if change >= 0:
        CountCoin(change)
    elif change < 0:
        print("จำนวนเงินไม่เพียงพอ")