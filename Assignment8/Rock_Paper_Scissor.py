import random
options = ['Rock', 'Paper', 'Scissor']
scores = {'user': 0 , 'computer': 0}
for i in range (5):
    computer_choice = random.choice(options)
    user_choice = input ('play the game: ')
    user_choice = user_choice.capitalize()
    if user_choice == computer_choice:
        print('Equal')
    elif user_choice == 'Rock':
        if computer_choice == 'Scissor':
            print('user wins')
            scores['user'] += 1
        elif computer_choice == 'Paper':
            print('computer wins')
            scores['computer'] += 1
    elif user_choice == 'Scissor':
        if computer_choice == 'Rock':
            print('computer wins')
            scores['computer'] += 1
        elif computer_choice == 'Paper':
            print('user wins')
            scores['user'] += 1
    elif user_choice == 'Paper':
        if computer_choice == 'Rock':
            print('user wins')
            scores['user'] += 1
        elif computer_choice == 'Scissor':
            print('computer wins')
            scores['computer'] += 1
    else:
        print('Invalid input')

if scores['computer'] > scores['user']:
    print('computer is winner with sores ', scores['computer'])
else :
    print('user is winner with sores ', scores['user'])
