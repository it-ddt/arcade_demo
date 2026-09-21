"""Модуль представления меню."""

from __future__ import annotations

from typing import TYPE_CHECKING

import arcade

if TYPE_CHECKING:
    from main import App


class MenuView(arcade.View):
    """Меню."""

    window: App


    def __init__(self) -> None:
        """Конструктор класса.

        Создает и показывает текст.
        """
        super().__init__()
        self.title = arcade.Text(
            "ENTER - сыграть, ESC - выход",
            self.window.width // 2,
            self.window.height // 2,
            anchor_x="center",
            anchor_y="center",
            font_size=50,  # TODO: рассчитать от размера окна
        )

    def on_draw(self) -> None:
        """Отрисовывает текст заголовка."""
        self.clear()
        self.title.draw()

    def on_key_press(self, symbol: int, _: int) -> None:
        """Включает представление игры по ENTER."""
        if symbol == arcade.key.ENTER:
            self.window.show_game()
        if symbol == arcade.key.ESCAPE:
            arcade.exit()
