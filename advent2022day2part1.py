rock = 1
paper = 2
scissors = 3
draw = 3
win = 6

opponent_strings = {'A', 'B', 'C'}
player_strings = {'X', 'Y', 'Z'}

score = 0

def rps(opponent, player):
    if opponent == 'A':
        opponent = rock
    elif opponent == 'B':
        opponent = paper
    else: 
        opponent = scissors

    if player == 'X':
        player = rock
    elif player == 'Y':
        player = paper
    else: 
        player = scissors

    if player == opponent:
        player += draw
    elif player == 1 and opponent == 3:
        player += win
    elif player == 3 and opponent == 1:
        player += 0
    elif player > opponent:
        player += win

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
    