import os
from player import Player


class Map:
    PLAYERS = None
    def __init__(self) -> None:
        self.column = 3
        self.row = 3
        self.brick = "[ ]"
        self.lines = [[self.brick for i in range(self.column)] for j in range(self.row)]      
    
    def set_player_in_map(self, players: Player):
        self.PLAYERS = players
    
    def draw(self):
        self.__cls()
        i = 0
        print("".join([" "+str(j)+" " for j in range(len(self.lines))]))
        for row in self.lines:
            print(''.join([str(elem) for elem in row])+" "+str(i))
            i= i+1
    
    def edit_map(self, line: int, column:int, player:int):
        if self.__check_empty_box(line, column):
            self.lines[line][column] = self.PLAYERS[player].get_symbole()
    
    def __check_empty_box(self,l,c):
        return True if self.lines[l][c] == self.brick else False
    
    def __cls(self):
        ''' Permet de clear la console '''
        os.system('cls')
        
    def check_line_win(self) -> bool:
        isOk = False
        for row in self.lines:
            if(row[0] == row[1] and row[2] == row[0]) and row[0] is not self.brick:
                isOk = True
        return isOk
    
    def check_column_win(self) ->bool:
        isOk= False
        if (self.lines[0][0] == self.lines[1][0] and self.lines[0][0] == self.lines[2][0]) and self.lines[0][0] is not self.brick:
            isOk= True
        elif (self.lines[0][1] == self.lines[1][1] and self.lines[0][1] == self.lines[2][1]) and self.lines[0][1] is not self.brick:
            isOk= True
        elif (self.lines[0][2] == self.lines[1][2] and self.lines[0][2] == self.lines[2][2]) and self.lines[0][2] is not self.brick:
            isOk= True
        return isOk
    
    def check_diagonal_win(self):
        isOk = False
        if(self.lines[0][0] == self.lines[1][1] and self.lines[0][0] == self.lines[2][2]) and not self.__check_empty_box(0,0):
            isOk=True
        elif(self.lines[0][-1] == self.lines[1][1] and self.lines[0][-1] == self.lines[2][0]) and not self.__check_empty_box(0,-1):
            isOk=True
        return isOk
    
    def check_win(self) -> bool:
        isWin=False
        if self.check_line_win():
            isWin=True
        if self.check_column_win():
            isWin=True
        if self.check_diagonal_win():
            isWin=True
        return isWin