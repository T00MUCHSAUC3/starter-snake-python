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

    #NOTE WHERE ARE THE OTHER SNAKES?

    get_snakes(env[4], OS[0].get("id"), grid) 
    final_grid = [grid, food_coord]

    return final_grid


def get_snakes(snakes, ourSnakeID, init_grid):
    
    #NOTE Get other snakes that aren't me and return them
    for snake in snakes:
        body = snake.get("body")
        this_id = snake.get("id")

        if this_id != ourSnakeID:
            head = body[0]
            x = head.get("x")
            y = head.get("y")

            top = y-1
            bottom = y-1
            left = x-1
            right = x+1

            if top > 0:
                init_grid[top][x] = 0
            if bottom < height:
                init_grid[bottom][x] = 0
            if left > 0:
                init_grid[y][left] = 0
            if right < width:
                init_grid[y][right] = 0

        for coord in body:
            x = coord.get("x")
            y = coord.get("y")
            init_grid[y][x] = 0


def get_distance(point_x, point_y):

    """
    This method will get the distance between two points
    """

    return (math.hypot(point_x[0] - point_y[0], point_x[1] - point_y[1]))

def closestFood():

    """
    This method will get the closest food to our snake
    """

    infinity = float('inf')
    
    return 0
