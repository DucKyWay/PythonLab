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
