import random

def play():
    user = input("What's your choices? r for rock, p for paper, s for scissors \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost.'

def is_win(user, computer):
    # return true if user wins
    # r > s, s > p, p > r

    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') \
        or (user == 's' and computer == 'p'):
        return True

c = ''
while c != 'q':
    print(play())
    c = input("\ninput 'q' to quit, other to continue:\n")
