"""Модуль звука."""

import arcade
from arcade import Sound


class SoundManager:
    """Менеджер звука."""

    def __init__(self) -> None:
        """Создает менеджер звуков."""
        self._volume = 1
        self.is_mute = not bool(self._volume)
        self.sounds: dict[str, arcade.Sound] = {}
        self.players = []

    def change_volume(self, step: float) -> None:
        """Изменяет уровень громкости."""
        new_volume = self._volume + step

        if new_volume >= 0 and new_volume <= 1:
            self._volume = new_volume

        if self._volume > 0:
            self.is_mute = False
        else:
            self.is_mute = True

    def add_sound(self, name: str, sound: arcade.Sound) -> None:
        """Добавляет звук."""
        self.sounds[name] = sound

    def play_sound(self, sound_name: str) -> None:
        """Издает звук один раз."""
        if self.is_mute:
            return

        sound = self.sounds.get(sound_name)
        if not sound:
            return
        player = sound.play()
        self.players.append(player)

    def play_music(self) -> None:
        """Проигрывает музыку циклично."""
        if self.is_mute:
            return

        sound = self.sounds.get("music")
        if not sound:
            return
        player = sound.play(loop=True)
        self.players.append(player)  # TODO: что делать с отыгравшими плеерами?

    def mute(self) -> None:
        """Выключает все звуки."""
        for player in self.players:
            arcade.stop_sound(player)
        self.players.clear()
        self.is_mute = True

    def toggle_mute(self) -> bool:
        """Переключает mute."""
        self.is_mute = not self.is_mute
        if self.is_mute:
            self.mute()
        else:
            self.play_music()
        return self.is_mute
