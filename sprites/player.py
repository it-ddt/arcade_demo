"""Модуль игрока."""

import math

import arcade


class Player(arcade.Sprite):
    """Игрок."""

    def __init__(self, x: int, y: int, texture: arcade.Texture) -> None:
        """Конструктор класса.

        Задает текстуру, координаты, скорость и направления движения.
        """
        super().__init__()
        self.texture = texture
        self.center_x = x
        self.center_y = y
        self.motion_speed = 200
        self.rotation_speed = 100
        self.turn_direction = 0
        self.move_direction = 0

    def update(self, delta_time: float) -> None:
        """Обновление.

        Перемещение и поворот.
        """
        self.angle += self.turn_direction * self.rotation_speed * delta_time
        angle_rad = math.radians(self.angle)
        self.center_x += math.sin(angle_rad) * self.move_direction * self.motion_speed * delta_time
        self.center_y += math.cos(angle_rad) * self.move_direction * self.motion_speed * delta_time
