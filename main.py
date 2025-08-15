import random
import sys
from typing import List
from collections import deque

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
        # check bounds 
        if not (0<=x<self.num_cols and 0<=y<self.num_rows): 
            return False
        # get the color of the cell
        original_color = self.grid[x][y]
        # if the original color and the target color are the same, do nothing
        if original_color == new_color:
            return False

        # Fill (BFS) 
        queue = deque() 
        queue.append((x,y)) # add the selected cell
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            curr_x,curr_y = queue.popleft()

            if self.grid[curr_x][curr_y] != original_color:
                continue
            
            # change color
            self.grid[curr_x][curr_y] = new_color
            
            # apply to adjacent cells
            for dx,dy in dirs:
                nx,ny = curr_x+dx,curr_y+dy
                if (0<=nx<self.num_cols and
                    0<=ny<self.num_rows and
                    self.grid[nx][ny] == original_color):
                    queue.append((nx,ny))

        return True
