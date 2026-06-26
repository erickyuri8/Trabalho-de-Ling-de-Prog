from code.Const import WIDTH
from code.background import Background
from code.player import Player
from code.obstacle import Obstacle


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):

        match entity_name:

            case "bg":
                list_bg = []

                for i in range(5):
                    list_bg.append(Background(f"bg{i}", position))
                    list_bg.append(Background(f"bg{i}", (WIDTH, 0)))

                return list_bg

            case "player":
                return Player("carp", position)

            case "dog":
                return Obstacle("dog", position, speed=10)

            case "cone":
                return Obstacle("cone", position, speed=11)

            case "capsule":
                return Obstacle("capsule", position, speed=10)

        raise ValueError(f"Entidade '{entity_name}' não existe.")