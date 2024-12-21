class Map:
    def __init__(self):
        self.layout = [[0,1,2,3,0],
        [3,3,2,1,0],
        [0,1,3,1,2],
        [3,2,1,0,3],
        [3,1,2,3,3]]
        self.playerPos = [0,0] # y,x
    def move(self,dir):
        if dir == "left":
            if (self.playerPos[1]-1)<0:
                print("Invalid move")
            else:
                self.playerPos[1] -=1
        elif dir == "right":
            if (self.playerPos[1]+1)>4:
                print("Invalid move")
            else:
                self.playerPos[1] +=1
        elif dir == "up":
            if (self.playerPos[0]-1)<0:
                print("Invalid Move")
            else:
                self.playerPos[0] -=1
        elif dir == "down":
            if (self.playerPos[0]+1)>4:
                print("Invalid Move")
            else:
                self.playerPos[0] +=1
        print(f"Coords ({str(self.playerPos[1])},{str(-self.playerPos[0])})")
        # player.interact(self.layout[self.playerPos[0]][self.playerPos[1]])
    def displayMap(self):

        top = ' '
        bottom = ' '
        left = ' '
        right = ' '
        if self.playerPos[0]-1>=0:
            top = (self.layout[self.playerPos[0]-1][self.playerPos[1]])
        if self.playerPos[0]+1>=-4:
            bottom = (self.layout[self.playerPos[0]+1][self.playerPos[1]])
        if self.playerPos[1]-1>=0:
            left = (self.layout[self.playerPos[0]][self.playerPos[1]-1])
        if self.playerPos[1]+1<=4:
            right = (self.layout[self.playerPos[0]][self.playerPos[1]+1])
        print(f"  {top}")
        print(f"{left} X {right}")
        print(f"  {bottom}")
    def deleteTile(self):
        self.layout[self.playerPos[0]][self.playerPos[1]] = 0
        print(self.layout[self.playerPos[1]][self.playerPos[0]])


hello = Map()
hello.move("right")
hello.deleteTile()
hello.displayMap()

