import random
import sys

class ColorPalette:
    def __init__(self,num_rows:int,num_cols:int,moves:int,target_color:str):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.moves = moves
        self.target_color
        
        colors = ['r','b','g','y']
        
    def fill(self,x:int,y:int,new_color:str)->bool:
        # check bounds and if the color is the same
        if 0<=x<self.num_cols and 0<=y<self.num_rows and new_color!=grid[x][y]:
            print(f"was {grid[x][y]} now {new_color}")
            grid[x][y] = new_color
            return True
        else:
            return False

        # Fill the rest recursively(BFS) 
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        for x1,x2 in dirs:
            nx = x+x1
            ny = y+y1
            print(f"checking {nx},{ny}")
            fill(nx,ny,new_color)
