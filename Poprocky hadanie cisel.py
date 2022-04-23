import random
players = []
num_players = 0
while num_players <= 0 or num_players >= 6:
    num_players = int(input('Number of players: '))
for i in range(num_players):
    name = input('Name: ')
    human = ''
    while human != 'y' and human != 'n':
        human = input('Are you a human? y/n: ')
        human.lower()
    order = i + 1
    dictionary = {'name': name,
         'human': human,
         'order': order,
         'list': [],
        'guess': 0}
    players.append(dictionary)

range_num1 = int(input('Enter the 1st number for guessing: '))
range_num2 = int(input('Enter the 2nd number for guessing: '))
if range_num1 < range_num2:
    r1 = range_num1
    r2 = range_num2
    attempts = int(range_num2 / 2)
    guess = r2 + 1
else:
    r1 = range_num2
    r2 = range_num1
    attempts = int(range_num1 / 2)
    guess = r1 + 1
guessing_num = random.randint(r1, r2)
attempt = int(attempts / num_players)
print('Guessing number: {}'.format(guessing_num))
result = ''
x = True
while x:
    for i in players:
        if result == '':
            if attempt != 0:
                if i['human'] == 'y':
                    print('Player {} ({}) attempts left: {}'.format(i['order'], i['name'], attempt))
                    guess = int(input('Player {} ({}) enter number: '.format(i['order'], i['name'])))
                    i['list'].append(guess)
                    i['guess'] += 1
                    if guess == guessing_num:
                        result = 'Player {} ({}) has won'.format(i['order'], i['name'])
                        x = False
                    elif guess != guessing_num:
                        if guess < guessing_num:
                            print('Your guess was lower than the number')
                            r1 = guess
                        else:
                            print('Your guess was higher than the number')
                            r2 = guess
                    print('Attempts left: {}\n'
                          'You have guessed {}x\n'
                          'You have guussed: {}'.format(attempt - 1, i['guess'], i['list']))
                else:
                    print('Player {} ({}) attempts left: {}'.format(i['order'], i['name'], attempt))
                    guess = random.randint(r1, r2)
                    i['list'].append(guess)
                    i['guess'] += 1
                    print('Player {} ({}): {}'.format(i['order'], i['name'], guess))
                    if guess == guessing_num:
                        result = 'Player {} ({}) has won'.format(i['order'], i['name'])
                        x = False
                    elif guess != guessing_num:
                        if guess < guessing_num:
                            print('Your guess was lower than the number')
                            r1 = guess
                        else:
                            print('Your guess was higher than the number')
                            r2 = guess
                        print('Attempts left: {}\n'
                              'You have guessed {}x\n'
                              'You have guessed: {}'.format(attempt - 1, i['guess'], i['list']))

            else:
                if result == '':
                    result = 'All attempts were used, no one won'
                x = False
        else:
            x = False
    attempt -= 1
    if attempt == 0:
        x = False
        result = 'You do not have any more attempts'
print('Correct answer: {}'.format(guessing_num))
for i in players:
    print('Player {} ({}): {}'.format(i['order'], i['name'], i['list']))
print('Result: {}'.format(result))