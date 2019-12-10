import collections

class Game:
    """Class to crete Game instances"""

    def __init__(self):
        """Method to initiate new Game instance with the combinations dictionary"""
        self.name = "Game of Greed"
        self.combinations = {
        1:{1:100, 2:200, 3:1000, 4:2000, 5:3000, 6:4000},
        2:{3:200, 4:400, 5:600, 6:800},
        3:{3:300, 4:600, 5:900, 6:1200},
        4:{3:400, 4:800, 5:1200, 6:1600},
        5:{1:50, 2:100, 3:500, 4:1000, 5:1500, 6:2000},
        6:{3:600, 4:1200, 5:1800, 6:2400},
        'straight': 1500,
        'unique_pairs': 1500
        }

    def calculate_score(self, dice_roll):
        """Method to calculate score based on the input of the dice rolls that represented as tuple"""

        roll = dice_roll
        roll_counter = collections.Counter(roll)

        try:
            result = 0

            for index, (key, val) in enumerate(roll_counter.items()):
                if index == 5 and key in self.combinations and val == 1:
                    return self.combinations['straight']

                # TO DO: refactor this one. Mb there is a way to make shoreter?

                if len(roll_counter) == 3 and index == 2 and val == 2 and key in self.combinations:
                    return self.combinations['unique_pairs']


                if val in self.combinations[key].keys():
                    result+= self.combinations[key][val]
            return(result)
        except KeyError:
            return('invalid value')


    def play(self):
        """Method to create initial game flow"""

        print("**************************\n\nWelcome to the Greed Game!\n\nTo see the rules go to:\n https://en.wikipedia.org/wiki/Dice_10000\n")
        if input("Wanna play?\n\n") == 'y':
            print("\nGreat! Check back tomorrow :D\n")
        else:
            print("\nOK. Maybe another time\n")

game = Game()
game.play()
print(game.calculate_score((1, 2, 3, 3, 2, 4)))
