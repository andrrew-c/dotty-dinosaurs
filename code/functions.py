from random import choice

# Choices of colours
choices = 'red', 'blue', 'yellow', 'orange', 'green', 'purple'

def roll_dice(dice_options):

    """ :params dice_options - LIST - Options to select from"""

    return choice(dice_options)


class Player():

    def __init__(self):

        # Each player starts with a board of empty colours
        self.dinosaur = {c:0 for c in choices}






