"""Модуль приложения."""

import arcade
import pyglet

import config
from views import GameView, LoadView, MenuView

from .assets_manger import AssetsManager
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

        self.assets_manager = AssetsManager()
        self.sound_manager = SoundManager()

        self.loader = self.assets_manager.load_assets()
        self.views = {"load": LoadView()}
        self.switch_view("load")

        self.is_continue_game_button_visible = False

        arcade.run()

    def switch_view(self, view_name: str) -> None:
        """Включает представление."""
        view = self.views.get(view_name)
        if not view:
            error_message = f"Представление {view_name} не найдено."
            raise RuntimeError(error_message)
        self.show_view(view)

    def make_views(self) -> None:
        """Создает остальные представления."""
        views = {
            "menu": MenuView(),
            "game": GameView(),
        }
        self.views.update(views)

    def start_new_game(self) -> None:
        """Начинает новую игру."""
        self.views["game"].setup()
        self.is_continue_game_button_visible = True
        self.switch_view("game")

    def continue_game(self) -> None:
        """Продолжает игру."""
        self.switch_view("game")

    def on_setup(self) -> None:
        """Все ассеты загружены!."""
        all_sounds = self.assets_manager.sounds
        self.sound_manager.load_sounds(all_sounds)
        self.make_views()
        self.switch_view("menu")
        self.sound_manager.play_music()
