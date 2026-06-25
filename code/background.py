#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIDTH, BG1_SPEED
from code.entity import Entity


class Background(Entity):
    def __init__(self, name : str, position: tuple):
        super().__init__(name, position)
        pass

    def move(self, ):
        self.rect.centerx -= BG1_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIDTH
        pass
