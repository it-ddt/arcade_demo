"""Модуль конфигурации."""

import pathlib

TITLE = "Игра на Arcade 3.3.3"
FPS = 60  # сколько кадров в секунду

IMG_EXTENSIONS = ("png", "jpg", "jpeg")
SOUND_EXTENSIONS = ("mp3", "wav", "ogg")
FONT_EXTENSIONS = ("ttf", "otf")

FONT_TITLE = "Press Start 2P"
FONT_BUTTON = "Press Start 2P"
FONT_SCORE = "Press Start 2P"

BASE_DIR = pathlib.Path(__file__).resolve().parent  # папка проекта
ASSETS_DIR = BASE_DIR / "assets"
IMG_DIR = ASSETS_DIR / "img"
SOUND_DIR = ASSETS_DIR /  "sound"
FONT_DIR = ASSETS_DIR / "font"
