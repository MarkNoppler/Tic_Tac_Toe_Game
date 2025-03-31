"""
What it is:
A two player text-based Tic Tac Toe game with a GUI using Pygame

How to use it:
Run the code for the game screen to appear. The first player will be the X. Press on one of the cells in the 3x3 grid to
apply an X mark. This then applies to the O mark. The first to get 3 values in a row wins.

Documentation:
https://www.pygame.org/docs/

Made by Jacob Fairhurst
"""

#imports
import pygame
import sys
from typing import Optional

pygame.init()

#Constants. Square size = 600/3, circle radius square / 3
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
FONT = pygame.font.Font(None, 36)


class TicTacToe:
    """
    Class containing all set up for the Tic Tac Toe in Pygame
    """
    def __init__(self):
        """
        Initialise the game and display.
        """
        #pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic-Tac-Toe: (Use R key to restart.)")
        self.screen.fill(WHITE)
        self.board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]
        self.current_player = "X"
        self.draw_grid()
        self.running = True

    def draw_grid(self) -> None:
        """
        Draws the grid on screen iterating through rows.
        """
        for row in range(1, BOARD_ROWS):
            pygame.draw.line(self.screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
        for col in range(1, BOARD_COLS):
            pygame.draw.line(self.screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.display.update()

    def mark_square(self, row: int, col: int) -> bool:
        """
        Marks a square with the corresponding player's symbol.

        :param row: Each row cell on the grid
        :param col: Each column cell on the grid

        :return: Boolean. True if move is valid, False if not
        """
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def draw_figures(self) -> None:
        """
        Draws the players X or O on the screen
        """
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == "O":
                    pygame.draw.circle(self.screen, CIRCLE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif self.board[row][col] == "X":
                    start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                    end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                    pygame.draw.line(self.screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
                    start_asc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                    end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
                    pygame.draw.line(self.screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
        pygame.display.update()

    def check_winner(self) -> Optional[str]:
        """
        Checks for a winner comparing cells in a line across columns, rows or diagonally
        :return: None if no winner is found. Returns the winning player's symbol ("X" or "O") if a winner is found.
        """
        for row in range(BOARD_ROWS):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] and self.board[row][0] is not None:
                return self.board[row][0]
        for col in range(BOARD_COLS):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] is not None:
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return self.board[0][2]
        return None

    def display_winner(self, winner: str) -> None:
        """
        Display a winner message to the user
        :param winner: The winner (either 'X' or 'O')
        :return: None
        """
        message = f"{winner} Wins! --- (Press the R key to play again.)"
        text = FONT.render(message, True, (0, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.fill((255, 255, 255))
        self.screen.blit(text, text_rect)
        pygame.display.update()

    def restart(self) -> None:
        """
        Restarts the game by clearing the board and going back to the first player's turn.

        This method resets the game board, sets the current player to "X", and re-enables
        the game to be played again by setting the `running` flag to True.

        :return: None
        """
        self.screen.fill(WHITE)
        self.draw_grid()
        self.board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]
        self.current_player = "X"
        self.running = True

    def mainloop(self) -> None:
        """
        Logic for the game main loop to update the game state and handle cursor inputs
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and self.running:
                    x, y = event.pos
                    row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
                    if self.mark_square(row, col):
                        self.draw_figures()
                        winner = self.check_winner()
                        if winner:
                            pygame.time.wait(1500)
                            self.display_winner(winner)
                            print(f"{winner} wins!")
                            self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.restart()


#run the programme
if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop()