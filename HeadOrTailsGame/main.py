#
#   Heads or tail game
#   The game will consist of 5 rounds.
#   In each round:
#   the user will make a guess,
#   the computer will flip a coin,
#   the player will get 1 point for a correct guess.
#

from random import randint

class CoinFlipper:

    def __init__(self):
        self.rounds = 5
        self.current_round = 0
        self.user_score = 0
        self.heads = 0
        self.tails = 1

    def FlipCoin(self, user_guess):    
        random_choice = randint(0,1)

        if random_choice == self.heads and user_guess == 'heads':
            self.user_score += 1
            print("You win, your score: " + str(self.user_score))
        elif random_choice == self.tails and user_guess == 'tails':
            self.user_score += 1
            print("You win, your score: " + str(self.user_score))
        else:
            print("You loose, your score: " + str(self.user_score))

if __name__ == '__main__':

    flipper = CoinFlipper()

    for i in range(flipper.rounds):
        flipper.current_round = i
        user_guess = input('Take a guess, \'heads\' or \'tails\'')
        if(user_guess == 'heads' or 'tails'):
            flipper.FlipCoin(user_guess)
        else:
            print('Wrong information was provided to the system \nTake a guess, \'heads\' or \'tails\'')
    
    if(flipper.user_score >= 3):
        print("You won the turnament with " + str(flipper.user_score) + " points")
    else:
        print("You lost the turnament with " + str(flipper.user_score) + " points")
