from game import Game
import collections

class LazyPlayer:


    def _print(self, *args):
        print('bot2 print')
        print(args[0])

    def _input(self, *args):
        print('bot2 input')
        print(args[0], 'n')
        return 'n'

class BotPlayer:
    """ class to build BotPlayers"""

    def __init__(self):
        self.roll = None
        self.game = None
        self.combinations = {
        # 50:{5}
        # 100:{1, 55},
        # 200:{11, 222}
        # 300:{333}
        # 400:{444, 2222}
        # 500:{555}
        # 600:{22222, 3333, 666}
        # 800:{}
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

    def _print(self, *args):
        msg = args[0]
        if msg.startswith("You rolled"):
            self.roll = [int(char) for char in msg if char.isdigit()]

        print(msg)

    def _input(self, *args):
        prompt = args[0]

        if prompt == "Wanna play? ":
            print(prompt, 'y')
            return 'y'



        if prompt == 'Enter dice to keep: ':
            score = self.game.calculate_score(self.roll)

            roll_counter = collections.Counter(self.roll)
            str_to_return = ''
            for index, (key, val) in enumerate(roll_counter.items()):
                if index == 5 and key in self.combinations and val == 1:
                    return self.roll

                if len(roll_counter) == 3 and index == 2 and val == 2 and key in self.combinations:
                    return self.roll

                if len(roll_counter) == 2 and val == 4 and key == 5 and 1 in roll_counter.keys():
                    return self.roll

                if val in self.combinations[key].keys():

                    str_to_return+=str(key)
            return(str_to_return)

            # print(score)
            # if score == 50:
            #     return str(5)
            # if score == 100 and 1 in self.roll:
            #     return str(1)
            # if score == 100 and 5 in self.roll:
            #     return str(55)


            # without this line out response is int which make tuple in line 104 angry
            # response_str = ''
            # for val in self.roll:
            #     response_str += str(val)

            # return response_str

            # if 1 in self.roll:
            #     return str(1)
            # if 5 in self.roll:
            #     return str(5)

if __name__ == "__main__":
    bot = BotPlayer()
    game = Game(bot._print, bot._input)
    bot.game = game
    game.play(10)
