# 6R 0Y 7G 5B 1R 4Y 2G
# 9G 8B 3Y 1G 0R 5Y 7R
# 4B 2R 9Y 6G 3B 8Y 0G
# 5G 7Y 2B 4R 3G 6R 1B
# 6R

# 1 ดูทั้งเลขและสี ว่าตรงกันหมดหรือไม่ เช่นถ้า Table คือ 8R แล้วเราก็มี 8R ด้วย ให้ลง 8R ไปเลย
# 2 ถ้าไม่เจอที่เลขและสี match กัน ให้ check เลขก่อน ว่ามีเลขตรงกันหรือไม่
# 3 ถ้ามีให้ลงได้ เช่น Table คือ 8R และกรณีที่เราไม่มี 8R แต่เรามี 8B กับ 8G ในมือ ให้เราลง 8G "ดูตามลำดับความสำคัญของสี" (R,G,B,Y)
# 4 ถ้าไม่เจอเลขที่ match กัน ให้ check สีต่อ โดยเรียงลำดับเลขจากน้อยไปมาก หมายถึง ถ้า Table เป็น 8R และเราไม่มี 8R หรือแม้กระทั่งเลข 8 เฉยๆ เราก็ต้องไปดูการ์ดเลขอื่นที่เป็นสีแดงแทนโดย "ลงการ์ดเลขน้อยที่สุด" ก่อน เช่นถ้า Table เป็น 8R และเราไม่มีทั้ง 8R หรือเลข 8 แต่เรามี 9R, 1R ให้ลง 1R เพราะเลขน้อยกว่า
# 5 ถ้าผู้เล่นคนใดคนหนึ่งลงไพ่ไม่ได้แล้ว ให้จบเกม และพิมพ์การ์ดปัจจุบันของ Table และการ์ดในมือที่เหลือทั้งหมดโดย ให้เรียงลำดับความสำคัญของไพ่ด้วย

#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

player_cards = [[], [], [], []]
sorted_cards = [[], [], [], []]
number_priority = {str(i): i for i in range(10)}
color_priority = {'R': 0, 'G': 1, 'B': 2, 'Y': 3} # --> r g b y
start_game, turn = "", ""

def sorted_card(card):
    num, color = card[0], card[1]
    return (color_priority[color], number_priority[num])

def card_check(current_card, cards):
    print(current_card, cards)

def start():
    for i in range(4):
        card = input()
        player_cards[i] = list(card.split(" "))
        sorted_cards[i] = sorted(player_cards[i], key=sorted_card)

def gameplay(start_game):
    turn = start_game
    while True:
        for i in range(4):
            # if card_check(sorted_cards[i]) == "both number and color":
            #     turn = card_check
            # elif card_check(sorted_cards[i]) == "both number":
            # elif card_check(sorted_cards[i]) == "color":
            card_check(turn, sorted_cards[i])
            print(f"Player {i+1} place turn card to match 6R in both number and color")
            print(f"Now the current card is {turn}...")
        break
    

def main():
    start()
    start_game = input()

    gameplay(start_game)

    print(f"start: {player_cards}")
    print(f"sort: {sorted_cards}")

main()