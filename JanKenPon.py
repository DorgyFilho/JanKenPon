from random import randint

def JanKenPon():
    optList = ['Rock', 'Paper', 'Scissors']
    CPU = optList[randint(0,2)]
    player = input('Rock, Paper or Scissors?: ')
    if player == CPU:
        print('Tie!')
    elif player == 'Rock' and CPU == 'Scissors':
        print('You Win! {} smashes {}'.format(player, CPU))
    elif player == 'Paper' and CPU == 'Rock':
        print('You Win! Paper surrounds Rock'.format(player, CPU))
    elif player == 'Scissors' and CPU == 'Paper':
        print('You Win! {} cuts {}'.format(player, CPU))
    elif player == 'Scissors' and CPU == 'Rock':
        print('You Lose! {} smashes {}'.format(CPU, player))
    elif player == 'Rock' and CPU == 'Paper':
        print('You Lose! {} surrounds {}'.format(CPU, player))
    elif player == 'Paper' and CPU == 'Scissors':
        print('You Lose! {} cuts {}'.format(CPU, player))
    else:
        print('Invalid Option!')

def main():
    again = 'Y'
    while again == 'Y':
        print('Welcome to the Jankenpon Game!')
        print('Choose Your Destiny')
        print('S-Start\nQ-Quit')
        op = input('Answer: ').upper()
        if op == 'S':
            JanKenPon()
        elif op == 'Q':
            print('Shutdown!')
            exit()
        else:
            print('Invalid Answer!')
            break
        print('Do You Want to Try Again? Y or N')
        again = input('Answer Here: ').upper()
        if again == 'N':
            print('Shutdown!')
            break
    else:
        print('Invalid Option!')

main()

