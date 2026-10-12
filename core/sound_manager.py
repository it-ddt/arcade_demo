"""Модуль звука."""

import arcade


class SoundManager:
    """Менеджер звука."""

    def __init__(self) -> None:
        """Создает менеджер звуков."""
        self._volume = 1.0
        self.is_mute = not bool(self._volume)
        self.sounds: dict[str, arcade.Sound] = {}
        self.players = []

    @property
    def volume(self) -> float:
        """Уровень громкости."""
        return self._volume

    @volume.setter
    def volume(self, value: float) -> None:
        value = max(0.0, min(1.0, value))
        self._volume = value
        self._is_mute = not bool(self._volume)

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
        player = sound.play(loop=True, volume=self._volume)
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
