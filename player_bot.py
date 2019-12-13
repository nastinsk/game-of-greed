from game import Game

class LazyPlayer:
    # constructor, play and calcuate_score available
    # everything else is done only with I/O
    # def __init__(self):
    #     self.roll = None

    def _print(self, *args):
        print('bot')
        print(args[0])

    def _input(self, *args):
        print('bot2')
        print(args[0], 'n')
        return 'n'

class BotPlayer:
    




if __name__ == "__main__":
    bot = LazyPlayer()
    game = Game(bot._print, bot._input)
    bot.game = game
    game.play(10)
