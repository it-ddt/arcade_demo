"""Модуль приложения."""

from collections.abc import Generator

import arcade
import pyglet

import config
import utils
from views import GameView, LoadView, MenuView

from .game import Game
from .sound_manager import SoundManager


class App(arcade.Window):
    """Окно: менеджер представлений."""

    def __init__(self) -> None:
        """Конструктор класса.

        Создает и показывает представление геймплея;
        Запускает главный цикл движка.
        """
        # убирает рваные края у текстовых объектов
        pyglet.options.dpi_scaling = "real"

        # выбирает второй экран
        display = pyglet.display.get_display()
        screens = display.get_screens()
        screen = screens[0]

        super().__init__(
            fullscreen=True,
            update_rate=1 / config.FPS,
            draw_rate=1 / config.FPS,
            screen=screen,
        )

        self.sound_manager = SoundManager()

        self.textures: dict[arcade.Texture] = {}

        self.loader = self.load_assets()

        self.game = Game()

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

        textures_names = utils.get_filenames(config.IMG_DIR, config.IMG_EXTENSIONS)
        sounds_names = utils.get_filenames(config.SOUND_DIR, config.SOUND_EXTENSIONS)

        assets_count = (len(textures_names) + len(sounds_names))
        if assets_count:
            load_step = round(100 / assets_count)
        else:
            load_step = 100
        file_names = textures_names + sounds_names
        for file_name in file_names:
            name, extention = file_name.split(".")[0], file_name.split(".")[-1]
            if extention in config.IMG_EXTENSIONS:
                self.textures[name] = arcade.load_texture(config.IMG_DIR / file_name)
            elif extention in config.SOUND_EXTENSIONS:
                sound = arcade.load_sound(config.SOUND_DIR / file_name)
                self.sound_manager.add_sound(name, sound)
            percentage += load_step
            yield percentage

    def make_views(self) -> None:
        """Создает остальные представления."""
        views = {
            "menu": MenuView(),
        }
        self.views.update(views)

    def start_new_game(self) -> None:
        """Начинает новую игру."""
        self.game.start_new_game()
        self.switch_view("game")

    def continue_game(self) -> None:
        """Продолжает игру."""

    def on_setup(self) -> None:
        """Все ассеты загружены!."""
        self.make_views()
        self.switch_view("menu")
        self.sound_manager.play_music()

