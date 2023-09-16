import random
guess_range=20
answer=0
replay=1

print('''Welcome to The Guessing Game!
To play the game, simply guess a number from 1 to 20
and we'll tell you whether the guessed number is correct, or lower or higher than the correct answer.
Mind you, you'll only get 4 guesses!
Good luck~''')

while replay==1:
    answer=random.randint(1,guess_range)
    
    for i in range(4):
        
        
        if i==3:
            print("\nBe careful! this is your last guess...")
            last_guess=int(input("\nEnter a number: "))
            
            if last_guess==answer:
                print("\nCongrats, your guess is correct!")
            else:
                print("\nOh no! Your guess was wrong, the correct answer was",answer)
                
            replay=int(input("\nIf you wish to play once more, enter 1, if not, then enter 0: "))
            
            
        else:      
            guess=int(input("\nEnter a number: "))
            
            if guess==answer:
                print("\nCongrats, your guess is correct!")
                replay=int(input("\nIf you wish to play once more, enter 1, if not, then enter 0: "))
                break
            elif guess>answer:
                print("\nYour guess is too high, try again :(")
            elif guess<answer:
                print("\nYour guess is too low, try again :(")

print("\nThanks for playing!")