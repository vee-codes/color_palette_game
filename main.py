import random
import sys
from typing import List

class ColorPalette:
    def __init__(self,num_rows:int,num_cols:int,moves:int,target_color:str,grid:List[List[str]]=None):
        """Initialize random grid"""
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.moves = moves
        self.target_color = target_color
        colors = ['r','b','g','y']

        if not grid:
            self.grid = [['' for c in range(num_cols)] for r in range(num_rows)]
            print(self.grid)
            for r in range(num_rows):
                for c in range(num_cols):
                    self.grid[r][c] = colors[random.randrange(len(colors))]
            print(self.grid)
        else:
            self.grid = [row.copy() for row in grid]

    def fill(self,x:int,y:int,new_color:str)->bool:
        # check bounds and if the color is the same
        if 0<=x<self.num_cols and 0<=y<self.num_rows and new_color!=grid[x][y]:
            print(f"was {grid[x][y]} now {new_color}")
            self.grid[x][y] = new_color
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
        
