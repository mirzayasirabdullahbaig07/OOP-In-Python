"""
Typing Speed Test - OOP with pygame
-----------------------------------
Run: python typing_speed_test.py
"""

import pygame
import sys
import time
import random

# ----- Config -----
WIDTH, HEIGHT = 800, 400
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
INPUT_COLOR = (50, 50, 50)
RESULT_COLOR = (200, 200, 50)
FPS = 60

SENTENCES = [
    "Python is an amazing programming language",
    "Artificial intelligence is the future",
    "Data science involves statistics and coding",
    "Machine learning powers recommendation systems",
    "OpenAI creates advanced AI models"
]

# ----- Typing Test Class -----
class TypingSpeedTest:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Typing Speed Test (OOP)")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 28)
        self.big_font = pygame.font.SysFont("Arial", 36)

        self.reset_test()

    def reset_test(self):
        self.sentence = random.choice(SENTENCES)
        self.input_text = ""
        self.start_time = None
        self.wpm = 0
        self.accuracy = 0
        self.finished = False

    def calculate_results(self):
        if not self.start_time:
            return
        elapsed_time = max(time.time() - self.start_time, 1)
        words_typed = len(self.input_text.split())
        self.wpm = round((words_typed / elapsed_time) * 60)

        correct_chars = sum(1 for i, c in enumerate(self.input_text) if i < len(self.sentence) and c == self.sentence[i])
        self.accuracy = round((correct_chars / len(self.sentence)) * 100)

    def draw_text(self, text, pos, color=TEXT_COLOR, font=None):
        if font is None:
            font = self.font
        txt_surface = font.render(text, True, color)
        rect = txt_surface.get_rect(center=pos)
        self.screen.blit(txt_surface, rect)

    def run(self):
        running = True
        while running:
            self.screen.fill(BG_COLOR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN and not self.finished:
                    if not self.start_time:
                        self.start_time = time.time()

                    if event.key == pygame.K_RETURN:
                        self.finished = True
                        self.calculate_results()

                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]

                    else:
                        self.input_text += event.unicode

                elif event.type == pygame.KEYDOWN and self.finished:
                    if event.key == pygame.K_r:  # Restart
                        self.reset_test()

            # Draw sentence
            self.draw_text(self.sentence, (WIDTH // 2, 80), TEXT_COLOR, self.big_font)

            # Draw input box
            pygame.draw.rect(self.screen, INPUT_COLOR, (100, 150, WIDTH - 200, 50))
            self.draw_text(self.input_text, (WIDTH // 2, 175))

            # Results
            if self.finished:
                self.draw_text(f"WPM: {self.wpm}", (WIDTH // 2, 250), RESULT_COLOR, self.big_font)
                self.draw_text(f"Accuracy: {self.accuracy}%", (WIDTH // 2, 300), RESULT_COLOR, self.big_font)
                self.draw_text("Press R to Restart", (WIDTH // 2, 350), (200, 200, 200))

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    TypingSpeedTest().run()
