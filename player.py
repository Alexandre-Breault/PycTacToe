from esymbole import Color
class Player:
    
    def __init__(self,name, symbole, color=Color.CWHITE) -> None:
        self.name = name
        self.symbole = symbole
        self.color = color
        
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
        
    def toString(self):
        return self.name
    
    def get_symbole(self):
        return self.color+self.symbole+str(Color.RESET.value)