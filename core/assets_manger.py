"""Модуль менеджера ассетов: изображений, звуков, шрифтов."""

from collections.abc import Generator

import arcade
from PIL import ImageFont

import config
import utils


class AssetsManager:
    """Менеджер ассетов."""

    def __init__(self) -> None:
        """Создает менеджер ассетов."""
        self.textures: dict[str, arcade.Texture] = {}
        self.sounds: dict[str, arcade.Sound] = {}
        self.fonts: dict[str, str] = {}

    def load_assets(self) -> Generator[int]:
        """Загружает ассеты: текстуры и звуки."""
        percentage = 0

        textures_names = utils.get_filenames(config.IMG_DIR, config.IMG_EXTENSIONS)
        sounds_names = utils.get_filenames(config.SOUND_DIR, config.SOUND_EXTENSIONS)
        fonts_names = utils.get_filenames(config.FONT_DIR, config.FONT_EXTENSIONS)

        assets_count = (len(textures_names) + len(sounds_names) + len(fonts_names))
        if assets_count:
            load_step = round(100 / assets_count)
        else:
            load_step = 100
        file_names = textures_names + sounds_names + fonts_names
        for file_name in file_names:
            name, extention = file_name.split(".")[0], file_name.split(".")[-1]
            if extention in config.IMG_EXTENSIONS:
                self.textures[name] = arcade.load_texture(config.IMG_DIR / file_name)
            elif extention in config.SOUND_EXTENSIONS:
                sound = arcade.load_sound(config.SOUND_DIR / file_name)
                self.sounds[name] = sound
            elif extention in config.FONT_EXTENSIONS:
                arcade.load_font(config.FONT_DIR / file_name)
                font = ImageFont.truetype(config.FONT_DIR / file_name)
                font_family = font.getname()[0]
                self.fonts[name] = font_family
            percentage += load_step
            yield percentage

    def get_font(self, file_name: str) -> str:
        """Возвращает имя шрифта, если он есть в списке шрифтов."""
        if file_name in self.fonts:
            return self.fonts[file_name]
        error_message = f"Шрифта {file_name} нет в папке {config.FONT_DIR}"
        raise RuntimeError(error_message)
