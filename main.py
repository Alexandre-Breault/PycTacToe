import os
from player import Player
from esymbole import Symbole, Config, Color
from config.config import config
#TODO 
# Ameliorer le code
#
'''Partie configuration'''
configs = config.read_config()
player=configs[Config.nombre_participant.name]
list_color = list(Color)
color= (Color[configs[Config.color_player.name]].value, Color[configs[Config.color_player2.name]].value)
list_player = list()
list_symbole = list(Symbole)



for i in range(player):
    list_player.append(Player("player"+str(i), list_symbole[i].value, color[i]))
brick = "[ ]"
rows, cols = (3, 3)
lines = [[brick for i in range(cols)] for j in range(rows)]
player_round=0

def cls():
    ''' Permet de clear la console '''
    os.system('cls')

def compte_round():
    global player_round
    player_round=player_round+1
def array_line():
    i = 0
    print("".join([" "+str(j)+" " for j in range(len(lines))]))
    for row in lines:
        print(''.join([str(elem) for elem in row])+" "+str(i))
        i= i+1

def get_player():
    if player_round % 2==0:
        select = 1
    else:
        select = 0
    return select

def array_console():
    array_line()
    add_bateau()
    
def add_bateau():
    try:
        print("Au tour de "+list_player[get_player()].toString())
        line= int(input("Saisir une line : "))
        column=int(input("Saisir une colonne : "))
        if check_empty(line, column):
            lines[line][column] = list_player[get_player()].get_symbole()
        else:
            cls()
            array_line()
            add_bateau()
        if not check_win():
            cls()
            replay()
        else:
            cls()
            array_line()
            print(list_player[get_player()].toString(),"WIN !!!!")
    except ValueError as e:
        cls()
        print(e)
        array_line()
        add_bateau()
    except Exception as e:
        cls()
        print(e)
        array_line()
        add_bateau()
        

def replay():
    compte_round()
    array_console()

def check_win():
    isWin=False
    if check_lines_player():
        isWin=True
    if check_column_player():
        isWin=True
    if check_diagonal_player():
        isWin=True
    return isWin

def check_lines_player():
    isOk = False
    for row in lines:
        if(row[0] == row[1] and row[2] == row[0]) and row[0] is not brick:
            isOk = True
    return isOk

def check_column_player():
    isOk= False
    if (lines[0][0] == lines[1][0] and lines[0][0] == lines[2][0]) and lines[0][0] is not brick:
        isOk= True
    elif (lines[0][1] == lines[1][1] and lines[0][1] == lines[2][1]) and lines[0][1] is not brick:
        isOk= True
    elif (lines[0][2] == lines[1][2] and lines[0][2] == lines[2][2]) and lines[0][2] is not brick:
        isOk= True
    return isOk

def check_diagonal_player():
    isOk = False
    if(lines[0][0] == lines[1][1] and lines[0][0] == lines[2][2]) and not check_empty(0,0):
        isOk=True
    elif(lines[0][-1] == lines[1][1] and lines[0][-1] == lines[2][0]) and not check_empty(0,-1):
        isOk=True
    return isOk


def check_empty(l,c):
    '''Permet de verifier si la case est vide ou pas'''
    return  True if lines[l][c] == brick else False

try:
    array_console()
    input()
    
except Exception as exce:
    print(exce)
    input()