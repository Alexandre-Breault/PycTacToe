import os
from map import Map
from setup import Setup

'''Partie configuration'''
setup = Setup()
list_player = setup.get_player_list()
scene = Map()
map = scene.lines
brick = scene.brick
player_round=0

def cls():
    ''' Permet de clear la console '''
    os.system('cls')

# def compte_round():
#     global player_round
#     player_round=player_round+1

# def get_player():
#     if player_round % 2==0:
#         select = 1
#     else:
#         select = 0
#     return select
    
# def add_bateau():
#     try:
#         print("Au tour de "+list_player[get_player()].toString())
#         line= int(input("Saisir une line : "))
#         column=int(input("Saisir une colonne : "))
#         if check_empty(line, column):
#             map[line][column] = list_player[get_player()].get_symbole()
#         else:
#             cls()
#             # array_line()
#             add_bateau()
#         if not check_win():
#             cls()
#             replay()
#         else:
#             cls()
#             array_line()
#             print(list_player[get_player()].toString(),"WIN !!!!")
#     except ValueError as e:
#         cls()
#         print(e)
#         # array_line()
#         add_bateau()
#     except Exception as e:
#         cls()
#         print(e)
#         array_line()
#         add_bateau()
        

# def replay():
#     compte_round()
#     array_console()

# def check_win():
#     isWin=False
#     if check_lines_player():
#         isWin=True
#     if check_column_player():
#         isWin=True
#     if check_diagonal_player():
#         isWin=True
#     return isWin

# def check_lines_player():
#     isOk = False
#     for row in map:
#         if(row[0] == row[1] and row[2] == row[0]) and row[0] is not brick:
#             isOk = True
#     return isOk

# def check_column_player():
#     isOk= False
#     if (map[0][0] == map[1][0] and map[0][0] == map[2][0]) and map[0][0] is not brick:
#         isOk= True
#     elif (map[0][1] == map[1][1] and map[0][1] == map[2][1]) and map[0][1] is not brick:
#         isOk= True
#     elif (map[0][2] == map[1][2] and map[0][2] == map[2][2]) and map[0][2] is not brick:
#         isOk= True
#     return isOk

# def check_diagonal_player():
#     isOk = False
#     if(map[0][0] == map[1][1] and map[0][0] == map[2][2]) and not check_empty(0,0):
#         isOk=True
#     elif(map[0][-1] == map[1][1] and map[0][-1] == map[2][0]) and not check_empty(0,-1):
#         isOk=True
#     return isOk


# def check_empty(l,c):
    '''Permet de verifier si la case est vide ou pas'''
    return  True if map[l][c] == brick else False


# array_console()

scene.draw()