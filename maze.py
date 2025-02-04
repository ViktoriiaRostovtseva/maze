import pygame
import random

# Maze dimensions
WIDTH, HEIGHT = 21, 21  
CELL_SIZE = 30  
WINDOW_SIZE = WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create maze
maze = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Maze generation
def generate_maze(x, y):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    random.shuffle(directions)
    
    for dx, dy in directions:
        nx, ny = x + dx * 2, y + dy * 2
        if 0 < nx < WIDTH and 0 < ny < HEIGHT and maze[ny][nx] == 0:
            maze[y + dy][x + dx] = 1  
            maze[ny][nx] = 1
            generate_maze(nx, ny)

# Start generation
maze[1][1] = 1
generate_maze(1, 1)

# Player
player_x, player_y = 1, 1  #start
goal_x, goal_y = WIDTH - 2, HEIGHT - 2  #finish

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Maze Game")

def draw_maze():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            color = WHITE if maze[y][x] == 1 else BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.draw.circle(screen, BLUE, (player_x * CELL_SIZE + CELL_SIZE // 2, player_y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
    pygame.draw.rect(screen, GREEN, (goal_x * CELL_SIZE, goal_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def move_player(keys):
    global player_x, player_y
    dx, dy = 0, 0

    if keys[pygame.K_LEFT]:
        dx = -1
    if keys[pygame.K_RIGHT]:
        dx = 1
    if keys[pygame.K_UP]:
        dy = -1
    if keys[pygame.K_DOWN]:
        dy = 1    
    new_x, new_y = player_x + dx, player_y + dy
    if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT and maze[new_y][new_x] == 1:
        player_x, player_y = new_x, new_y

def main():
    global player_x, player_y
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)
        draw_maze()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        move_player(keys)
            
        if player_x == goal_x and player_y == goal_y:
            print("You win!")
            running = False  

        clock.tick(10)  

    pygame.quit()

if __name__ == "__main__":
    main()
