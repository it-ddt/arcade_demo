"""Модуль представлений."""

import random

import arcade

import config
from sprites import (
    BaseSprite,
    Mouse,
    Obstacle,
    Player,
    TextOutlined,
)

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
        self.world_width = self.window.width * config.WORLD_WIDTH
        self.world_height = self.window.height * config.WORLD_HEIGHT

        self.sprites: arcade.SpriteList[BaseSprite] = arcade.SpriteList()
        self.mice: arcade.SpriteList[Mouse] = arcade.SpriteList()
        self.obstacles: arcade.SpriteList[Obstacle] = arcade.SpriteList()

        self.player = Player(
            0,
            0,
            self.textures["player"],
        )
        self.sprites.append(self.player)
        self.tags.append(self.player.tag_hp)

        self.mice_spawn_interval = 1  # сек
        self.mice_spawn_timer = self.mice_spawn_interval
        self.mice_caught_counter = 0

        self.score = TextOutlined(
            str(self.mice_caught_counter),
            self.window.width // 2,
            int(self.window.height * 0.9),
            font_size=100,  # TODO: рассчитать от размера окна
            font_name=self.fonts[config.FONT_SCORE],
        )
        self.text_objects.append(self.score)

        self.make_world_bounds()

    def make_world_bounds(self) -> None:
        """Создает 4 стены вокруг мира."""
        obstacle = Obstacle(
            self.world_width / 2,
            self.world_height,
            self.world_width,
            self.world_height * 0.1,
        )  # верхняя
        self.obstacles.append(obstacle)
        obstacle = Obstacle(
            self.world_width / 2,
            0,
            self.world_width,
            self.world_height * 0.1,
        )  # нижняя
        self.obstacles.append(obstacle)
        obstacle = Obstacle(
            0,
            self.world_height / 2,
            self.world_height * 0.1,
            self.world_height,
        )  # левая
        self.obstacles.append(obstacle)
        obstacle = Obstacle(
            self.world_width,
            self.world_height / 2,
            self.world_height * 0.1,
            self.world_height,
        )  # правая
        self.obstacles.append(obstacle)

    def on_draw(self) -> None:
        """Сначала рисует все, а потом границы мира."""
        self.clear()
        self.camera_player.use()
        self.bg_sprites.draw()
        self.sprites.draw()
        for tag in self.tags:
            tag.draw()
        self.obstacles.draw()

        self.camera_hud.use()
        for text_object in self.text_objects:
            text_object.draw()
        for button in self.buttons:
            button.on_draw()


    def setup(self) -> None:
        """Возвращает игру в исходное состояние."""
        self.sprites.clear()
        self.mice.clear()

        self.player.center_x = self.world_width / 2
        self.player.center_y = self.world_height / 2
        self.player.angle = 0
        self.sprites.append(self.player)

        self.mice_caught_counter = 0
        self.score.text = str(self.mice_caught_counter)
        self.mice_spawn_timer = self.mice_spawn_interval

    def on_key_press(self, symbol: int, _: int) -> None:
        """Система ввода: нажатие клавиш."""
        if symbol == arcade.key.ESCAPE:
            self.window.switch_view("menu")

        if symbol == arcade.key.D:
            self.player.turn_direction = 1
        if symbol == arcade.key.A:
            self.player.turn_direction = -1

        if symbol == arcade.key.W:
            self.player.move_direction = 1
        if symbol == arcade.key.S:
            self.player.move_direction = -1

    def on_key_release(self, symbol: int, _: int) -> None:
        """Система ввода: отпускание клавиш."""
        if symbol == arcade.key.D:
            self.player.turn_direction = 0
        if symbol == arcade.key.A:
            self.player.turn_direction = 0

        if symbol == arcade.key.W:
            self.player.move_direction = 0
        if symbol == arcade.key.S:
            self.player.move_direction = 0

    def on_update(self, delta_time: float) -> None:
        """Спавнит мышей, двигает игрока, удаляет пойманных мышей."""
        self.mice_spawn_timer += delta_time
        if self.mice_spawn_timer >= self.mice_spawn_interval:
            self.spawn_mouse()
            self.mice_spawn_timer = 0
        for mouse in self.mice:
            mouse.move(self.player.center_x, self.player.center_y)
        self.sprites.update(delta_time)

        mice_caught: list[Mouse] = arcade.check_for_collision_with_list(
            self.player,
            self.mice,
        )
        for mouse in mice_caught:
            self.window.sound_manager.play_sound("catch")
            self.tags.remove(mouse.tag_hp)
            mouse.remove_from_sprite_lists()
            self.mice_caught_counter += 1
            self.score.text = str(self.mice_caught_counter)

        self.update_camera()

    def update_camera(self) -> None:
        """"""

        cam_y = self.player.center_y

        min_x = self.window.width / 2
        cam_x = self.player.center_x
        max_x = self.world_width - self.window.width / 2

        min_y = self.window.height / 2
        cam_y = self.player.center_y
        max_y = self.world_height - self.window.height / 2

        cam_x = max(min_x, min(cam_x, max_x))
        cam_y = max(min_y, min(cam_y, max_y))
        self.camera_player.position = (cam_x, cam_y)

    def spawn_mouse(self) -> None:
        """Спавн мыши.

        Создает спрайт с текстурой в случайных координатах
        (отступ 10% от каждого края).
        """
        x = random.randint(
            int(self.window.width * 0.1),
            int(self.window.width * 0.9),
        )
        y = random.randint(
            int(self.window.height * 0.1),
            int(self.window.height * 0.9),
        )
        texture = self.textures["mouse"]
        mouse = Mouse(x, y, texture)
        mouse.scale = 0.1  # TODO: считать размер от размера окна
        self.sprites.append(mouse)
        self.mice.append(mouse)
        self.tags.append(mouse.tag_hp)
