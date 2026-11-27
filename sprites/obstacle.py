"""Модуль препятствия."""

import arcade


class Obstacle(arcade.SpriteSolidColor):
    """Препятствие."""

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        """Создает препятствие с центром в x y."""
        super().__init__(width, height, x, y)
