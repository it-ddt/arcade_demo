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
            thickness: int = 2,  # TODO: считать от font_size?
            anchor_x: str = "center",
            anchor_y: str = "center",
            font_size: int = 12,
            font_name: str = config.FONT_TITLE,
    ) -> None:
        """Создает оконтуренный текстовый с центом в x y с контуром толщиной thickness px."""
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
        """Сначала рисует контур с отступами в 4 стороны, потом основной текст."""
        self.outline.x = self.x + self.thickness
        self.outline.draw()
        self.outline.x = self.x - self.thickness
        self.outline.draw()
        self.outline.x = self.x

        self.outline.y = self.y + self.thickness
        self.outline.draw()
        self.outline.y = self.y - self.thickness
        self.outline.draw()
        self.outline.y = self.y

        # TODO: подвигать по 4 диагоналям

        super().draw()
