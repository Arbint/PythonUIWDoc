import random
from functions import GetPlayerInput
from gameRunner import RunGame


@RunGame
def RockPaperScissors():
    moves = ["rock", "paper", "scissors"] 
    playerMove = GetPlayerInput(options = moves, message = "please pick a move")

    print(f"your move: {playerMove}")

    computerMove = moves[random.randrange(0, len(moves))]
    print(f"computer move: {computerMove}")

    if playerMove == computerMove:
        print("it's a tie")
    elif moves.index(computerMove) == (moves.index(playerMove) + 1)%len(moves): 
        print("you lose!")
    else:
        print("you win!")


if __name__ == "__main__":
    print(f"you are running: {RockPaperScissors.__name__}")
    RockPaperScissors()