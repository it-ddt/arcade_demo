"""Точка входа в программу."""

from collections.abc import Generator

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
        self.sounds = {}

        self.loader = self.load_assets()

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

    def load_assets(self) -> Generator[int]:
        """Загружает ассеты: текстуры и звуки."""
        percentage = 0
        img_extentions = ("png", "jpg", "jpeg")
        sound_extentions = ("mp3", "wav", "ogg")

        textures_names = utils.get_filenames(config.IMG_DIR, img_extentions)
        sounds_names = utils.get_filenames(config.SOUND_DIR, sound_extentions)

        load_step = round(100 / (len(textures_names) + len(sounds_names)))
        file_names = textures_names + sounds_names
        for file_name in file_names:
            name, extention = file_name.split(".")[0], file_name.split(".")[-1]
            if extention in img_extentions:
                self.textures[name] = arcade.load_texture(config.IMG_DIR / file_name)
            elif extention in sound_extentions:
                self.sounds[name] = arcade.load_sound(config.SOUND_DIR / file_name)
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
