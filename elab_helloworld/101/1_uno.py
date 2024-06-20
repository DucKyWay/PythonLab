#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#
# https://elab.punsnx.com/elab/lab/1/22/

player_cards = [[], [], [], []]
sorted_cards = [[], [], [], []]
number_priority = {str(i): i for i in range(10)}
color_priority = {'R': 0, 'G': 1, 'B': 2, 'Y': 3} # --> red green blue yellow

def sorted_card(card):
    num, color = card[0], card[1]
    return (color_priority[color], number_priority[num])

def start():
    for i in range(4):
        card = input()
        player_cards[i] = list(card.split(" "))
        sorted_cards[i] = sorted(player_cards[i], key=sorted_card)
    start_game = input()

def main():
    print(start())

    print(player_cards)
    print(sorted_cards)

main()