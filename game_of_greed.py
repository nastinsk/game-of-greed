import collections
class Game:
    def __init__(self):
        self.name = "Game of Greed"
        self.combinations = {
        1:{1:100, 2:200, 3:1000, 4:2000, 5:3000, 6:4000},
        2:{3:200, 4:400, 5:600, 6:800},
        3:{3:300, 4:600, 5:900, 6:1200},
        4:{3:400, 4:800, 5:1200, 6:1600},
        5:{1:50, 2:100, 3:500, 4:1000, 5:1500, 6:2000},
        6:{3:600, 4:1200, 5:1800, 6:2400},
        'straight': 0
        }

    def calculate_score(self, dice_roll):
        roll = dice_roll
        roll_counter = collections.Counter(roll)
        print(roll_counter)
        try:
            result = 0

            for key, val in roll_counter.items():
                if val in self.combinations[key].keys():
                    result+= self.combinations[key][val]
            print(result)
        except KeyError:
            print('invalid value')


    def play(self):
        print("**************************\n\nWelcome to the Greed Game!\n\nTo see the rules go to:\n https://en.wikipedia.org/wiki/Dice_10000\n")
        if input("Wanna play?\n") == 'y':
            print("Great! Check back tomorrow :D\n")
        else:
            print("OK. Maybe another time\n")

#   create calculate_score method to game class;
#            input for this is a tuple representing the dice roll
#            the output is an integer representing a dice roll
    # add play instance method to Game class
        # greet user
        # prompt user "Wanna play?"
        # if users enters 'y' print "Great! Check back tomorrow :D"
        #if other print "OK. Maybe another time"
#
my_game = Game()
my_game.play()
my_game.calculate_score((1, 1, 1, 5, 5, 5))
