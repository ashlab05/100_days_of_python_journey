import random

print(""" __      __       .__                                ___________
/  \    /  \ ____ |  |   ____  ____   _____   ____   \__    ___/___
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \    |    | /  _ \
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/    |    |(  <_> )
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >   |____| \____/
       \/       \/          \/            \/     \/
 _______               ___.                    ________                            .__                   ________
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ """)


while True:
    # Get the user input to ask the level
    if input('Please choose your difficulty level easy/hard: ').lower() == 'easy':
        lives = 10
    else:
        lives = 5
    # Computer Guess
    computer_guess = random.randint(1, 100)
    print(f'Secret computer guessed {computer_guess}\n')
    while lives > 0:
        print(f'Remaining lives: {lives}')
        # User to guess
        user_guess = int(input('Guess the number: '))
        diff = user_guess - computer_guess

        if diff  ==  0:
            print('You guessed the number')
            break
        if diff < 0 :
            if -diff >= 10:
                print('Your guess is too low')
            else:
                print('Your guess is low')

        if diff > 0 :
            if diff >= 10:
                print('Your guess is too High')
            else:
                print('Your guess is high')
        lives = lives-1
    print('\n' * 5)
