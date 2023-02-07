class Map:
    def __init__(self) -> None:
        self.column = 3
        self.row = 3
        self.brick = "[ ]"
        self.lines = [[self.brick for i in range(self.column)] for j in range(self.row)]      
        
    def draw(self):
        i = 0
        print("".join([" "+str(j)+" " for j in range(len(self.lines))]))
        for row in self.lines:
            print(''.join([str(elem) for elem in row])+" "+str(i))
            i= i+1