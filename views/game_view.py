"""Модуль представлений."""

import random

import arcade

from .base_view import BaseView


class GameView(BaseView):
    """Представление геймплея."""

    def __init__(self) -> None:
        """Конструктор класса.

        Создает спрайтлисты: все (для отрисовки), мыши (для столкновений);
        Создает спрайты: игрок и фон;
        Подгоняет фон к размеру окна (не оставляет пустых областей).
        """
        super().__init__("game_bg")

    def on_key_press(self, symbol: int, _: int) -> None:
        """Система ввода: нажатие клавиш."""
        if symbol == arcade.key.ESCAPE:
            self.window.switch_view("menu")

        if symbol == arcade.key.D:
            self.player.turn_direction = 1
        if symbol == arcade.key.A:
            self.player.turn_direction = -1

        if symbol == arcade.key.W:
            self.player.move_direction = 1
        if symbol == arcade.key.S:
            self.player.move_direction = -1

    def on_key_release(self, symbol: int, _: int) -> None:
        """Система ввода: отпускание клавиш."""
        if symbol == arcade.key.D:
            self.player.turn_direction = 0
        if symbol == arcade.key.A:
            self.player.turn_direction = 0

        if symbol == arcade.key.W:
            self.player.move_direction = 0
        if symbol == arcade.key.S:
            self.player.move_direction = 0
