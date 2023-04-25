import pygame
import time
import heapq

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the size of the maze
MAZE_SIZE = (400, 400)

# Define the size of each cell in the maze
CELL_SIZE = 20

# Define the maze
MAZE = [[0 for j in range(MAZE_SIZE[1] // CELL_SIZE)] for i in range(MAZE_SIZE[0] // CELL_SIZE)]
MAZE_START = (0, 0)
MAZE_END = (MAZE_SIZE[0] // CELL_SIZE - 1, MAZE_SIZE[1] // CELL_SIZE - 1)

# Define the A* search algorithm
def a_star_search(graph, start, end):
    # Initialize the frontier and the explored set
    frontier = [(0, start)]
    explored = set()

    # Initialize the cost and the parent dictionaries
    cost = {start: 0}
    parent = {start: None}

    while frontier:
        # Get the node with the lowest cost from the frontier
        _, current = heapq.heappop(frontier)

        # If we have reached the goal, we're done
        if current == end:
            break

        # Add the current node to the explored set
        explored.add(current)

        # Loop over the neighbors of the current node
        for neighbor in graph[current]:
            # If the neighbor is already explored, skip it
            if neighbor in explored:
                continue

            # Calculate the tentative cost to reach the neighbor
            tentative_cost = cost[current] + 1

            # If the neighbor is not in the frontier, or the tentative cost is lower than the current cost, add it to the frontier
            if neighbor not in cost or tentative_cost < cost[neighbor]:
                cost[neighbor] = tentative_cost
                priority = tentative_cost + distance(neighbor, end)
                heapq.heappush(frontier, (priority, neighbor))
                parent[neighbor] = current

    # Return the path from the start to the end
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    return path

# Define the distance function for the A* search algorithm
def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Initialize the Pygame library
pygame.init()

# Set the size of the screen
screen_size = (MAZE_SIZE[0] + 1, MAZE_SIZE[1] + 1)
screen = pygame.display.set_mode(screen_size)

# Set the caption of the screen
pygame.display.set_caption("Maze Solver")

# Set the font of the text
font = pygame.font.SysFont(None, 24)

# Set the clock of the game
clock = pygame.time.Clock()

# Define the main loop of the game
def main_loop():

    while True:
        # ...
        # Update the Pygame window
        pygame.display.flip()
        
    # Initialize the game
    pygame.init()
    # Define the window size
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 700

    # Set the window size
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # Set the window title
    pygame.display.set_caption("Maze Solver")
    running = True
    start_time = time.time()
    solved = False

    # Create the graph of the maze
    graph = {}
    for i in range(MAZE_SIZE[0] // CELL_SIZE):
        for j in range(MAZE_SIZE[1] // CELL_SIZE):
            if MAZE[i][j] == 0:
                graph[(i, j)] = []
            if i > 0 and MAZE[i - 1][j] == 0:
                graph[(i, j)].append((i - 1, j))
            if i < MAZE_SIZE[0] // CELL_SIZE - 1 and MAZE[i + 1][j] == 0:
                graph[(i, j)].append((i + 1, j))
            if j > 0 and MAZE[i][j - 1] == 0:
                graph[(i, j)].append((i, j - 1))
            if j < MAZE_SIZE[1] // CELL_SIZE - 1 and MAZE[i][j + 1] == 0:
                graph[(i, j)].append((i, j + 1))

    # Find the path from the start to the end using the A* search algorithm
    path = a_star_search(graph, MAZE_START, MAZE_END)

    # Loop until the game is over
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the maze
    for i in range(MAZE_SIZE[0] // CELL_SIZE):
        for j in range(MAZE_SIZE[1] // CELL_SIZE):
            if MAZE[i][j] == 0:
                pygame.draw.rect(screen, BLACK, (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw the start and end cells
    pygame.draw.rect(screen, GREEN, (MAZE_START[0] * CELL_SIZE, MAZE_START[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (MAZE_END[0] * CELL_SIZE, MAZE_END[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw the path
    if not solved:
        for i in range(len(path) - 1):
            pygame.draw.line(screen, BLUE, (path[i][0] * CELL_SIZE + CELL_SIZE // 2, path[i][1] * CELL_SIZE + CELL_SIZE // 2), (path[i + 1][0] * CELL_SIZE + CELL_SIZE // 2, path[i + 1][1] * CELL_SIZE + CELL_SIZE // 2), 3)
        solved = True

    # Draw the text
    elapsed_time = int(time.time() - start_time)
    text = font.render("Elapsed Time: {} seconds".format(elapsed_time), True, BLACK)
    screen.blit(text, (10, 10))

    # Update the screen
    pygame.display.update()

    # Tick the clock
    clock.tick(60)

# Quit the game
pygame.quit()


# Call the main loop of the game
if __name__ == "__main__":
    main_loop()


