"""
Tic Tac Toe - OOP implementation using pygame

File: TicTacToe_Pygame_OOP.py
Requirements: pygame (install with `pip install pygame`)

Features:
- Object-oriented structure: Board, Game, Button, AI
- Two-player (human vs human)
- Human vs Computer using Minimax (unbeatable)
- Clickable cells, Restart button, mode toggle
- Simple, commented and ready to run

Run: python TicTacToe_Pygame_OOP.py

"""

import pygame
import sys
import math
import random
from typing import List, Optional, Tuple

# ----- Configuration -----
SCREEN_SIZE = 600
GRID_SIZE = 3
LINE_WIDTH = 8
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 8
CROSS_WIDTH = 12
SPACE = 55
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (84, 84, 84)
BUTTON_COLOR = (50, 50, 50)
BUTTON_TEXT_COLOR = (255, 255, 255)
FPS = 60

# ----- Board class -----
class Board:
    def __init__(self, size: int = GRID_SIZE):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]

    def reset(self):
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]

    def place(self, row: int, col: int, symbol: str) -> bool:
        if self.grid[row][col] is None:
            self.grid[row][col] = symbol
            return True
        return False

    def available_moves(self) -> List[Tuple[int,int]]:
        return [(r,c) for r in range(self.size) for c in range(self.size) if self.grid[r][c] is None]

    def is_full(self) -> bool:
        return all(self.grid[r][c] is not None for r in range(self.size) for c in range(self.size))

    def check_winner(self) -> Optional[str]:
        # rows
        for r in range(self.size):
            if self.grid[r][0] and all(self.grid[r][c] == self.grid[r][0] for c in range(self.size)):
                return self.grid[r][0]
        # cols
        for c in range(self.size):
            if self.grid[0][c] and all(self.grid[r][c] == self.grid[0][c] for r in range(self.size)):
                return self.grid[0][c]
        # diag
        if self.grid[0][0] and all(self.grid[i][i] == self.grid[0][0] for i in range(self.size)):
            return self.grid[0][0]
        if self.grid[0][self.size-1] and all(self.grid[i][self.size-1-i] == self.grid[0][self.size-1] for i in range(self.size)):
            return self.grid[0][self.size-1]
        return None

# ----- Simple Button helper -----
class Button:
    def __init__(self, rect: pygame.Rect, text: str, font: pygame.font.Font):
        self.rect = rect
        self.text = text
        self.font = font

    def draw(self, surface):
        pygame.draw.rect(surface, BUTTON_COLOR, self.rect, border_radius=8)
        txt = self.font.render(self.text, True, BUTTON_TEXT_COLOR)
        txt_rect = txt.get_rect(center=self.rect.center)
        surface.blit(txt, txt_rect)

    def is_clicked(self, pos) -> bool:
        return self.rect.collidepoint(pos)

# ----- Minimax AI for unbeatable play -----
class MinimaxAI:
    def __init__(self, ai_symbol: str = 'O', human_symbol: str = 'X'):
        self.ai = ai_symbol
        self.human = human_symbol

    def evaluate(self, board: Board) -> int:
        winner = board.check_winner()
        if winner == self.ai:
            return 1
        elif winner == self.human:
            return -1
        return 0

    def minimax(self, board: Board, depth: int, is_maximizing: bool) -> int:
        score = self.evaluate(board)
        if score != 0 or board.is_full():
            return score

        if is_maximizing:
            best = -math.inf
            for (r, c) in board.available_moves():
                board.grid[r][c] = self.ai
                val = self.minimax(board, depth+1, False)
                board.grid[r][c] = None
                best = max(best, val)
            return best
        else:
            best = math.inf
            for (r, c) in board.available_moves():
                board.grid[r][c] = self.human
                val = self.minimax(board, depth+1, True)
                board.grid[r][c] = None
                best = min(best, val)
            return best

    def find_best_move(self, board: Board) -> Tuple[int,int]:
        best_val = -math.inf
        best_move = None
        for (r, c) in board.available_moves():
            board.grid[r][c] = self.ai
            move_val = self.minimax(board, 0, False)
            board.grid[r][c] = None
            if move_val > best_val:
                best_val = move_val
                best_move = (r, c)
        if best_move is None:
            # fallback to random
            return random.choice(board.available_moves())
        return best_move

