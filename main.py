"""Точка входа в программу."""

from _collections_abc import Generator

import arcade

import config
import utils
from views import GameView, LoadView, MenuView


class App(arcade.Window):
    """Окно: менеджер представлений."""

    def __init__(self) -> None:
        """Конструктор класса.

        Создает и показывает представление геймплея;
        Запускает главный цикл движка.
        """
        super().__init__(
            fullscreen=True,
            update_rate=1 / config.FPS,
            draw_rate=1 / config.FPS,
        )

        self.textures = {}
        self.loader = self.load_textures()

        # TODO: забрать классовый атрибут name от представлений
        self.views = {
            "load": LoadView(),
        }
        self.switch_view("load")

        arcade.run()

    def switch_view(self, view_name: str) -> None:
        """Включает представление."""
        view = self.views.get(view_name)
        if not view:
            error_message = f"Представление {view_name} не найдено."
            raise RuntimeError(error_message)
        self.show_view(view)

    def load_textures(self) -> Generator[int]:
        """Загружает текстуры."""
        percentage = 0
        extentions = (".png", ".jpg", ".jpeg")
        textures_names = utils.get_filenames(config.IMG_DIR, extentions)
        load_step = round(100 / len(textures_names))
        for name in textures_names:  # TODO: избавиться от расширений в ключах
            self.textures[name] = arcade.load_texture(config.IMG_DIR / name)
            percentage += load_step
            yield percentage

    def make_views(self) -> None:
        """Создает остальные представления."""
        views = {
            "menu": MenuView(),
            "game": GameView(),
        }
        self.views.update(views)


if __name__ == "__main__":
    App()
