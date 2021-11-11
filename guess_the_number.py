import random

logo = """ 
.d88b                          88888 8           w     8b  8                 8               
8P www 8   8 .d88b d88b d88b     8   8d8b. .d88 w8ww   8Ybm8 8   8 8d8b.d8b. 88b. .d88b 8d8b 
8b  d8 8b d8 8.dP' `Yb. `Yb.     8   8P Y8 8  8  8     8  "8 8b d8 8P Y8P Y8 8  8 8.dP' 8P   
`Y88P' `Y8P8 `Y88P Y88P Y88P     8   8   8 `Y88  Y8P   8   8 `Y8P8 8   8   8 88P' `Y88P 8    
                                                                                             
 """

possible_numbers = []

for num in range (1, 101):
    possible_numbers.append(num)

def play():
    print(logo)
    end_of_game = False
    random_number = random.choice(possible_numbers)

    difficulty = input('I\'m thinking of a number between 1 and 100.\n\nTo choose a difficulty type either "easy" or "hard".\n').lower()

    if difficulty == 'easy':
        lives = 10
        print(f'You have {lives} attempts remaining to guess the number.\n')
    elif difficulty == 'hard':
        lives = 5
        print(f'You have {lives} attempts remaining to guess the number.\n')

    while not end_of_game:

        guess = int(input('Make a guess: \n'))

        if guess == random_number:
            print(f'You got it! The answer was {random_number}\n')
            end_of_game = True
        elif lives == 0:
            print('You\'ve run out of guesses. You lose!\n')
            end_of_game = True
        elif guess < random_number:
            lives -= 1
            print(f'Too low!\n\nYou have {lives} attempts remaining to guess the number.\n')
            if lives == 0:
                print(f'The number was {random_number}\n')
                end_of_game = True
        elif guess > random_number:
            lives -= 1
            print(f'Too high!\n\nYou have {lives} attempts remaining to guess the number.\n')
            if lives == 0:
                print(f'The number was {random_number}\n')
                end_of_game = True

    replay = input('Would you like to play a guessing game? Type "y" to play, type "n" otherwise.\n')
    if replay == 'y':
        play()
play()
