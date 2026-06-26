import random
from code.entity import Entity
from code.Const import WIDTH


class Obstacle(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)

        self.speed = 8

    def move(self):

        self.rect.x -= self.speed

        if self.rect.right < 0:

            self.rect.left = WIDTH + random.randint(100, 300)