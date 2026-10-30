"""Модуль игры: логика, правила, взаимодействие спрайтов."""

import arcade
from app import App

from sprites import BaseSprite, Mouse, Player


class Game:
    """Игра."""

    def __init__(self, window: App):
        """Создает игру."""
        self.window = window

        self.sprites: arcade.SpriteList[BaseSprite] = arcade.SpriteList()
        self.mice: arcade.SpriteList[Mouse] = arcade.SpriteList()
        self.text_objects = list[arcade.Text]

        self.player: Player | None = None

        self.mice_spawn_interval = 1  # сек
        self.mice_spawn_timer = self.mice_spawn_interval
        self.mice_caught_counter = 0

        self.score = arcade.Text(
            str(self.mice_caught_counter),
            self.window.width // 2,
            int(self.window.height * 0.9),
            font_size=100,  # TODO: рассчитать от размера окна
            anchor_x="center",
            anchor_y="center",
        )
        self.text_objects.append(self.score)

    def start_new_game(self) -> None:
        """Начинает новую игру."""
        self.sprites.clear()
        player_x = self.window.width // 2
        player_y = self.window.height // 2
        self.player = Player(player_x, player_y, self.window.textures["player"])
        self.sprites.append(self.player)

        self.mice.clear()
        self.mice_spawn_timer = self.mice_spawn_interval
        self.mice_caught_counter = 0

        self.score.text = str(self.mice_caught_counter)

    def continue_game(self) -> None:
        """Продолжает игру."""

    def save_game(self) -> None:
        """Сохраняет игру."""

    def load_game(self) -> None:
        """Загружает игру."""

    def on_update(self, delta_time: float) -> None:
        """Спавнит мышей, двигает игрока, удаляет пойманных мышей."""
        self.mice_spawn_timer += delta_time
        if self.mice_spawn_timer >= self.mice_spawn_interval:
            self.spawn_mouse()
            self.mice_spawn_timer = 0
        for mouse in self.mice:
            mouse.move(self.player.center_x, self.player.center_y)
        self.sprites.update(delta_time)
        for sprite in self.sprites:
            sprite.stay_inside_bounds(self.window.width, self.window.height)

        mice_caught: list[arcade.Sprite] = arcade.check_for_collision_with_list(
            self.player,
            self.mice,
        )
        for mouse in mice_caught:
            self.window.sound_manager.play_sound("catch")
            mouse.remove_from_sprite_lists()
            self.mice_caught_counter += 1
            self.score.text = str(self.mice_caught_counter)

    def spawn_mouse(self) -> None:
        """Спавн мыши.

        Создает спрайт с текстурой в случайных координатах
        (отступ 10% от каждого края).
        """
        texture = self.window.textures["mouse"]
        x = random.randint(
            int(self.window.width * 0.1),
            int(self.window.width * 0.9),
        )
        y = random.randint(
            int(self.window.height * 0.1),
            int(self.window.height * 0.9),
        )
        mouse = Mouse(x, y, texture)
        mouse.scale = 0.1  # TODO: считать размер от размера окна
        self.sprites.append(mouse)
        self.mice.append(mouse)
