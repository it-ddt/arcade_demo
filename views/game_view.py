"""Модуль представлений."""

from __future__ import annotations

import random
from typing import TYPE_CHECKING

import arcade

import config
import utils
from sprites import Player

if TYPE_CHECKING:
    from main import App


class GameView(arcade.View):
    """Представление геймплея."""

    window: App

    def __init__(self) -> None:
        """Конструктор класса.

        Создает спрайтлисты: все (для отрисовки), мыши (для столкновений);
        Создает спрайты: игрок и фон;
        Подгоняет фон к размеру окна (не оставляет пустых областей).
        """
        super().__init__()

        self.mice_spawn_interval = 1  # сек
        self.mice_spawn_timer = self.mice_spawn_interval

        self.mice_caught_counter = 0

        self.sprites_to_draw = arcade.SpriteList()
        self.mice = arcade.SpriteList()

        player_x = self.window.width // 2
        player_y = self.window.height // 2
        bg_x = self.window.width // 2
        bg_y = self.window.height // 2

        self.player = Player(player_x, player_y)

        bg_texture = arcade.load_texture(config.IMG_DIR / "background.png")
        bg = arcade.Sprite()
        bg.texture = bg_texture
        bg.center_x = bg_x
        bg.center_y = bg_y

        bg.scale = utils.get_scale(
            self.window.width,
            self.window.height,
            bg.texture.width,
            bg.texture.height,
        )

        self.sprites_to_draw.append(bg)
        self.sprites_to_draw.append(self.player)

        self.score = arcade.Text(
            str(self.mice_caught_counter),
            self.window.width // 2,
            int(self.window.height * 0.9),
            font_size=100,  # TODO: рассчитать от размера окна
            anchor_x="center",
            anchor_y="center",
        )

    def on_draw(self) -> None:
        """Очищает окно и рисует все спрайты."""
        self.clear()
        self.sprites_to_draw.draw()
        self.score.draw()
        arcade.draw_line(
            self.window.width // 2,
            self.window.height,
            self.window.width // 2,
            0,
            arcade.color.RED,
            line_width=5,
        )
        arcade.draw_line(
            0,
            self.window.height // 2,
            self.window.width,
            self.window.height // 2,
            arcade.color.RED,
            line_width=5,
        )

    def on_key_press(self, symbol: int, _: int) -> None:
        """Система ввода: нажатие клавиш."""
        if symbol == arcade.key.ESCAPE:
            self.window.show_menu()

        if symbol == arcade.key.D:
            self.player.d_x = 1
        if symbol == arcade.key.A:
            self.player.d_x = -1

        if symbol == arcade.key.W:
            self.player.d_y = 1
        if symbol == arcade.key.S:
            self.player.d_y = -1

    def on_key_release(self, symbol: int, _: int) -> None:
        """Система ввода: отпускание клавиш."""
        if symbol == arcade.key.D:
            self.player.d_x = 0
        if symbol == arcade.key.A:
            self.player.d_x = 0

        if symbol == arcade.key.W:
            self.player.d_y = 0
        if symbol == arcade.key.S:
            self.player.d_y = 0

    def on_update(self, delta_time: float) -> None:
        """Спавнит мышей, двигает игрока, удаляет пойманных мышей."""
        self.mice_spawn_timer += delta_time
        if self.mice_spawn_timer >= self.mice_spawn_interval:
            self.spawn_mice()
            self.mice_spawn_timer = 0
        self.player.move(delta_time)

        mice_caught: list[arcade.Sprite] = arcade.check_for_collision_with_list(
            self.player,
            self.mice,
        )
        for mouse in mice_caught:
            mouse.remove_from_sprite_lists()
            self.mice_caught_counter += 1
            self.score.text = str(self.mice_caught_counter)

    def spawn_mice(self) -> None:
        """Спавн мыши.

        Создает спрайт с текстурой в случайных координатах
        (отступ 10% от каждого края).
        """
        mouse = arcade.Sprite()
        mouse_texture = arcade.load_texture(config.IMG_DIR / "mouse.png")
        mouse.texture = mouse_texture
        mouse.center_x = random.randint(
            int(self.window.width * 0.1),
            int(self.window.width * 0.9),
        )
        mouse.center_y = random.randint(
            int(self.window.height * 0.1),
            int(self.window.height * 0.9),
        )
        mouse.scale = 0.1  # TODO: считать размер от размера окна
        self.sprites_to_draw.append(mouse)
        self.mice.append(mouse)
