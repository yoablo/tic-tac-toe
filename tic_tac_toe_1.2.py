import pygame

from constants import WIDTH, HEIGHT, SCREEN, CLOCK, CELL_WIDTH, CELL_HEIGHT, X_SIZE, O_SIZE, X_WIDTH, \
    LINE_WIDTH, CIRCLE_WIDTH, CORRECTIVE_VAL_TEXT_WIDTH_1, CORRECTIVE_VAL_TEXT_HEIGHT_1, FRAMERATE, SIZE_FONT, COLORS, \
    CELLS_AMMOUNT, CAPTION, BOARD_SIZE, AMMOUNT_TO_WIN


class TicTacToe:

    def __init__(self):

        pygame.init()

        self.width = WIDTH
        self.height = HEIGHT

        self.screen = SCREEN
        pygame.display.set_caption(CAPTION)

        self.clock = CLOCK

        self.running = True
        self.board_size = BOARD_SIZE
        self.ammount_to_win = AMMOUNT_TO_WIN
        self.cells_ammount = CELLS_AMMOUNT

        self.cell_width = CELL_WIDTH
        self.cell_height = CELL_HEIGHT

        self.X_size = X_SIZE
        self.O_size = O_SIZE

        self.X_width = X_WIDTH
        self.line_width = LINE_WIDTH
        self.circle_width = CIRCLE_WIDTH

        self.corrective_val_text_width_1 = CORRECTIVE_VAL_TEXT_WIDTH_1
        self.corrective_val_text_height_1 = CORRECTIVE_VAL_TEXT_HEIGHT_1

        self.font = pygame.font.SysFont(None, SIZE_FONT)
        self.Colors = COLORS

        self.frame_rate = FRAMERATE

        self.reset_game()

    def reset_game(self):

        self.is_game_over = False

        self.current_is_x = True

        self.board = [[None] * self.board_size for _ in range(self.board_size)]

    def game_over_won(self):

        text_surface = self.font.render(f"{'O' if self.current_is_x else 'X'} is winner", True,
                                        self.Colors.TEXT_COLOR.value)
        self.screen.blit(text_surface, (self.width // 2 - self.corrective_val_text_width_1,
                                        self.height // 2 - self.corrective_val_text_height_1))
        self.is_game_over = True

    def game_over_draw(self):
        is_draw = False
        cell_count = sum(cell is not None for row in self.board for cell in row)

        if cell_count == self.cells_ammount:
            text_surface = self.font.render("game over", True, self.Colors.TEXT_COLOR.value)
            self.screen.blit(text_surface, ((self.width / 2) - self.corrective_val_text_width_1,
                                            (self.height / 2) - self.corrective_val_text_height_1))
            is_draw = True

        return is_draw

    def cell_is_in_board(self, row, col):
        return 0 <= row < self.board_size and 0 <= col < self.board_size

    def check_cells_near(self, row, cell, move1, move2):
        counter = 1
        i = 1

        while (self.board[row][cell] is not None and self.cell_is_in_board(row + move1 * i, cell + move2 * i) and
               self.board[row][cell] == self.board[row + move1 * i][cell + move2 * i] and i != self.ammount_to_win):
            counter += 1
            i += 1

        return counter == self.ammount_to_win

    def diagonals_check(self, cell, row):
        found_winner = False

        if self.check_cells_near(row, cell, 1, 1) or \
                self.check_cells_near(row, cell, -1, 1) or \
                self.check_cells_near(row, cell, 1, -1) or \
                self.check_cells_near(row, cell, -1, -1):
            found_winner = True
            self.game_over_won()

        return found_winner

    def vertical_check(self, cell, row):
        found_winner = False

        if self.check_cells_near(row, cell, 1, 0):
            self.game_over_won()
            found_winner = True

        return found_winner

    def horizontal_check(self, cell, row):
        found_winner = False

        if self.check_cells_near(row, cell, 0, 1):
            self.game_over_won()
            found_winner = True

        return found_winner

    def game_logic(self):
        for row in range(self.board_size):
            for cell in range(self.board_size):
                if self.diagonals_check(cell, row) or \
                        self.vertical_check(cell, row) or \
                        self.horizontal_check(cell, row) or \
                        self.game_over_draw():
                    pass

    def draw_grid(self):

        start_pos = self.cell_width
        for position in range(self.board_size - 1):
            pygame.draw.line(self.screen, self.Colors.LINE_COLOR.value, (start_pos, 0), (start_pos, self.height),
                             self.line_width)
            start_pos += self.cell_width

        start_pos = self.cell_height
        for position in range(self.board_size - 1):
            pygame.draw.line(self.screen, self.Colors.LINE_COLOR.value, (0, start_pos), (self.width, start_pos),
                             self.line_width)
            start_pos += self.cell_height

    def draw_x(self, center):
        x, y = center

        pygame.draw.line(self.screen, self.Colors.X_COLOR.value, (x - self.X_size, y - self.X_size),
                         (x + self.X_size, y + self.X_size),
                         self.X_width)
        pygame.draw.line(self.screen, self.Colors.X_COLOR.value, (x + self.X_size, y - self.X_size),
                         (x - self.X_size, y + self.X_size),
                         self.X_width)

    def draw_circle(self, center):
        pygame.draw.circle(self.screen, self.Colors.O_COLOR.value, center, self.O_size, self.circle_width)

    def get_cell_center(self, row, col):
        center_x = col * self.cell_width + self.cell_width // 2
        center_y = row * self.cell_height + self.cell_height // 2

        return (center_x, center_y)

    def handle_click(self, pos):
        x, y = pos

        col = x // self.cell_width
        row = y // self.cell_height

        if self.board[row][col] is None:
            self.board[row][col] = f"{'X' if self.current_is_x else 'O'}"

            self.current_is_x = not self.current_is_x

    def show_current_player_sigh(self):
        text_surface = self.font.render(f"{'O' if not self.current_is_x else 'X'} is playing", True,
                                        self.Colors.TEXT_COLOR.value)

        self.screen.blit(text_surface, (0, 0))

    def draw_signs(self):

        for row in range(self.board_size):
            for col in range(self.board_size):

                value = self.board[row][col]

                if value is None:
                    continue

                center = self.get_cell_center(row, col)

                if value == "X":
                    self.draw_x(center)
                else:
                    self.draw_circle(center)

        if not self.is_game_over:
            self.show_current_player_sigh()

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
        self.screen.fill(self.Colors.BLACK.value)

        self.draw_grid()

        self.draw_signs()

        self.game_logic()

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()

            self.actions()

            self.clock.tick(self.frame_rate)

        pygame.quit()


game = TicTacToe()
game.run()
