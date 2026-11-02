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
            height: int = 100,
            color: arcade.color.Color = arcade.color.BABY_BLUE,
            text: str = "кнопка",
            action: Callable | None = None,
    ) -> None:
        """Создает кнопку.

        x y - центр
        Ширина = текстовй контент + горизонтальный отступ
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
        padding_x = 100
        super().__init__(self.label.content_width + padding_x, height, x, y, color)


    def on_click(self) -> None:
        """Вызов действия по ЛКМ."""
        self.action()

    def on_draw(self) -> None:
        """Рисует прямоугольник (спрайт) и текст."""
        arcade.draw_sprite(self)
        self.label.draw()
