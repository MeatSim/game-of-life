import random

height = 100
width = 100

def randomize(grid, width, height):
    for i in range(0, height):
        for j in range(0, width):
            grid[i][j] = random.randint(0,1)

grid_model = [0] * height
next_grid_model = [0] * height
for i in range(height):
    grid_model[i] = [0] * width
    next_grid_model[i] = [0] * width

def count_neighbors(grid, row, col):
    count = 0
    
    #count surrounding neighbors up to edge
    #above
    if row-1 >=0:
        count += grid[row-1][col]
        #above left
        if (col-1 >= 0):
            count += grid[row-1][col-1]
        #above right
        if (col+1 < width):
            count += grid[row-1][col+1]
    #left
    if col-1 >= 0:
        count += grid[row][col-1]
    #right
    if col+1 < width:
        count += grid[row][col+1]
    #below
    if row+1 < height:
        count += grid[row+1][col]
        #below left
        if (col-1 >= 0):
            count += grid[row+1][col-1]
        #below right
        if (col+1 < width):
            count += grid[row+1][col+1]

    #upper edge wraps to bottom edge
    if row == 0:
        count += grid[height-1][col]
        #upper left corner
        if col == 0:
            count += grid[height-1][width-1]
            count += grid[height-1][col+1]
            count += grid[row+1][width-1]
        #upper right corner
        elif col+1 == width:
            count += grid[height-1][0]
            count += grid[height-1][col-1]
            count += grid[row+1][0]
        #not corner
        else:
            count += grid[height-1][col-1]
            count += grid[height-1][col+1]
    
    #left edge wraps to right edge
    if col == 0:
        count += grid[row][width-1]
        #not corner
        if row != 0 and row+1 != height:
            count += grid[row-1][width-1]
            count += grid[row+1][width-1]

    #right edge wraps to left edge
    if col+1 == width:
        count += grid[row][0]
        #not corner
        if row != 0 and row+1 != height:
            count += grid[row-1][0]
            count += grid[row+1][0]

    #bottom edge wraps to top edge
    if row+1 == height:
        count += grid[0][col]
        #bottom left corner
        if col == 0:
            count += grid[0][width-1]
            count += grid[row-1][width-1]
            count += grid[0][col+1]
        #bottom right corner
        elif col+1 == width:
            count += grid[0][0]
            count += grid[0][col-1]
            count += grid[row-1][0]
        #not corner
        else:
            count += grid[0][col-1]
            count += grid[0][col+1]
            
    return count

def clear_cells():
    global height, width, grid_model

    for i in range(0, height):
        for j in range(0, width):
            grid_model[i][j] = 0

glider_pattern = [[0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0]]

glider_gun_pattern = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def load_pattern(pattern, x_offset=0, y_offset=0):
    global grid_model

    clear_cells()

    j = y_offset

    for row in pattern:
        i = x_offset
        for value in row:
            grid_model[i][j] = value
            i = i + 1
        j = j + 1

def next_gen():
    global grid_model, next_grid_model
    for i in range(0, height):
        for j in range(0, width):
            cell = 0

            #count number of live neighbors
            count = count_neighbors(grid_model, i, j)

            #cell 'lives' according to rules
            if grid_model[i][j] == 0 and count == 3:
                cell = 1
            elif grid_model[i][j] == 1:
                if count == 2 or count == 3:
                    cell = 1

            #record result on next_grid_model
            #so that result doesn't interfere with other calculations
            next_grid_model[i][j] = cell

    #swap grid_model with next_grid_model after all calculations
    temp = grid_model
    grid_model = next_grid_model
    next_grid_model = temp

            

if __name__ == '__main__':
    next_gen()
                
            
    
