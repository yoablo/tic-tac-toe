import pygame

X_SIZE = 70
WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

running = True

cell_width = WIDTH // 3
cell_height = HEIGHT // 3

X_size = X_SIZE
O_size = 100

X_width = 10
line_width = 10
circle_width = 10

# half the width and height of text
corrective_val_text_width_1 = 100
corrective_val_text_height_1 = 30

#font = pygame.font.SysFont(None, 60)
