import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 2180, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Riddle Master")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
BLUE = (0, 128, 255)
GREEN = (0, 200, 100)
RED = (255, 50, 50)

# Font
font = pygame.font.SysFont("comicsansms", 32)

# Fade effect
def fade_in(text, color, bg_color):
    for alpha in range(0, 255, 5):
        screen.fill(bg_color)
        surface = font.render(text, True, color)
        surface.set_alpha(alpha)
        screen.blit(surface, (WIDTH//2 - surface.get_width()//2, HEIGHT//2 - surface.get_height()//2))
        pygame.display.update()
        pygame.time.delay(30)

def fade_out():
    for alpha in range(255, 0, -5):
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(alpha)
        screen.blit(overlay, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)

# Riddles and answers
riddles = [
    ("I'm a thing which is in kitchens and also in bathrooms. What am I?", "sink"),
    ("I'm a thing which has keys but can't open locks. What am I?", "piano"),
    ("A thing which has hands but cannot clap. What am I?", "clock"),
    ("I'm tall when I'm young, and I'm short when I'm old. What am I?", "candle"),
    ("I am not alive, but I grow. I don’t have lungs, but I need air. I don’t have a mouth, but water kills me. What am I?", "fire"),
    ("You see me once in June, twice in November, but not at all in May. What am I?", "e"),
    ("The more you take, the more you leave behind. What am I?", "footsteps"),
    ("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", "echo"),
    ("You look at me, I look back. You speak, I mimic. But I never blink. What am I?", "mirror"),
    ("The more you pack me, the lighter I become. What am I?", "hole")
]

def show_message(message, color=WHITE, bg_color=BLACK, delay=2):
    screen.fill(bg_color)
    text_surface = font.render(message, True, color)
    screen.blit(text_surface, (WIDTH//2 - text_surface.get_width()//2, HEIGHT//2 - text_surface.get_height()//2))
    pygame.display.update()
    time.sleep(delay)

def ask_riddle(riddle, answer):
    fade_in(riddle, WHITE, PURPLE)
    user_input = ""
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_input.lower() == answer:
                        show_message("Correct! Well done.", GREEN)
                    else:
                        show_message("Incorrect. Try again.", RED)
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

        screen.fill(BLUE)
        riddle_surface = font.render(riddle, True, WHITE)
        input_surface = font.render("Your answer: " + user_input, True, WHITE)
        screen.blit(riddle_surface, (WIDTH//2 - riddle_surface.get_width()//2, HEIGHT//3))
        screen.blit(input_surface, (WIDTH//2 - input_surface.get_width()//2, HEIGHT//2))
        pygame.display.update()

# Game loop
fade_in("Welcome to Riddle Master!", WHITE, BLACK)
fade_in("Get ready to test your wits...", WHITE, BLACK)
fade_in("Press any key to begin!", WHITE, BLACK)

waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            waiting = False
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

for riddle, answer in riddles:
    ask_riddle(riddle, answer)
    fade_out()

show_message("Congratulations! You're a true Riddle Master!", WHITE, GREEN, delay=3)
show_message("Thank you for playing!", WHITE, BLACK, delay=3)
pygame.quit()