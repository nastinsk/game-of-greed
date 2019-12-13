from game import Game

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

        if prompt == "which would you like to keep? ":
            score = self.game.calculate_score(self.roll)

        if prompt == 'Enter dice to keep: ':

            # without this line out response is int which make tuple in line 104 angry
            response_str = ''
            for val in self.roll:
                response_str += str(val)

            return response_str

            # if 1 in self.roll:
            #     return 1
            # if 5 in self.roll:
            #     return 1

if __name__ == "__main__":
    bot = BotPlayer()
    game = Game(bot._print, bot._input)
    bot.game = game
    game.play(10)
