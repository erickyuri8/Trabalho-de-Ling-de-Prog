#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import mixer_music

from code.Const import WIDTH, HEIGHT, MENU_BUTTONS
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIDTH, HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_BUTTONS[0]:
                level = Level(self.window, "New game", menu_return)
                level_return = level.run()
            elif menu_return == MENU_BUTTONS[1]:
                pygame.quit()
                quit()
            else:
                pass


