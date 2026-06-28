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
            # MAIN MENU
            menu = Menu(self.window)
            menu_return = menu.run()
            if menu_return == MENU_BUTTONS[0]:  #NEW GAME
                #LEVEL 1
                level = Level(self.window, "Level1", menu_return)
                level_return, score = level.run()
                if level_return:  #COMPLETE LEVEL 1

                    #LEVEL 2
                    level = Level(self.window, "Level2", menu_return)
                    level_return, score = level.run()

                if not level_return:  #COLLISION LEVEL
                    go = GameOver(self.window, score)
                    go_return = go.run()
                    if go_return == GO_BUTTONS[0]:  #NEW GAME
                        continue  #RETURN TO MENU

                    elif go_return == GO_BUTTONS[1]:  #QUIT GAME
                        pygame.quit()
                        quit()
            elif menu_return == MENU_BUTTONS[1]:  #QUIT
                pygame.quit()
                quit()