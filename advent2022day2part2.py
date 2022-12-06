rock = 1
paper = 2
scissors = 3
draw = 3
win = 6

opponent_strings = {'A', 'B', 'C'}
player_strings = {'X', 'Y', 'Z'}        # X: Lose, Y: Draw, Z: Win

score = 0

def rps(opponent, player):
    if opponent == 'A':
        opponent = rock
    elif opponent == 'B':
        opponent = paper
    else: 
        opponent = scissors

    if player == 'X':
        if opponent == 1:
            player = 3
        elif opponent == 2:
            player = 1
        else:
            player = 2
    elif player == 'Y':
        player = opponent + 3
    else: 
        if opponent == 1:
            player = 2
        elif opponent == 2:
            player = 3
        else:
            player = 1
        player += 6

    return player

with open('rpsList.txt') as rpsList:
    s = rpsList.read()
    s = s.splitlines()

    for i in s:
        o = ''
        p = ''

        for j in i:
            if not j.isspace():
                if j in opponent_strings:
                    o = j
                elif j in player_strings:
                    p = j

        score += rps(o, p)

    print(score)    
    