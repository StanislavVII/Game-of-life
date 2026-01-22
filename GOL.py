import pygame
import numpy as np
import time


pygame.init()


black, white = (0, 0, 0), (255, 255, 255)


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
max_iterations = int(input("Enter the maximum number of iterations: "))


width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life")


grid = np.random.choice([0, 1], size=(rows, cols))


def update_grid(grid):
    new_grid = grid.copy()

    for i in range(rows):
        for j in range(cols):
            neighbors = (
                grid[i - 1 : i + 2, j - 1 : j + 2].sum()
                - grid[i, j]
            )
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1

    return new_grid


def draw_button():
    pygame.draw.rect(screen, white, (width - 80, 10, 70, 30))
    font = pygame.font.Font(None, 30)
    text = font.render("Pause", True, black)
    screen.blit(text, (width - 75, 15))


running = True
paused = False
iteration_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if width - 80 <= x <= width - 10 and 10 <= y <= 40:
                paused = not paused

    if not paused:
        grid = update_grid(grid)
        iteration_count += 1

        if iteration_count >= max_iterations:
            paused = True


    screen.fill(black)
    cell_size = width // cols, height // rows
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                pygame.draw.rect(
                    screen, white, (j * cell_size[0], i * cell_size[1], cell_size[0], cell_size[1])
                )


    draw_button()


    pygame.display.flip()


    time.sleep(0.1)


pygame.quit()
