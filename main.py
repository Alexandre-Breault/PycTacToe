import os
from map import Map
from setup import Setup
setup = Setup()
list_player = setup.get_player_list()
scene = Map()
map = scene.lines
brick = scene.brick
scene.set_player_in_map(list_player)
player_round=0
game_win = scene.check_win()
winner = ""
scene.draw()
while not game_win:
    current_player = 1 if player_round % 2==0 else 0
    print("Joueur :", list_player[current_player].toString())
    line = int(input("Saisir une line : "))
    column = int(input("Saisir une colonne : "))
    scene.edit_map(line=line, column=column, player=current_player)
    player_round+=1
    scene.draw()
    game_win = scene.check_win()
    winner=list_player[current_player].toString()
print("Le joueur "+winner+" a gagné !!!")