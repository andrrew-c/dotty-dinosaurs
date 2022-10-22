from random import choice
from turtle import pos

from numpy import cov

# Choices of colours
choices = 'red', 'blue', 'yellow', 'orange', 'green', 'purple'



class Player():

    """ Player of Dotty Dinosaurs

        A player starts with a board (self.dinosaur) that is initialised as blank.

        For each roll of the dice, the player updates their board to match the colour returned by the dice.
        For example, when a player rolls a 'red', they can add a 'red' piece to their dinosaur/board.

        (self.num_rolls) Integer - Each player keeps a note of how many rolls they've made.
        (self.win) Boolean - Each player checks after their turn, whether they have won.
    """

    def __init__(self):

        # Each player starts with a board of empty colours
        self.dinosaur = {c:0 for c in choices}

        # Initialise record of number of rolls
        self.num_rolls = 0

        # Initialise each player's win status
        self.win = False

    def roll_dice(self, dice_options):

        """ :params dice_options - LIST - Options to select from"""

        return choice(dice_options)

    def play_round(self):

        """ Roll dice and update board to 1 for that colour"""

        # Roll dice
        dice = self.roll_dice(choices)

        # Update rolls
        self.num_rolls += 1


        # Set value of dice (on board) to 1
        self.dinosaur.update({dice:1})

        # Now check whether I've won as a result of the change
        self.check_if_win()

    def check_if_win(self):
        """ If all colours on board are covered, then announce the win! """

        # Possible number of areas on board to play
        possible_areas = len(self.dinosaur)

        # Total number of covered spots
        covered_spots = sum(self.dinosaur.values())

        # If all spots are covered, then I've wone
        if possible_areas == covered_spots:
            self.win = True
            print("Yes!! I've won!")
        

class Game():

    """ A game of Dotty Dinosaurs 

        We initialise each player and play a game of Dotty Dinosaurs until one player wins.
    """

    def __init__(self, num_players):

        """ Initialise the game with a list for each player"""

        # Keep a note of the number of players in the game
        self.num_players = num_players

        # Initialise the players of the game
        self.players = [Player() for p in range(self.num_players)]

        # Initialise winning status to False
        self.any_winners = False

    def check_if_winner(self):

        """ Return True if there's at least one winner across the players"""

        # All win statuses
        num_winners = sum([player.win for player in self.players])

        # Return True if there's at least one winner
        return True if num_winners > 0 else False
        


    def play_round(self):

        """ Play a single round of the game, across each player"""

        # For each player in game
        for player in self.players:

            # Play a round
            player.play_round()

    def play_game(self):

        """ Keep playing rounds until there's a winner"""

        # While there's no winner
        while not self.check_if_winner():

            # Play a round
            game.play_round()

    # Print boards
    def print_boards(self):

        """ View each players board"""

        for p in range(len(self.players)):
            player = self.players[p]
            print(f"Player {p:,} with board {player.dinosaur}")
            


if __name__ == "__main__":

    # Start small with 2 players
    num_players = 2

    # Init Game
    game = Game(2)

    # Play a round over all players
    game.play_game()
