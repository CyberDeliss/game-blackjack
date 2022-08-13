from classes import *

game = Game()

# add condition about max of players

count_of_players = input_int_count()
game.start_game(count_of_players)

while True:
    game.loop()
    game.end_loop()
    print("Do you want play again?\n")
    if input_yes() and game.players:
        game.restart_game()
        continue
    break
