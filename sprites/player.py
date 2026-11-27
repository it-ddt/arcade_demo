"""Модуль игрока."""

import arcade

from .base_sprite import BaseSprite
from .text_outlined import TextOutlined


class Player(BaseSprite):
    """Игрок."""

    def __init__(self, x: int, y: int, texture: arcade.Texture) -> None:
        """Конструктор класса.

        Задает текстуру, координаты, скорость и направления движения.
        """
        super().__init__(x, y, texture)
        self.motion_speed = 2000
        self.rotation_speed = 100
        self.turn_direction = 0
        self.move_direction = 0
        self.hp = 100.0
        self.tag_hp = TextOutlined(
            str(self.hp),
            x,
            y,
        )

    def __str__(self) -> str:
        """Строковое представление."""
        return f"Игрок в {self.center_x} {self.center_y}"

    def update(self, delta_time: float) -> None:
        """Подтягивает тег к центру игрока."""
        super().update(delta_time)
        self.tag_hp.x = self.center_x
        self.tag_hp.y = self.center_y
        self.tag_hp.text = str(self.position)  # TODO: del on prod
