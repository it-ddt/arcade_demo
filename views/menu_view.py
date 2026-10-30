"""Модуль представления меню."""

from __future__ import annotations

from functools import partial
from typing import TYPE_CHECKING

import arcade

if TYPE_CHECKING:
    from main import App

from sprites import Button

from .base_view import BaseView


class MenuView(BaseView):
    """Меню."""

    window: App


    def __init__(self) -> None:
        """Конструктор класса.

        Создает и показывает текст.
        """
        super().__init__("menu_bg")

        self.title = arcade.Text(
            "",
            self.window.width // 2,
            self.window.height // 2,
            anchor_x="center",
            anchor_y="center",
            font_size=50,  # TODO: рассчитать от размера окна
        )
        self.text_objects.append(self.title)
        self.make_buttons()

    def on_key_press(self, symbol: int, _: int) -> None:
        """Включает представление игры по ENTER."""
        if symbol == arcade.key.ENTER and self.window.views.get("game"):
            self.window.switch_view("game")
        elif symbol == arcade.key.ESCAPE:
            arcade.exit()
        elif symbol == arcade.key.M:
            self.window.sound_manager.toggle_mute()
            self.set_menu_text()
        elif symbol == arcade.key.N:
            self.window.start_new_game()

    def on_mouse_press(self, x: int, y: int, button: int, _: int) -> None:
        """Клик на кнопки."""
        if button != arcade.MOUSE_BUTTON_LEFT:
            return
        for button_sprite in self.buttons:
            if button_sprite.collides_with_point((x, y)):
                button_sprite.on_click()
                self.make_buttons()

    def make_buttons(self) -> None:
        """Создает кнопки."""
        self.buttons.clear()
        buttons_actions = {"новая игра": self.window.start_new_game}

        if self.window.sound_manager.volume > 0.0:
            buttons_actions["выключить звук"] = partial(
                setattr, self.window.sound_manager, "volume", 0.0,
            )
        else:
            buttons_actions["включить звук"] = partial(
                setattr, self.window.sound_manager, "volume", 1.0,
            )

        if self.window.views.get("game"):  # TODO: проверить стаус игры приложения
            buttons_actions["продолжить игру"] = self.window.continue_game

        buttons_actions["выйти"] = arcade.exit

        button_height = 100  # TODO: забрать из кнопки
        offset_y = button_height // 2
        x = self.window.width // 2

        total_buttons_height = (
            button_height * len(buttons_actions)
            + (len(buttons_actions) - 1)
            * offset_y
        )

        y = self.window.height // 2 + total_buttons_height // 2 - button_height // 2

        for text, action in buttons_actions.items():
            button = Button(x, y, text=text, action=action)
            self.buttons.append(button)
            y -= button.height + offset_y
