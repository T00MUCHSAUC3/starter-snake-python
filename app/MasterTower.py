import Astar, math, sys, random

#NOTE This function will set up our grid
def initGrid(env, OS):
    
    #NOTE SET UP GRID
    grid = []
    for col in range(0, env[1]):
        row = []
        for idx in range(0, env[2]):
            row.append(1)
        grid.append(row)

    #NOTE SET UP FOOD LOCATIONS
    food_coord = []
    for coord in env[3]:
        x = coord.get("x")
        y = coord.get("y")
        print("FOOD: ", x, y)
        food_coord.append([x, y])

    final_grid = [grid, food_coord]

    return final_grid
        

        
