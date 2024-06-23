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

color_priority = {'R': 0, 'G': 1, 'B': 2, 'Y': 3}
number_priority = {str(i): i for i in range(10)}

def sorted_card(card):
    num, color = card[0], card[1]
    return (color_priority[color], number_priority[num])

def start():
    player_cards = []
    for i in range(4):
        card = input()
        player_cards.append(sorted(card.split(" "), key=sorted_card))
    start_game = input()
    return player_cards, start_game

def gameplay(player_cards, start_game):
    turn = start_game
    player_index = 0
    
    while True:
        turn_played = False
        current_player_cards = player_cards[player_index]
        
        for i in range(len(current_player_cards)):
            s_card_get = current_player_cards[i]
            if s_card_get == turn:
                print(f"Player {player_index+1} place {s_card_get} card to match {turn} in both number and color")
                turn = s_card_get
                current_player_cards.pop(i)
                turn_played = True
                break

        if not turn_played:
            same_number_cards = [card for card in current_player_cards if card[0] == turn[0]]
            if same_number_cards:
                same_number_cards.sort(key=lambda x: color_priority[x[1]])
                s_card_get = same_number_cards[0]
                print(f"Player {player_index+1} place {s_card_get} card to match {turn} in number")
                turn = s_card_get
                current_player_cards.remove(s_card_get)
                turn_played = True
        
        if not turn_played:
            same_color_cards = [card for card in current_player_cards if card[1] == turn[1]]
            if same_color_cards:
                same_color_cards.sort(key=lambda x: number_priority[x[0]])
                s_card_get = same_color_cards[0]
                print(f"Player {player_index+1} place {s_card_get} card to match {turn} in color")
                turn = s_card_get
                current_player_cards.remove(s_card_get)
                turn_played = True
        
        if turn_played:
            print(f"Now the current card is {turn}...")
        else:
            print(f"Player {player_index+1} does not have a card to place")
            break
        
        player_index = (player_index + 1) % 4
    
    return turn

def main():
    player_cards, start_game = start()
    current_card = gameplay(player_cards, start_game)
    
    print("------------------")
    print(f"Current Card: {current_card}")
    print("Table hands:")
    for i in range(4):
        remaining_cards = sorted(player_cards[i], key=sorted_card)
        remaining_cards_str = " ".join(remaining_cards)
        print(f"Player {i+1}: {remaining_cards_str}")
    print("------------------")
main()
