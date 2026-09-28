"""Cho-Han, by Al Sweigart al@inventwithpython.com

The traditional Japanese dice game of even-odd.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game

Assignment 3 changes by Dustin Andersen: prompt initials, house fee, and bonus.
"""

import random
import sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
If the two dice total 2 or 7, you receive a 10 mon bonus.
''')

purse = 5000
while True:  # Main game loop.
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('da: ')  # DA: use my initials for the wager prompt.
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    while True:
        bet = input('da: ').upper()  # DA: use my initials for the guess prompt.
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    total = dice1 + dice2  # DA: keep the total for parity and the bonus rule.
    rollIsEven = total % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot
        house_fee = pot * 12 // 100  # DA: house takes 12%, rounded down to whole mon.
        print('The house collects a', house_fee, 'mon fee.')
        purse = purse - house_fee
    else:
        purse = purse - pot
        print('You lost!')

    # DA: award the bonus after the wager result, whether the guess won or lost.
    if total == 2 or total == 7:
        print('The dice total', total, '- you got a 10 mon bonus!')
        purse = purse + 10

    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
