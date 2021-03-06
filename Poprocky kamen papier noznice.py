import random
round = int(input('Number of rounds to win: '))
opponent = ''
while opponent != 'h' and opponent != 'c':
    opponent = input('Second player, human or comuter(h/c): ')
    opponent.lower()
options = ['r', 'p', 's']
l1 = []
l2 = []
w1 = 0
w2 = 0
def game(player1, player2):
    if player1 == player2:
        result = 'draw'
    elif player1 == 'r':
        if player2 == 'p':
            result = 'player 2 wins'
        else:
            result = 'player 1 wins'
    elif player1 == 'p':
        if player2 == 's':
            result = 'player 2 wins'
        else:
            result = 'player 1 wins'
    elif player1 == 's':
        if player2 == 'r':
            result = 'player 2 wins'
        else:
            result = 'player 1 wins'
    return result
if opponent == 'h':
    while w1 != round and w2 != round:
        player1 = ''
        player2 = ''
        print('Player 1')
        while player1 not in options:
            player1 = input('Rock, paper, scissors?(r/p/s): ')
        print('Player 2')
        while player2 not in options:
            player2 = input('Rock, paper, scissors?(r/p/s): ')
        print(game(player1, player2))
        l1.append(player1)
        l2.append(player2)
        if game(player1, player2) == 'player 1 wins':
            w1 += 1
        elif game(player1, player2) == 'player 2 wins':
            w2 += 1
        else:
            pass
else:
    while w1 < round and w2 < round:
        player1 = ''
        player2 = ''
        print('Player 1')
        while player1 not in options:
            player1 = input('Rock, paper, scissors?(r/p/s): ')
        player2 = random.choice(options)
        print(game(player1, player2))
        l1.append(player1)
        l2.append(player2)
        if game(player1, player2) == 'player 1 wins':
            w1 += 1
        elif game(player1, player2) == 'player 2 wins':
            w2 += 1
        else:
            pass
print('Thank you for playing')
print('Player 1')
print('Wins: ' + str(w1))
print('Attempts: ' + ', '.join(l1))
print('Player 2')
print('Wins: ' + str(w2))
print('Attempts: ' + ', '.join(l2))
if w1 > w2:
    print('Player 1 wins it all')
else:
    print('Player 2 wins it all')