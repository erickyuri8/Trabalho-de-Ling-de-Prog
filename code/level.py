#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import HEIGHT
from code.entity import Entity
from code.entityFactory import EntityFactory

class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 15000 #GAME TIME
        self.score = 0 #INITIAL SCORE
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        if self.name == "Level1": #BG LEVELS
            self.entity_list.extend(EntityFactory.get_entity("bg"))
        elif self.name == "Level2":
            self.entity_list.extend(EntityFactory.get_entity("bg2"))
        self.player = EntityFactory.get_entity("player", (10, 250))
        self.entity_list.append(self.player)
        # OBSTACLES
        self.obstacles = [
            EntityFactory.get_entity("dog",     (600,  280)),
            EntityFactory.get_entity("cone",    (1100, 280)),
            EntityFactory.get_entity("capsule", (1600, 280)),
        ]
        for obs in self.obstacles:
            obs.all_obstacles = self.obstacles
        self.entity_list.extend(self.obstacles)

    def run(self):
        pygame.mixer.music.load("./asset/gamesound.wav") #LEVEL MUSICS
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        while True:
            dt = clock.tick(60) #FPS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()
            self.timeout -= dt
            self.score += dt / 1000
            if self.timeout <= 0:
                return True, self.score
            self.window.fill((0, 0, 0))
            for ent in self.entity_list:
                ent.move()
            for obstacle in self.obstacles:
                if self.player.rect.colliderect(obstacle.rect): #COLLISION IN THE OBSTACLES
                    return False, self.score
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
            #INFORMATION ABOUT THE LEVEL, LIKE: TIME, FPS, SCORE AND THE SPECIFIC LEVEL
            self.level_text(20, f"Tempo: {self.timeout / 1000:.1f}s", (255, 255, 255), (45, 15))
            self.level_text(15, f"FPS: {clock.get_fps():.0f}", (255, 255, 255), (30, 35))
            self.level_text(15, f"Score: {int(self.score)}", (255, 255, 255), (30, 55))
            self.level_text(15, self.name, (255, 255, 255), (30, 75))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Mouse Memoirs", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)