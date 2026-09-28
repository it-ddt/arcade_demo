"""Модуль игрока."""

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
        self.speed = 200
        self.d_x = 0
        self.d_y = 0

    def move(self, delta_time: float) -> None:
        """Изменяет обе координаты на произведение направления и скорости."""
        self.center_x += self.d_x * self.speed * delta_time
        self.center_y += self.d_y * self.speed * delta_time
