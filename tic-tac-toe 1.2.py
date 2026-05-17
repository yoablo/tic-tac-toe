import pygame

from constants import WIDTH, HEIGHT, screen, clock, running, cell_width, cell_height, X_size, O_size, X_width, \
    line_width, circle_width, corrective_val_text_width_1, corrective_val_text_height_1


class TicTacToe:

    def __init__(self):

        pygame.init()

        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.screen = screen
        pygame.display.set_caption("Tic Tac Toe")

        self.clock = clock

        self.running = running  #

        self.cell_width = cell_width
        self.cell_height = cell_height

        self.X_size = X_size
        self.O_size = O_size

        self.X_width = X_width
        self.line_width = line_width
        self.circle_width = circle_width

        # half the width and height of text
        self.corrective_val_text_width_1 = corrective_val_text_width_1
        self.corrective_val_text_height_1 = corrective_val_text_height_1

        self.font = pygame.font.SysFont(None, 60)

        self.reset_game()

    def reset_game(self):

        self.is_game_over = False

        self.current_is_x = True

        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

    def game_over_won(self):

        text_surface = self.font.render(f"{'O' if self.current_is_x else 'X'} is winner", True, "yellow")
        self.screen.blit(text_surface, (self.WIDTH / 2 - self.corrective_val_text_width_1,
                                        self.HEIGHT / 2 - self.corrective_val_text_height_1))
        self.is_game_over = True
        return

    def game_logic(self):

        cell_count = 0

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != None or self.board[0][2] == self.board[1][1] == \
                self.board[2][0] != None:
            self.game_over_won()

        elif self.board[0][0] == self.board[1][0] == self.board[2][0] != None or self.board[0][1] == self.board[1][1] == \
                self.board[2][1] != None or self.board[0][2] == self.board[1][2] == self.board[2][2] != None:
            self.game_over_won()

        else:
            for row in self.board:
                if row[0] == row[1] == row[2] != None:
                    self.game_over_won()

                else:
                    for cell in row:
                        if cell is not None:
                            cell_count = cell_count + 1

                    if cell_count == 9:
                        text_surface = self.font.render("game over", True, "yellow")
                        self.screen.blit(text_surface, (self.WIDTH / 2 - self.corrective_val_text_width_1,
                                                        self.HEIGHT / 2 - self.corrective_val_text_height_1))

    def draw_grid(self):

        pygame.draw.line(self.screen, "white", (self.cell_width, 0), (self.cell_width, self.HEIGHT), self.line_width)
        pygame.draw.line(self.screen, "white", (self.cell_width * 2, 0), (self.cell_width * 2, self.HEIGHT),
                         self.line_width)
        pygame.draw.line(self.screen, "white", (0, self.cell_height), (self.WIDTH, self.cell_height), self.line_width)
        pygame.draw.line(self.screen, "white", (0, self.cell_height * 2), (self.WIDTH, self.cell_height * 2),
                         self.line_width)

    def draw_x(self, center):

        x, y = center

        pygame.draw.line(self.screen, "red", (x - self.X_size, y - self.X_size), (x + self.X_size, y + self.X_size),
                         self.X_width)
        pygame.draw.line(self.screen, "red", (x + self.X_size, y - self.X_size), (x - self.X_size, y + self.X_size),
                         self.X_width)

    def draw_circle(self, center):

        pygame.draw.circle(self.screen, "blue", center, self.O_size, self.circle_width)

    def get_cell_center(self, row, col):

        center_x = col * self.cell_width + self.cell_width // 2
        center_y = row * self.cell_height + self.cell_height // 2

        return (center_x, center_y)

    def handle_click(self, pos):

        x, y = pos

        col = x // self.cell_width
        row = y // self.cell_height

        # Prevent overwriting
        if self.board[row][col] is not None:
            return

        if self.current_is_x:
            self.board[row][col] = "X"
        else:
            self.board[row][col] = "O"

        self.current_is_x = not self.current_is_x

    def draw_signs(self):

        for row in range(3):
            for col in range(3):

                value = self.board[row][col]

                if value is None:
                    continue

                center = self.get_cell_center(row, col)

                if value == "X":
                    self.draw_x(center)
                else:
                    self.draw_circle(center)

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if not self.is_game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                self.running = False
            if keys[pygame.K_r]:
                self.reset_game()

    def actions(self):

        self.screen.fill("black")

        self.draw_grid()

        self.draw_signs()

        self.game_logic()

        pygame.display.flip()

    def run(self):

        while self.running:
            self.handle_events()

            self.actions()

            self.clock.tick(60)

        pygame.quit()


game = TicTacToe()
game.run()
