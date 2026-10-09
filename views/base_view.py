"""Модуль базового представления - родительского для всех."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import App

import arcade

import utils


class BaseView(arcade.View, ABC):
    """Базовое представление."""

    window: App

    @abstractmethod
    def __init__(self, bg_name: str = "") -> None:
        """Создает базовое представление."""
        super().__init__()
        self.sprites = arcade.SpriteList()
        self.text_objects: list[arcade.Text] = []
        if bg_name:
            self.make_bg(bg_name)

    def make_bg(self, bg_name: str) -> None:
        """Создает фон."""
        bg_x = self.window.width // 2
        bg_y = self.window.height // 2
        bg_texture = self.window.textures[bg_name]
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
        self.sprites.append(bg)

    def on_draw(self) -> None:
        """Отрисовывает спрайты."""
        self.clear()
        self.sprites.draw()
        for text_object in self.text_objects:
            text_object.draw()
