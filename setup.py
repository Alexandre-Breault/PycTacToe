import json
import os
from player import Player
from esymbole import Symbole, Config, Color

class Setup:
    def __init__(self) -> None:
        self.config = self.__read_config()
        self.player_number = self.config[Config.nombre_participant.name]
        self.__list_color = list(Color)
        self.color = (Color[self.config[Config.color_player.name]].value, Color[self.config[Config.color_player2.name]].value)
        self.__list_player = []
        self.symbole = list(Symbole)
        self.__create_player()
        
    def __create_player(self):
        '''
        Permet de créer les joueurs et les ajouts a la liste player
        '''
        for i in range(self.player_number):
            self.__list_player.append(Player(name=("player ",str(i)),symbole=self.symbole[i], color=self.color[i]))

    def __read_config(self) -> dict:
        '''
        Lit la config dans le fichier de configuration
        '''
        json_file = open("config.json")
        data = json.load(json_file)
        return data

    def get_color(self, name):
        return self.__list_color[name]

    def get_player_list(self) -> list:
        return self.__list_player