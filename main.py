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
        self.colors = ['r','b','g','y']
        self.available_moves = self.moves

        if not grid:
            self.grid = [['' for c in range(num_cols)] for r in range(num_rows)]
            print(self.grid)
            for r in range(num_rows):
                for c in range(num_cols):
                    self.grid[r][c] = self.colors[random.randrange(len(self.colors))]
            print(self.grid)
        else:
            self.grid = [row.copy() for row in grid]

    def fill(self,new_color:str, x:int,y:int)->bool:
        """ Fills cell and adjacent cell with new_color"""
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

        # decrement the num of moves left if a valid fill operation
        self.available_moves -= 1
        return True
    
    def check_win(self)->bool:
        """Determines if the game has ended"""

        # win condition
        if all(cell == self.target_color for row in self.grid for cell in row):
            print("You have won!")
            return True
        # no moves left
        if self.available_moves == 0:
            print("You have lost")
            return True
        # moves left
        return False

    def display(self):
        """ Displays the grid with game info"""
        print(f"Target Color: {self.target_color}\n"
              f"Moves Left: {self.available_moves}\n"
              f"Pick a color and position as follows `<color> <row> <col>` to change color\n")
        for row in self.grid:
            print(' '+' '.join(cell for cell in row))
        print()

    def get_input(self):
        """ Gets and validates user input"""
        while True:
            user_input = input()
            args = user_input.replace(',',' ').split() # commas found
            args = user_input.replace('  ',' ').split() # mutlie spaces found

            # input validation
            if len(args) != 3:
                print("Invalid input, valid example:  `r 1 0`")
                continue

            color = args[0]
            if color not in self.colors:
                print(f"Invalid color, use any of {self.colors}")
                continue
             
            x = int(args[1])
            y = int(args[2]) 
            return color,x,y
    
    def play(self):
        """Main game loop"""
        print("starting game")
        while not self.check_win():
            self.display()
            color,x,y = self.get_input()
            self.fill(color,x,y)

if __name__ == '__main__':

    grid1 = [['g','g','g','g'],
             ['g','b','b','g'],
             ['g','b','b','g'],
             ['g','g','g','g']]

    game = ColorPalette(4,4,4,'r',grid1)
    game.play()
