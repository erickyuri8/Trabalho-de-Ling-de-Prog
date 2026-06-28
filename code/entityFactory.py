from code.Const import WIDTH
from code.background import Background
from code.player import Player
from code.obstacle import Obstacle


class EntityFactory:
    @staticmethod #STATIC METHOD TO CREATE ENTITY
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case "bg":
                list_bg = []
                for i in range(5): #ITERATIONS ABOUT THE FIVE FRAMES IN THE ASSET FILE
                    list_bg.append(Background(f"bg2{i}", position))
                    list_bg.append(Background(f"bg2{i}", (WIDTH, 0)))
                return list_bg
            case "bg2":
                list_bg = []
                for i in range(4): #ITERATIONS ABOUT THE FOUR FRAMES IN THE ASSET FILE
                    list_bg.append(Background(f"bg{i}", position))
                    list_bg.append(Background(f"bg{i}", (WIDTH, 0)))
                return list_bg
            case "player":
                return Player("carp", position)
            case "dog":
                return Obstacle("dog", position, speed=7) #OBSTACLE SPEED
            case "cone":
                return Obstacle("cone", position, speed=8) #OBSTACLE SPEED
            case "capsule":
                return Obstacle("capsule", position, speed=8) #OBSTACLE SPEED

        raise ValueError(f"Entity '{entity_name}' does not exist.")