"""Модуль представлений."""

import random

import arcade

from sprites import Player

from .base_view import BaseView


class GameView(BaseView):
    """Представление геймплея."""

    def __init__(self) -> None:
        """Конструктор класса.

        Создает спрайтлисты: все (для отрисовки), мыши (для столкновений);
        Создает спрайты: игрок и фон;
        Подгоняет фон к размеру окна (не оставляет пустых областей).
        """
        super().__init__("game_bg")

        self.mice_spawn_interval = 1  # сек
        self.mice_spawn_timer = self.mice_spawn_interval

        self.mice_caught_counter = 0

        self.mice = arcade.SpriteList()

        player_x = self.window.width // 2
        player_y = self.window.height // 2

        self.player = Player(player_x, player_y, self.window.textures["player"])
        self.sprites.append(self.player)

        self.score = arcade.Text(
            str(self.mice_caught_counter),
            self.window.width // 2,
            int(self.window.height * 0.9),
            font_size=100,  # TODO: рассчитать от размера окна
            anchor_x="center",
            anchor_y="center",
        )
        self.text_objects.append(self.score)

    def on_key_press(self, symbol: int, _: int) -> None:
        """Система ввода: нажатие клавиш."""
        if symbol == arcade.key.ESCAPE:
            self.window.switch_view("menu")

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
            self.window.sound_manager.play_sound("catch")
            mouse.remove_from_sprite_lists()
            self.mice_caught_counter += 1
            self.score.text = str(self.mice_caught_counter)

    def spawn_mice(self) -> None:
        """Спавн мыши.

        Создает спрайт с текстурой в случайных координатах
        (отступ 10% от каждого края).
        """
        texture = self.window.textures["mouse"]
        mouse = arcade.Sprite(texture)
        mouse.center_x = random.randint(
            int(self.window.width * 0.1),
            int(self.window.width * 0.9),
        )
        mouse.center_y = random.randint(
            int(self.window.height * 0.1),
            int(self.window.height * 0.9),
        )
        mouse.scale = 0.1  # TODO: считать размер от размера окна
        self.sprites.append(mouse)
        self.mice.append(mouse)
