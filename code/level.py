#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code import menu
from code.Const import HEIGHT
from code.entity import Entity
from code.entityFactory import EntityFactory
import random


class Level:

    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20 segundos
        self.score = 0
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        # Background
        self.entity_list.extend(
            EntityFactory.get_entity("bg")
        )
        # Player
        self.player = EntityFactory.get_entity(
            "player",
            (10, 250)
        )
        self.entity_list.append(self.player)
        # Obstáculo
        tipo = random.choice(["dog", "cone", "capsule"])

        self.obstacles = [

            EntityFactory.get_entity("dog", (500, 280)),
            EntityFactory.get_entity("cone", (922, 280)),
            #EntityFactory.get_entity("capsule", (2900, 280))

        ]

        self.entity_list.extend(self.obstacles)

    def run(self):
        pygame.mixer_music.load("./asset/gamesound.wav")
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            # Atualiza tempo
            self.timeout -= clock.get_time()
            # Atualiza score
            self.score += clock.get_time() / 1000
            if self.timeout <= 0:
                print("GAME OVER")
                return menu
            # Limpa a tela
            self.window.fill((0, 0, 0))
            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
                        self.player.jump()

            # Atualiza entidades
            for ent in self.entity_list:
                ent.move()

            # Colisão
            for obstacle in self.obstacles:
                if self.player.rect.colliderect(obstacle.rect):
                    print("GAME OVER")
                    return menu #trocar aqui para retur gameover e apresentart

            # Desenha entidades
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)

            # Informações na tela
            self.level_text(
                15,
                f"Tempo: {self.timeout / 1000:.1f}s",
                (255, 255, 255),
                (70, 15)
            )

            self.level_text(
                15,
                f"FPS: {clock.get_fps():.0f}",
                (255, 255, 255),
                (45, 35)
            )

            self.level_text(
                15,
                f"Score: {int(self.score)}",
                (255, 255, 255),
                (55, 55)
            )

            pygame.display.flip()

    def level_text(self,
                   text_size: int,
                   text: str,
                   text_color: tuple,
                   text_pos: tuple):

        text_font: Font = pygame.font.SysFont(
            name="Mouse Memoirs",
            size=text_size
        )

        text_surf: Surface = text_font.render(
            text,
            True,
            text_color
        ).convert_alpha()

        text_rect: Rect = text_surf.get_rect(
            center=text_pos
        )

        self.window.blit(
            source=text_surf,
            dest=text_rect
        )