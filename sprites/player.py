"""Модуль игрока."""

import arcade

from .base_sprite import BaseSprite


class Player(BaseSprite):
    """Игрок."""

    def __init__(self, x: int, y: int, texture: arcade.Texture) -> None:
        """Конструктор класса.

        Задает текстуру, координаты, скорость и направления движения.
        """
        super().__init__(x, y, texture)
        self.motion_speed = 200
        self.rotation_speed = 100
        self.turn_direction = 0
        self.move_direction = 0

    def __str__(self) -> str:
        """Строковое представление."""
        return f"Мышь в {self.center_x} {self.center_y}"
