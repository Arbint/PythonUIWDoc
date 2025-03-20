from functions import GetPlayerInput
import functools

def RunGame(GameEntry):
    @functools.wraps(GameEntry)
    def wrapper(*args, **kwargs):
        while True:
            GameEntry(*args, **kwargs)
            playAgain = GetPlayerInput(options = ["Y", "N"], message = "Do you want to play again?")
            if playAgain.upper() == "N":
                break

    return wrapper