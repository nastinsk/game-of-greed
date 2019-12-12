import collections
import random

class User:
    def __init__(self, total_score=0, current_score=0):
        self.total_score = total_score
        self.current_score = current_score




class Game:
    """Class to crete Game instances"""

    def __init__(self, print_f = print, input_f = input):
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
        'unique_pairs': 1500,
        'mcflurry': 2000
        }
        self.total_score = 0
        self.current_score = 0
        self.input_ = input_f
        self.print_ = print_f

    def calculate_score(self, dice_roll):
        """Method to calculate score based on the input of the dice rolls that represented as tuple"""

        roll = dice_roll
        if len(str(dice_roll)) > 1:
            roll_counter = collections.Counter(roll)


            try:
                result = 0

                for index, (key, val) in enumerate(roll_counter.items()):
                    if index == 5 and key in self.combinations and val == 1:
                        return self.combinations['straight']

                    if len(roll_counter) == 3 and index == 2 and val == 2 and key in self.combinations:
                        return self.combinations['unique_pairs']

                    if len(roll_counter) == 2 and val == 4 and key == 5 and 1 in roll_counter.keys():
                        return self.combinations['mcflurry']

                    if val in self.combinations[key].keys():
                        result+= self.combinations[key][val]
                return(result)

            except KeyError:
                return('invalid value')
        else:
            if roll == 5:
                self.current_score += 50
                return self.current_score
            if roll == 1:
                self.current_score += 100
                return self.current_score
            else:
                self.current_score += 0
                return self.current_score


    def play(self):
        """Method to create initial game flow"""

        self.print_("**************************\n\nWelcome to the Greed Game!\n\nTo see the rules go to:\n https://en.wikipedia.org/wiki/Dice_10000\n")
        if self.input_("Wanna play?\n\n") == 'y':
            self.print_("\nGreat!\n")
            self.new_roll(6)
        else:
            self.print_("\nOK. Maybe another time\n")

    def roll_set(self, value):
        """method to roll dice between 1 and 6"""
        dice_roll = []
        for i in range(value):
            dice_roll.append(random.randint(1,6))
        return dice_roll

        # or
        # return [random.randint(1, 6) for i in range(value)]




    def set_aside(self, u_input, rolled_dice, dice_amount):

        if len(u_input) > 1:
            try:
                user_dice =  [int(n) for n in u_input.split(' ')]
                print(user_dice, "user dice")
                print(rolled_dice, "rolled")

                # line 106 from https://stackoverflow.com/questions/3847386/testing-if-a-list-contains-another-list-with-python

                if all(elem in rolled_dice for elem in user_dice):
                    print(user_dice, "user dice2")
                    print(rolled_dice, "rolled2")
                    self.current_score += self.calculate_score(user_dice)
                    u_input = self.input_(f"You set aside {len(user_dice)} dice. You're current score is {self.current_score}. Yor total score is {self.total_score}. Hit 'b' if you want\n to bank it, hit any other key if you want to roll {dice_amount-len(user_dice)} remaining dice\n")

                    if u_input == 'b':
                            self.total_score += self.current_score
                            self.print_(f"\nYour total score is {self.total_score}\n")
                            self.current_score = 0
                            self.new_roll(6)
                    else:
                        # self.current_score = 0
                        self.new_roll(dice_amount-len(user_dice))
                else:
                    self.print_(f'\n*** {user_dice} is not your dice you lost all your current points \nYou\'re total score is  {self.total_score}\n')
                    self.current_score = 0
                    self.new_roll(6)

            except ValueError:
                self.print_(f"HIT FIRST This is not an integer you lost your current points. Your total score is {self.total_score}\n")
                self.current_score = 0
                self.new_roll(6)

        else:
            try:
                if len(u_input) == 1 and u_input.isdigit():
                    if int(u_input) in rolled_dice:
                        self.current_score += self.calculate_score(int(u_input))
                        u_input = self.input_(f"You set aside {len(u_input)} die. You're current score is {self.current_score}. Yor total score is {self.total_score}. Hit 'b' if you want to bank it, hit any other key if you want to roll {dice_amount-1} remaining dice\n")

                        if u_input == 'b':
                            self.total_score += self.current_score
                            self.print_(f"\nYour total score is {self.total_score}\n")
                            self.current_score = 0
                            self.new_roll(6)

                        else:
                            # self.current_score = 0
                            self.new_roll(dice_amount-1)

                    else:
                        print(f'\n*** {u_input} is not your dice you lost all your current points \nYou\'re total score is  {self.total_score}\n')
                    self.current_score = 0
                    self.new_roll(6)
                    
            except:
                self.print_(f"\nHIT SECONdThis is not an integer you lost your current points. Your total score is {self.total_score}\n")
                self.current_score = 0
                self.new_roll(6)



    def new_roll(self, dice_amount):

        if self.input_(("\n*** Hit any key to roll the dice\n")) or '\n':
            new_roll = self.roll_set(dice_amount)
            user_input = self.input_(f'\n*** Here is your dice {new_roll} set aside at least one die \nto roll again (use spaces to multiple dice) or hit "b" \nto Bank your {self.current_score} Current Points\n\n')
            if user_input == 'b':
                self.total_score += self.current_score
                self.print_(f"Your total score is {self.total_score}")
                self.current_score = 0
                self.new_roll(6)
            else:
                self.set_aside(user_input, new_roll, dice_amount)



if __name__ == "__main__":

    game = Game()
    game.play()
    # print(game.calculate_score((1, 2, 3, 3, 2, 4)))
    # print(game.roll(3))
