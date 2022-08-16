import lichess.api
from lichess.format import JSON
import chess
import time

wrong_name = True

while wrong_name:
    user = input("Enter your Name on Lichess: ")
    try:
        games = lichess.api.user_games(user, format=JSON)
        wrong_name = False
    except:
        print("\nThis name is not avaiable")

game = next(games)
white_player = game["players"]["white"]["user"]["id"]
black_player = game["players"]["black"]["user"]["id"]
winner_color = game["winner"]
move_list = game["moves"].split(" ")

if winner_color == "white":
    winner = white_player
if winner_color == "black":
    winner = black_player

board = chess.Board()

print("\nYOUR LAST GAME ON LICHESS\n")
time.sleep(1.5)
print(white_player + " (White) vs. " + black_player + " (Black)\n")
time.sleep(1.5)
for i in move_list:
    board.push_san(i)
    print("--------" + black_player)
    print(board)
    print("--------" + white_player + "\n")
    time.sleep(0.5)

if winner == user.lower():
    print("\n\nYou are the winner")
else:
    print(winner + " is the winner!")