# ----- Main Game class -----
class TicTacToeGame:
    def __init__(self, screen_size: int = SCREEN_SIZE):
        pygame.init()
        self.size = GRID_SIZE
        self.screen_size = screen_size
        self.cell_size = screen_size // self.size
        self.screen = pygame.display.set_mode((screen_size, screen_size + 80))
        pygame.display.set_caption('Tic Tac Toe - OOP (pygame)')
        self.clock = pygame.time.Clock()
        self.board = Board(self.size)
        self.current_player = 'X'
        self.running = True
        self.game_over = False
        self.font = pygame.font.SysFont(None, 30)
        self.large_font = pygame.font.SysFont(None, 40)
        self.ai_enabled = False
        self.ai = MinimaxAI(ai_symbol='O', human_symbol='X')
        # Buttons
        self.btn_restart = Button(pygame.Rect(20, screen_size + 20, 140, 40), 'Restart', self.font)
        self.btn_toggle = Button(pygame.Rect(180, screen_size + 20, 220, 40), 'Mode: Human vs Human', self.font)

    def draw_grid(self):
        self.screen.fill(BG_COLOR)
        # vertical lines
        for i in range(1, self.size):
            pygame.draw.line(self.screen, LINE_COLOR, (i * self.cell_size, 0), (i * self.cell_size, self.screen_size), LINE_WIDTH)
        # horizontal lines
        for i in range(1, self.size):
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * self.cell_size), (self.screen_size, i * self.cell_size), LINE_WIDTH)

    def draw_marks(self):
        for r in range(self.size):
            for c in range(self.size):
                center_x = c * self.cell_size + self.cell_size // 2
                center_y = r * self.cell_size + self.cell_size // 2
                mark = self.board.grid[r][c]
                if mark == 'O':
                    pygame.draw.circle(self.screen, CIRCLE_COLOR, (center_x, center_y), CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif mark == 'X':
                    # draw X
                    start_pos1 = (c * self.cell_size + SPACE, r * self.cell_size + SPACE)
                    end_pos1 = ((c+1) * self.cell_size - SPACE, (r+1) * self.cell_size - SPACE)
                    start_pos2 = (c * self.cell_size + SPACE, (r+1) * self.cell_size - SPACE)
                    end_pos2 = ((c+1) * self.cell_size - SPACE, r * self.cell_size + SPACE)
                    pygame.draw.line(self.screen, CROSS_COLOR, start_pos1, end_pos1, CROSS_WIDTH)
                    pygame.draw.line(self.screen, CROSS_COLOR, start_pos2, end_pos2, CROSS_WIDTH)

    def draw_ui(self):
        # Bottom panel background
        panel_rect = pygame.Rect(0, self.screen_size, self.screen_size, 80)
        pygame.draw.rect(self.screen, (40, 40, 40), panel_rect)
        # Buttons
        self.btn_restart.draw(self.screen)
        self.btn_toggle.draw(self.screen)
        # Status text
        status_text = 'Turn: ' + self.current_player if not self.game_over else 'Game Over'
        txt = self.large_font.render(status_text, True, (255,255,255))
        self.screen.blit(txt, (420, self.screen_size + 28))

    def cell_from_pos(self, pos) -> Optional[Tuple[int,int]]:
        x, y = pos
        if y >= self.screen_size:
            return None
        col = x // self.cell_size
        row = y // self.cell_size
        return (row, col)

    def handle_click(self, pos):
        if self.game_over:
            return
        # Buttons
        if self.btn_restart.is_clicked(pos):
            self.reset_game()
            return
        if self.btn_toggle.is_clicked(pos):
            self.ai_enabled = not self.ai_enabled
            self.btn_toggle.text = 'Mode: Human vs Computer' if self.ai_enabled else 'Mode: Human vs Human'
            self.reset_game()
            return

        cell = self.cell_from_pos(pos)
        if cell:
            r, c = cell
            if self.board.place(r, c, self.current_player):
                self._post_move()

    def _post_move(self):
        winner = self.board.check_winner()
        if winner or self.board.is_full():
            self.game_over = True
            return
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        self.board.reset()
        self.current_player = 'X'
        self.game_over = False

    def ai_move(self):
        if self.game_over or not self.ai_enabled:
            return
        if self.current_player == self.ai.ai:
            move = self.ai.find_best_move(self.board)
            if move:
                r, c = move
                self.board.place(r, c, self.ai.ai)
                self._post_move()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.handle_click(event.pos)

            # If AI enabled, let it make a move when it's its turn
            if self.ai_enabled and not self.game_over and self.current_player == self.ai.ai:
                # small delay so move appears natural
                pygame.time.delay(200)
                self.ai_move()

            self.draw_grid()
            self.draw_marks()
            self.draw_ui()

            # If there's a winner, draw a message
            if self.game_over:
                winner = self.board.check_winner()
                msg = 'Draw!'
                if winner:
                    msg = f'Winner: {winner}'
                overlay = pygame.Surface((self.screen_size, self.screen_size), pygame.SRCALPHA)
                overlay.fill((0,0,0,120))
                self.screen.blit(overlay, (0,0))
                text_surf = self.large_font.render(msg, True, (255,255,255))
                text_rect = text_surf.get_rect(center=(self.screen_size//2, self.screen_size//2))
                self.screen.blit(text_surf, text_rect)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = TicTacToeGame()
    game.run()
