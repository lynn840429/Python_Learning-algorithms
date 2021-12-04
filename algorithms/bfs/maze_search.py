from collections import deque

'''
BFS time complexity : O(|E| + |V|)
BFS space complexity : O(|E| + |V|)

do BFS from (0,0) of the grid and get the minimum number of steps needed to get to the lower right column

only step on the columns whose value is 1

if there is no path, it returns -1

Ex 1)
If grid is
[[1,0,1,1,1,1],
 [1,0,1,0,1,0],
 [1,0,1,0,1,1],
 [1,1,1,0,1,1]], 
the answer is: 14

Ex 2)
If grid is
[[1,0,0],
 [0,1,1],
 [0,1,1]], 
the answer is: -1
'''

def maze_search(maze):
    BLOCKED, ALLOWED = 0, 1
    UNVISITED, VISITED = 0, 1

    initial_x, initial_y = 0, 0

    if maze[initial_x][initial_y] == BLOCKED:
        return -1
    
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    height, width = len(maze), len(maze[0])

    target_x, target_y = height - 1, width - 1

    queue = deque([(initial_x, initial_y, 0)])
    if DEBUG: print("queue=", queue)

    # is_visited = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    is_visited = [[UNVISITED for w in range(width)] for h in range(height)]
    if DEBUG: print("is_visited=", is_visited)
    # is_visited = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    is_visited[initial_x][initial_y] = VISITED
    if DEBUG: print("is_visited=", is_visited)

    while queue:
        x, y, steps = queue.popleft()
        if DEBUG: print(x, y, steps)

        if x == target_x and y == target_y:
            return steps

        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy
            if DEBUG: print("new_x=", new_x, "new_y=", new_y)
            if DEBUG: print("queue=", queue)

            if not (0 <= new_x < height and 0 <= new_y < width):
                continue

            if maze[new_x][new_y] == ALLOWED and is_visited[new_x][new_y] == UNVISITED:
                queue.append((new_x, new_y, steps + 1))
                is_visited[new_x][new_y] = VISITED
                if DEBUG_2: print(maze_pos[new_x][new_y])

    return -1 

DEBUG = False
DEBUG_2 = True
# maze = [[1,0,0],
#         [1,1,1],
#         [0,1,1]]
maze = [[1,0,0],
        [1,1,1],
        [1,0,1]]
maze_pos = [[1,2,3],
            [4,5,6],
            [7,8,9]]
print("Step=", maze_search(maze))