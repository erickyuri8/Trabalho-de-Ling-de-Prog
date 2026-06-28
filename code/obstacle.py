import random
from code.entity import Entity
from code.Const import WIDTH

MIN_DISTANCE = 300  #MINIMUM DISTANCE BETWEEN OBSTACLES

class Obstacle(Entity):
    def __init__(self, name, position, speed=8):
        super().__init__(name, position)
        self.speed = speed
        self.all_obstacles = []  # OBSTACLES REFERENCE

    def move(self):
        self.rect.x -= self.speed #
        if self.rect.right < 0:
            self.rect.left = self._get_safe_spawn()

    def _get_safe_spawn(self):
        max_attempts = 20
        for _ in range(max_attempts):
            candidate = WIDTH + random.randint(100, 400) # DISTANCE BETWEEN THE OBSTACLES
            safe = True
            for other in self.all_obstacles:
                if other is self:
                    continue
                if abs(candidate - other.rect.left) < MIN_DISTANCE:
                    safe = False
                    break
            if safe:
                return candidate
        return WIDTH + 600 # SAFE DISTANCE IF DON'T FIND ANY DISTANCE