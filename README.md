# Game Of Greed

**Author**: Anastasia Lebedeva
**Version**: 1.1.1

## Overview
Command line version of the dice game - Game Of Greed.
To learn the rules go [here](https://en.wikipedia.org/wiki/Dice_10000)


## Getting Started
1. Run command 'python3 game_of_greed.py'
2. Type 'y' + Enter to play,
type anything else + Enter to quit.
3. To run the test run "pytest -s"


## Architecture
* Python 3.7.5
* Pipenv
* Pytest


## API
1. .__init__()  - method to initiate new Game instance with the combinations dictionary
2. .play() - Method to create initial game flow
3. .calculate_score() - Method to calculate score based on the input of the dice rolls that represented as a tuple
4. Game()
5. User()
6. .roll()
7. .gameflow()


## Change Log

* 12/09/2019 17:01 - Initial setup
* 12/09/2019 18:30 - .play() method added
* 12/09/2019 19:45 - combinations added
* 12/09/2019 00:30 - calculate_score function finished
* 12/10/2019 01:05 - all current tests pass
* 12/10/2019 16:37 - test for roll method created, roll method created
