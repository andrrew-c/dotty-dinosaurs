from random import choice
from turtle import pos

from numpy import cov

# Choices of colours
choices = 'red', 'blue', 'yellow', 'orange', 'green', 'purple'



class Player():

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
        

