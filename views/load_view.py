"""Модуль представления загрузки ассетов."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import App

import arcade


class LoadView(arcade.View):
    """Представление загрузки."""

    window: App

    def __init__(self) -> None:
        """Создает представление загрузки."""
        super().__init__()
        self.title_text = arcade.Text(
            "Загрузка текстур",
            self.window.width // 2,
            self.window.height // 2,
            font_size=50,
            anchor_x="center",
            anchor_y="center",
        )
        self.percentage_text = arcade.Text(
            "0",
            self.window.width // 2,
            round(self.window.height * 0.2),
            font_size=50,
            anchor_x="center",
            anchor_y="center",
        )

    def on_draw(self) -> None:
        """Отрисовывает заголовок."""
        self.clear()
        self.title_text.draw()
        self.percentage_text.draw()

    def on_update(self, delta_time) -> None:
        """Обновление счетчика загрузки."""
        try:
            self.percentage_text.text = str(next(self.window.loader))
        except StopIteration:  # Все текстуры загружены.
            self.percentage_text.text = "100"
            self.window.make_views()
            self.window.switch_view("menu")
