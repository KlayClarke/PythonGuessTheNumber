import random

possible_numbers = []

for num in range (1, 101):
    possible_numbers.append(num)

def play():
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
