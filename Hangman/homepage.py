import pygame
import sys 
import random

# initialize pygame
pygame.init()

# initialize pygame mixer
pygame.mixer.init()



#create a pygame display surface
WIDTH = 850
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# COLORS 
WHITE = (255, 255, 255)
BLUE = (30, 144,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (168, 169, 169)

#background image
bg_img = pygame.image.load("hangman_top.png")
SCREEN.blit(bg_img, (0,0))


#background music
pygame.mixer.music.load("Sounds/bg_music.mp3")
pygame.mixer.music.play(-1)

# SOUNDS ***********************************************************************
win_fx = pygame.mixer.Sound("Sounds/win.wav")
lose_fx = pygame.mixer.Sound("Sounds/lose.wav")

#object
class Buttons:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.SysFont("cursive", 40)
        self.is_hovered = False
        
    def make(self, screen):
        if self.is_hovered:
            color = BLUE
        else:
            color = RED
        pygame.draw.rect(screen, color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, (self.rect.centerx - text_surface.get_width() // 2, self.rect.centery - text_surface.get_height() // 2))

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)


clock = pygame.time.Clock()
FPS = 60

#button
start_button = Buttons(325, 325, 200, 50, "Start Game")
quit_button = Buttons(325, 400, 200, 50, "Quit")

#game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
   
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start_button.is_clicked(mouse_pos):
                #Game start
                pygame.mixer.music.stop()
                running = False
                
            elif quit_button.is_clicked(mouse_pos):
                #quit the game
                running = True

    mouse_pos = pygame.mouse.get_pos()
    start_button.check_hover(mouse_pos)
    quit_button.check_hover(mouse_pos)
          
    start_button.make(SCREEN)
    quit_button.make(SCREEN)
    clock.tick(FPS)
    pygame.display.update()
pygame.quit() 
