from main import ColorPalette
import pytest

grid1 = [['g','g','g','g'],
         ['g','b','b','g'],
         ['g','b','b','g'],
         ['g','g','g','g']]

expected1 = [['g','g','g','g'],
             ['g','y','y','g'],
             ['g','y','y','g'],
             ['g','g','g','g']]

expected2 = [['r','r','r','r'],
             ['r','b','b','r'],
             ['r','b','b','r'],
             ['r','r','r','r']]
 
def test_grid1_fill_inner():
    rows = len(grid1)
    cols = len(grid1[0])
    test_grid = ColorPalette(rows,cols,4,'y',grid1)

    # check no change
    test_grid.fill(1,1,'b') 
    assert test_grid.grid == grid1
    # check update made only on inner
    test_grid.fill(1,1,'y')
    assert test_grid.grid == expected1

def test_grid1_fill_outer():
    rows = len(grid1)
    cols = len(grid1[0])
    test_grid = ColorPalette(rows,cols,4,'y',grid1)

    test_grid.fill(0,0,'g')
    assert test_grid.grid == grid1
    test_grid.fill(0,0,'r')
    assert test_grid.grid == expected2

