from gameit.example import exampleGame
from gameit.aqeelshamz import treasureHunt
from gameit.MohdShibin import snakeGame
from gameit.sreni import Tic_Tac_Toe
from gameit.kmSidharthM import Space_Invader

def main():
    games = {
      "example": exampleGame, 
      "aqeelshamz": treasureHunt, 
      "MohdShibin": snakeGame,
      "sreni":Tic_Tac_Toe, 
      "kmSidharthM":Space_Invader,
    }

    while True:
        username = input("Enter github username:\n")
        try:
            games[username]()
            print("Happy Gaming")
        except:
            print("Username not found!!.")


if __name__ == "__main__":
  main()
