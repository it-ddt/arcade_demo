"""Утилиты."""

import pathlib

import arcade

def get_scale(
        width_required: float,
        height_required: float,
        width_initial: float,
        height_initial: float,
    ) -> float:
    """Возвращает масштаб.

    Масштаб - множитель: наибольше из отношений
    требуемой к исходной ширине (высоте).
    """
    width_ratio = width_required / width_initial
    height_ratio = height_required / height_initial
    return max(width_ratio, height_ratio)


def get_filenames(path: pathlib.Path, extentions: tuple[str]) -> list[str]:
    """Возвращает имена и расширения файлов в папке."""
    files = pathlib.Path.iterdir(path)
    return [
        file.name for file in files
        if file.is_file()
        and file.suffix.lower()[1:] in extentions
    ]

def get_font_size(
    text: str,
    target_width: float,
    font_name: str = "Press Start 2P",
) -> int:
    """Подбирает font_size так, чтобы текст примерно влез в target_width."""
    # Берём один пробный размер и масштабируем
    probe_size = 20
    probe = arcade.Text(text, 0, 0, font_size=probe_size, font_name=font_name)

    if probe.content_width == 0:
        return probe_size

    # Масштаб
    scale = target_width / probe.content_width
    return max(8, int(probe_size * scale))
