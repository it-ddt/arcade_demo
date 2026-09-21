"""Модуль конфигурации."""

import pathlib

FPS = 60  # сколько кадров в секунду

BASE_DIR = pathlib.Path(__file__).resolve().parent  # папка проекта
ASSETS_DIR = BASE_DIR / "assets"
IMG_DIR = ASSETS_DIR / "img"
