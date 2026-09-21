"""Утилиты."""


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
