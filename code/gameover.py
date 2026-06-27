#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIDTH, HEIGHT, GO_BUTTONS


class GameOver:
    def __init__(self, window, score):
        self.window = window
        self.score = score

    def run(self):
        pygame.mixer.music.stop()
        selected = 0

        while True:
            self.window.fill((0, 0, 0))

            self.go_text(60, "GAME OVER", (255, 0, 0), (WIDTH / 2, HEIGHT / 2 - 80))
            self.go_text(20, f"Score: {int(self.score)}", (255, 255, 255), (WIDTH / 2, HEIGHT / 2 - 20))

            for i in range(len(GO_BUTTONS)):
                if i == selected:
                    self.go_text(22, GO_BUTTONS[i], (0, 255, 255), (WIDTH / 2, HEIGHT / 2 + 40 + 35 * i))
                else:
                    self.go_text(22, GO_BUTTONS[i], (255, 255, 0), (WIDTH / 2, HEIGHT / 2 + 40 + 35 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if selected < len(GO_BUTTONS) - 1:
                            selected += 1
                        else:
                            selected = 0

                    if event.key == pygame.K_UP:
                        if selected > 0:
                            selected -= 1
                        else:
                            selected = len(GO_BUTTONS) - 1

                    if event.key == pygame.K_RETURN:
                        return GO_BUTTONS[selected]

    def go_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Mouse Memoirs", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)