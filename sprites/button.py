"""Модуль кликабельной кнопки."""

from collections.abc import Callable

import arcade

import config


class Button(arcade.SpriteSolidColor):
    """Кнопка."""

    def __init__(
            self,
            x: int,
            y: int,
            color: arcade.color.Color = arcade.color.BABY_BLUE,
            text: str = "кнопка",
            action: Callable | None = None,
    ) -> None:
        """Создает кнопку.

        x y - центр
        Ширина = текстовй контент + горизонтальный отступ
        Высота = текстовй контент + вертикальный отступ
        """
        self.action = action
        self.text = text
        self.label = arcade.Text(
            self.text,
            x,
            y,
            anchor_x="center",
            anchor_y="center",
            font_size=50,
            font_name=config.FONT_BUTTON,
        )
        padding_x = 50
        padding_y = 25
        width = self.label.content_width + padding_x * 2
        height = self.label.content_height + padding_y * 2
        super().__init__(width, height, x, y, color)

    def on_click(self) -> None:
        """Вызов действия по ЛКМ."""
        self.action()

    def on_draw(self) -> None:
        """Рисует прямоугольник (спрайт) и текст."""
        arcade.draw_sprite(self)
        self.label.draw()
