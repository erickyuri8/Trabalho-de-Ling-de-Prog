#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.entity import Entity


class Player(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)
        self.y_original = position[1]
        self.vel_y = 0
        self.gravity = 1.0
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.vel_y = -15
            self.is_jumping = True

    def move(self):
        if self.is_jumping:
            self.rect.y += self.vel_y
            self.vel_y += self.gravity

            if self.rect.y >= self.y_original:
                self.rect.y = self.y_original
                self.vel_y = 0
                self.is_jumping = False