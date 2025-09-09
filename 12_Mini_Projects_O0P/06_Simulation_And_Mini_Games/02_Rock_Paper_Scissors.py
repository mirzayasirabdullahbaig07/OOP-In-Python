"""
Rock Paper Scissors - OOP implementation using pygame

File: RockPaperScissors_Pygame_OOP.py
Requirements: pygame (install with `pip install pygame`)

Features:
- Object-oriented structure: Game, Button
- Player vs AI
- Simple clickable buttons for Rock, Paper, Scissors
- Displays AI choice and result (Win/Lose/Draw)
- Restart button

Run: python RockPaperScissors_Pygame_OOP.py

"""

import pygame
import sys
import random

# ----- Configuration -----
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
BG_COLOR = (30, 30, 30)
BUTTON_COLOR = (50, 50, 200)
BUTTON_HOVER = (70, 70, 220)
TEXT_COLOR = (255, 255, 255)
FPS = 60
CHOICES = ["Rock", "Paper", "Scissors"]

# ----- Button class -----
class Button:
    def __init__(self, rect: pygame.Rect, text: str, font: pygame.font.Font):
        self.rect = rect
        self.text = text
        self.font = font

    def draw(self, surface, mouse_pos):
        color = BUTTON_HOVER if self.rect.collidepoint(mouse_pos) else BUTTON_COLOR
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        txt = self.font.render(self.text, True, TEXT_COLOR)
        txt_rect = txt.get_rect(center=self.rect.center)
        surface.blit(txt, txt_rect)

    def is_clicked(self, pos) -> bool:
        return self.rect.collidepoint(pos)

# ----- Main Game class -----
class RockPaperScissorsGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Rock Paper Scissors - OOP (pygame)')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 40)
        self.large_font = pygame.font.SysFont(None, 50)
        self.running = True
        self.result = ""
        self.player_choice = None
        self.ai_choice = None
        # Buttons
        self.buttons = [
            Button(pygame.Rect(50, 300, 140, 50), "Rock", self.font),
            Button(pygame.Rect(230, 300, 140, 50), "Paper", self.font),
            Button(pygame.Rect(410, 300, 140, 50), "Scissors", self.font),
        ]
        self.restart_button = Button(pygame.Rect(230, 20, 140, 40), "Restart", self.font)

    def get_result(self, player: str, ai: str) -> str:
        if player == ai:
            return "Draw!"
        if (player == "Rock" and ai == "Scissors") or \
           (player == "Paper" and ai == "Rock") or \
           (player == "Scissors" and ai == "Paper"):
            return "You Win!"
        return "You Lose!"

    def handle_click(self, pos):
        if self.restart_button.is_clicked(pos):
            self.result = ""
            self.player_choice = None
            self.ai_choice = None
            return

        for btn in self.buttons:
            if btn.is_clicked(pos):
                self.player_choice = btn.text
                self.ai_choice = random.choice(CHOICES)
                self.result = self.get_result(self.player_choice, self.ai_choice)
                break

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        self.screen.fill(BG_COLOR)

        # Draw buttons
        for btn in self.buttons:
            btn.draw(self.screen, mouse_pos)
        self.restart_button.draw(self.screen, mouse_pos)

        # Display choices
        if self.player_choice:
            player_text = self.large_font.render(f'Player: {self.player_choice}', True, TEXT_COLOR)
            self.screen.blit(player_text, (50, 100))
        if self.ai_choice:
            ai_text = self.large_font.render(f'AI: {self.ai_choice}', True, TEXT_COLOR)
            self.screen.blit(ai_text, (50, 160))

        # Display result
        if self.result:
            result_text = self.large_font.render(self.result, True, TEXT_COLOR)
            self.screen.blit(result_text, (50, 220))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.handle_click(event.pos)

            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = RockPaperScissorsGame()
    game.run()
