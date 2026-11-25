"""Модуль текстового объекта с контуром."""

import arcade

import config


class TextOutlined(arcade.Text):
    """Текстовый объект с контуром."""

    def __init__(
            self,
            text: str,
            x: int,
            y: int,
            color: arcade.types.Color = arcade.color.WHITE,
            color_outline: arcade.types.Color = arcade.color.BLACK,
            thickness: int = 2,
            anchor_x: str = "center",
            anchor_y: str = "center",
            font_size: int = 12,
            font_name: str = config.FONT_TITLE,
    ) -> None:
        """Создает оконтуренный текстовый с центр в x y, контур толщиной thickness px."""
        super().__init__(
            text,
            x,
            y,
            color=color,
            font_size=font_size,
            anchor_x=anchor_x,
            anchor_y=anchor_y,
            font_name=font_name,
        )
        self.thickness = thickness
        self.outline = arcade.Text(
            text,
            x,
            y,
            color=color_outline,
            font_size=font_size,
            anchor_x=anchor_x,
            anchor_y=anchor_y,
            font_name=font_name,
        )

    def draw(self) -> None:
        """Сначала рисует контуры с отступами в 8 сторон, потом основной текст."""
        outline_coords = [
            (self.x + x * self.thickness, self.y + y * self.thickness)
            for x in range(-1, 2)
            for y in range(-1, 2)
            if x != 0 and y != 0
        ]
        for x, y in outline_coords:
            self.outline.x = x
            self.outline.y = y
            self.outline.draw()

        super().draw()

    @property
    def text(self) -> str:
        """Геттер основного текста."""
        return super().text

    @text.setter
    def text(self, value: str) -> None:
        """Сеттер основного текста и текста контура."""
        self._label.text = value
        self.outline.text = value
