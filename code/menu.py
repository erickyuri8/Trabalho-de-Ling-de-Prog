#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, MENU_BUTTONS


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/menuback.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load("./asset/menusound.wav")
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "City Cars",(128, 255, 0), ((WIN_WIDTH / 2), 70)) #modificar tamanho e cor

            for i in range(len(MENU_BUTTONS)):
                self.menu_text(20, MENU_BUTTONS[i], (255, 255, 0), ((WIN_WIDTH / 2), 200 + 25 * i))  # modificar tamanho e cor

            pygame.display.flip()
            # Check for all events
            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                 pygame.quit() #close window
                 quit() #end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Mouse Memoirs", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
