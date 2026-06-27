#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Const import WIDTH, HEIGHT, MENU_BUTTONS, GO_BUTTONS
from code.level import Level
from code.menu import Menu
from code.gameover import GameOver


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIDTH, HEIGHT))

    def run(self):
        while True:
            # Menu principal
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_BUTTONS[0]:  # NEW GAME
                # Level 1
                level = Level(self.window, "Level1", menu_return)
                level_return, score = level.run()

                if level_return:  # completou Level 1
                    # Level 2
                    level = Level(self.window, "Level2", menu_return)
                    level_return, score = level.run()

                if not level_return:  # colidiu em qualquer level
                    go = GameOver(self.window, score)
                    go_return = go.run()

                    if go_return == GO_BUTTONS[0]:  # NEW GAME
                        continue  # volta pro topo do while, reinicia do menu
                    elif go_return == GO_BUTTONS[1]:  # QUIT GAME
                        pygame.quit()
                        quit()

            elif menu_return == MENU_BUTTONS[1]:  # QUIT
                pygame.quit()
                quit()