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
            "",
            self.window.width // 2,
            self.window.height // 2,
            anchor_x="center",
            anchor_y="center",
            font_size=50,  # TODO: рассчитать от размера окна
        )
        self.text_objects.append(self.title)
        self.set_menu_text()

    def on_key_press(self, symbol: int, _: int) -> None:
        """Включает представление игры по ENTER."""
        if symbol == arcade.key.ENTER and self.window.views.get("game"):
            self.window.switch_view("game")
        elif symbol == arcade.key.ESCAPE:
            arcade.exit()
        elif symbol == arcade.key.M:
            self.window.sound_manager.toggle_mute()
            self.set_menu_text()
        elif symbol == arcade.key.N:
            self.window.start_new_game()
            self.set_menu_text()

    def set_menu_text(self) -> None:
        """Меняет текст в пунктах меню."""
        texts = [
            "N - новая игра",
            "ESC - выход",
        ]
        if self.window.sound_manager.is_mute:
            texts.append("M - включить звук")
        else:
            texts.append("М - выключить звук")

        if self.window.views.get("game"):
            texts.append("ENTER - продолжить")

        texts_str = ", ".join(texts)

        self.title.text = texts_str
