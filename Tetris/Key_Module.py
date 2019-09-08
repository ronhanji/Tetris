# A simple module to get user input allowing for backspace but not arrow keys or delete key
# Shown in a box in the middle of the screen,Only near the center of the screen is blitted to 
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
# colors and valid keys can be changed by changing the constants at the beginning of the program

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

BACKGROUND_COLOR = (0,0,0)
TEXT_COLOR = (255,255,255)
BOX_COLOR = (255,255,255)
VALID_KEYS = 'abcdefghijklmnopqrstuvwxyz 0123456789'
capsOn = False
font = pygame.font.match_font("arial")
scale = 20
#NOT PURE^^
def draw_text(surf, text, size, x, y, font, color=(255,255,255)):
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x,y)
    surf.blit(text_surface, text_rect)

def get_key():
  event = pygame.event.poll()
  if event.type == KEYDOWN:
    return event.key
  else:
    pass

def ask(screen):
  global capsOn, VALID_KEYS
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  enteringText = True
  while enteringText:
    screen.fill((0,0,0))
    draw_text(screen, 'Enter Name: {}'.format(''.join(current_string)),26,scale,scale*4,font)
    
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == K_LSHIFT or event.key == K_RSHIFT:
          capsOn = True
      
        if event.key == K_BACKSPACE:
          current_string = current_string[0:-1]
        if event.key == K_RETURN:
          enteringText = False
        if event.key == K_MINUS:
          current_string.append("_")
        if chr(event.key) in VALID_KEYS:
          inkeyLtr = chr(event.key)
          if capsOn:
            inkeyLtr = inkeyLtr.upper()
          current_string.append(inkeyLtr)
      if event.type == pygame.KEYUP:
        if event.key == K_LSHIFT or event.key == K_RSHIFT:
          capsOn = False
    pygame.display.flip()
  return ''.join(current_string)
