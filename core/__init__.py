"""Модуль импорта компонентов приложения."""

from .app import App
from .assets_manger import AssetsManager
from .sound_manager import SoundManager

__all__ = [
    "App",
    "AssetsManager",
    "SoundManager",
]
