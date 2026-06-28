#!/usr/bin/python
# -*- coding: utf-8 -*-

from pygame import Surface, Rect
import pygame
import pygame.image
from code.Const import WIDTH, MENU_BUTTONS
from pygame.font import Font


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/menuback.png") #MENU BACKGROUND
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer.music.load("./asset/menusound.wav") #MENU MUSIC
        pygame.mixer.music.play(-1) #LOOP MUSIC
        menu_buttons = 0

        while True: #TEXTS OF MENU
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(65, "CITY JUMPING CAR", (26, 26, 26), (WIDTH / 2, 70))
            self.menu_text(15, "SPACE = Saltar", (255, 255, 255), (WIDTH / 2, 298))
            self.menu_text(15, "ESC = Sair", (255, 255, 255), (WIDTH / 2, 310))

            for i in range(len(MENU_BUTTONS)):
                if i == menu_buttons:
                    self.menu_text(35, MENU_BUTTONS[i], (129, 11, 233), (WIDTH / 2, 200 + 35 * i))
                else:
                    self.menu_text(35, MENU_BUTTONS[i], (241, 255, 0), (WIDTH / 2, 200 + 35 * i))

            pygame.display.flip()

            for event in pygame.event.get(): #QUIT EVENT TO CLOSE WINDOW
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN: #EVENT PRESS KEY TO DOWN
                    if event.key == pygame.K_DOWN:
                        if menu_buttons < len(MENU_BUTTONS) - 1:
                            menu_buttons += 1
                        else:
                            menu_buttons = 0

                    if event.key == pygame.K_UP: #EVENT PRESS KEY TO UP
                        if menu_buttons > 0:
                            menu_buttons -= 1
                        else:
                            menu_buttons = len(MENU_BUTTONS) - 1

                    if event.key == pygame.K_RETURN:#EVENT PRESS KEY TO ENTER
                        return MENU_BUTTONS[menu_buttons]

                    if event.key == pygame.K_ESCAPE: #EVENT PRESS KEY TO ESC
                        pygame.quit()
                        quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Mouse Memoirs", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)