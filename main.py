"""Точка входа."""

import arcade

import config
from views import GameView, MenuView


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
        self.menu_view = MenuView()
        self.game_view = GameView()
        self.show_menu()
        arcade.run()

    def show_menu(self) -> None:
        """Включает представление меню."""
        self.show_view(self.menu_view)

    def show_game(self) -> None:
        """Включает представление игры."""
        self.show_view(self.game_view)


if __name__ == "__main__":
    App()
