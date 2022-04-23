import random
words = open("word_list.txt", "a")
words.write('\n')
words = open("word_list.txt", "r")
l_words = words.readlines()
words.close()
new_items = [x[:-1] for x in l_words]
wrong_guesses = 5
guesses_wrong = 0
print('You can get {} guesses wrong'.format(wrong_guesses))
word_guess = random.choice(new_items)
# print(word_guess)
word_len = []
for i in range(0, len(word_guess)):
    word_len.append("_")
print(' '.join(word_len))
wrong_l = []
two_let = list(word_guess)
guess = ''
while wrong_guesses > 0 and "_" in word_len:
    guess = input('Your guess: ')
    if guess == word_guess:
        temp_list = list(word_guess)
        word_len = temp_list
        print(' '.join(word_len))
    elif guess in word_guess:
        if guess not in two_let:
            wrong_guesses -= 1
            guesses_wrong += 1
            print('You have already guessed this')
            if guess not in wrong_l and guess not in word_guess:
                wrong_l.append(guess)
        while guess in two_let:
            x = two_let.index(guess)
            word_len[x] = guess
            two_let[x] = '_'
        else:
            pass
        print(' '.join(word_len))
    else:
        wrong_guesses -= 1
        guesses_wrong += 1
        if guess not in wrong_l:
            wrong_l.append(guess)
        else:
            print('You have already guessed this')
    print('Number of wrong guesses remaining: {}'.format(wrong_guesses))
    print('Number of wrong guesses: {}'.format(guesses_wrong))
    print('Wrong guesses: {}'.format(', '.join(wrong_l)))
if wrong_guesses == 0:
    print('You lost')
else:
    print('You won')
print('Number of wrong guesses: {}'.format(guesses_wrong))
fd=open("word_list.txt","r")
d=fd.read()
fd.close()
m=d.split("\n")
s="\n".join(m[:-1])
fd=open("word_list.txt","w+")
for i in range(len(s)):
    fd.write(s[i])
fd.close()