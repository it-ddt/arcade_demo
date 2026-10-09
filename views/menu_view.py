"""Модуль представления меню."""

from __future__ import annotations

from typing import TYPE_CHECKING

import arcade

if TYPE_CHECKING:
    from main import App

from .base_view import BaseView


class MenuView(BaseView):
    """Меню."""

    window: App


    def __init__(self) -> None:
        """Конструктор класса.

        Создает и показывает текст.
        """
        super().__init__("menu_bg")

        self.title = arcade.Text(
            "ENTER - сыграть, ESC - выход, M - выключить звук",
            self.window.width // 2,
            self.window.height // 2,
            anchor_x="center",
            anchor_y="center",
            font_size=50,  # TODO: рассчитать от размера окна
        )
        self.text_objects.append(self.title)

    def on_key_press(self, symbol: int, _: int) -> None:
        """Включает представление игры по ENTER."""
        if symbol == arcade.key.ENTER:
            self.window.switch_view("game")
        elif symbol == arcade.key.ESCAPE:
            arcade.exit()
        elif symbol == arcade.key.M:
            is_mute = self.window.sound_manager.toggle_mute()
            if is_mute:
                self.title.text = "ENTER - сыграть, ESC - выход, M - включить звук"
            else:
                self.title.text = "ENTER - сыграть, ESC - выход, M - выключить звук"
