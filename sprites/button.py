"""Модуль кликабельной кнопки."""

from collections.abc import Callable

import arcade


class Button(arcade.SpriteSolidColor):
    """Кнопка."""

    def __init__(
            self,
            x: int,
            y: int,
            width: int = 600,
            height: int = 100,
            color: arcade.color.Color = arcade.color.BABY_BLUE,
            text: str = "кнопка",
            action: Callable | None = None,
    ) -> None:
        """Создает кнопку с центром в x y."""
        super().__init__(width, height, x, y, color)
        self.action = action
        self.text = text
        self.label = arcade.Text(self.text, x, y, anchor_x="center", anchor_y="center", font_size=50)

    def on_click(self) -> None:
        """Вызов действия по ЛКМ."""
        self.action()

    def on_draw(self) -> None:
        """Рисует прямоугольник (спрайт) и текст."""
        arcade.draw_sprite(self)
        self.label.draw()
