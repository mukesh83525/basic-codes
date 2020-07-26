import random
list =['s','p','sc']
chances = 10
no_of_chances = 0
human_points = 0
computer_points = 0
print('\t\t\t\t\t\t\t\t\t\t The game start now place the input')
print('s for stone ,p for paper,sc for scissor')
print('you have 10 chance')
while no_of_chances < chances :
    k = input('choose the input now as "s","p","sc"')
    ran = random.choice(list)
    if k == ran :
        print(f"your input is {k} and computer input is {ran}")
        print('match is tie')
        #if we choose s
    elif k == 's' and ran == 'sc':
      human_points = human_points +1
      print(f"the input of user is {k } the input of computer is {ran }")
      print("You win this  round ")
      print(f"your points is {human_points} and computer points is {computer_points} ")
    elif k =='s' and ran =='p':
        computer_points = computer_points +1
        print(f"the input of user is {k} and input of computer is {ran}")
        print('computer won this round')
        print(f"your points are {human_points} and compputer points is {computer_points} ")
    #if we choose p
    elif k =='p' and ran =='s':
        human_points = human_points +1
        print(f"the input of user is {k} and input of computer is {ran}")
        print('You wonn this round ')
        print(f"your points are {human_points} and computer points are {computer_points} ")
    elif k =='p' and ran =='sc':
        computer_points = computer_points +1
        print(f"the input of user is {k} and input of computer is {ran}")
        print('computer wonn this round ')
        print(f"your points are {human_points} and computer points are {computer_points}")
    #if we choose sc
    elif k =='sc' and ran =='s':
        computer_points = computer_points +1
        print(f"the input of user is {k} and input of computer is {ran}")
        print('computer wonn this round ')
        print(f"your points are {human_points} and computer points are {computer_points}")
    elif k =='sc' and ran =='p':
        human_points = human_points +1
        print(f"the input of user is {k} and input of computer is {ran}")
        print('You wonn this round ')
        print(f"your points are {human_points} and computer points are {computer_points}")
    else:
        print('this is the wrong input')
    no_of_chances  = no_of_chances +1
    print(f"{chances - no_of_chances}out of {chances} chances left for you")
if computer_points > human_points:
    print('computer won the game')
if human_points>computer_points:
    print('You won the game')
print(f"Your points are {human_points}and computer poinnts are{computer_points}")