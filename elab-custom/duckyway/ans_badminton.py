def print_status(team1_score, team2_score, team1_positions, team2_positions, server):
    print(f"{team1_score}-{team2_score} | {' '.join(team1_positions)} - {' '.join(team2_positions)} | {server}")

def badminton_game():
    team1_score = 0
    team2_score = 0
    team1_positions = ['P1', 'P2']
    team2_positions = ['P3', 'P4']
    server = 'P2'

    print_status(team1_score, team2_score, team1_positions, team2_positions, server)
    
    while True:
        scorer = input("scorer: ")
        
        if scorer == '0':
            print("terminate program")
            break
        
        if scorer == 'P1' or scorer == 'P2':
            team1_score += 1
            if team1_score == 21:
                print(f"team 1 wins")
                break
            if server == 'P1' or server == 'P2':
                team1_positions[0], team1_positions[1] = team1_positions[1], team1_positions[0]
            server = team1_positions[0] if team1_score % 2 == 1 else team1_positions[1]
        
        elif scorer == 'P3' or scorer == 'P4':
            team2_score += 1
            if team2_score == 21:
                print(f"team 2 wins")
                break
            if server == 'P3' or server == 'P4':
                team2_positions[0], team2_positions[1] = team2_positions[1], team2_positions[0]
            server = team2_positions[0] if team2_score % 2 == 1 else team2_positions[1]
        

        print_status(team1_score, team2_score, team1_positions, team2_positions, server)

badminton_game()
