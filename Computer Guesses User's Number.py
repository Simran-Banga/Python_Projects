import random
print('''Welcome to The Number Guessing Game!
So to play this game, simply think of a number from 1 to 50
and let the computer make attempts to guess it.
Then you must tell the computer whether its guess is
too high(H), too low(L), or correct(C).
Have fun!''')

low=1
high=50
feedback=''
play=''

while feedback!="c" or play=='y':
    
    if low!=high:
        guess=random.randint(low, high)
    else:
        guess=low
        
    feedback=input(f"\nIs {guess} too low(L), too high(H), or correct(C)?: ").lower()
    
    if feedback=='h':
        high=guess-1
    elif feedback=='l':
        low=guess+1
    elif feedback=='c':
        play=input(f'''\nYay! The computer guessed your number {guess} correctly!
Do you wish to play again? (y/n): ''').lower()
        low=1
        high=50
    else:
        print("\nPlease try again and enter a valid choice.")
        
print('''\nThanks for playing!
Hope you enjoyed~''')
