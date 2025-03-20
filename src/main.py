from rockPaperScissors import RockPaperScissors
from hangMan import Hangman
from functions import GetPlayerInput
from gameRunner import RunGame

@RunGame
def PlayGames():
    games = {RockPaperScissors.__name__:RockPaperScissors, 
            Hangman.__name__:Hangman 
            }


    playerPick = GetPlayerInput(message="Please Pick a Game",options = list(games.keys()))
    (games[playerPick])()


if __name__ == "__main__":
    PlayGames()