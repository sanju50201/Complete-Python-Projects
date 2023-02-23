import pygame


# Initialize Pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Puzzle Game")

# game loop

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()


# create a puzzle grid

puzzle_width = 4
puzzle_height = 4
tile_size = 100

puzzle_grid = [[0 for y in range(puzzle_height)] for x in range(puzzle_width)]

for x in range(puzzle_width):
    for y in range(puzzle_height):
        puzzle_grid[x][y] = pygame.Rect(
            x * tile_size, y * tile_size, tile_size, tile_size)


# draw the puzzle pieces on the screen

for x in range(puzzle_width):
    for y in range(puzzle_height):
        pygame.draw.rect(screen, (255, 255, 255), puzzle_grid[x][y], 1)

selected_piece = None

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            for x in range(puzzle_width):
                for y in range(puzzle_height):
                    if puzzle_grid[x][y].collidepoint(mouse_pos):
                        selected_piece = puzzle_grid[x][y]

        if event.type == pygame.MOUSEBUTTONUP:
            selected_piece = None

    if selected_piece is not None:
        mouse_pos = pygame.mouse.get_pos()
        selected_piece.center = mouse_pos

    screen.fill((0, 0, 0))

    for x in range(puzzle_width):
        for y in range(puzzle_height):
            pygame.draw.rect(screen, (255, 255, 255), puzzle_grid[x][y])

    pygame.display.update()

pygame.quit()
