"""Модуль экспорта контента файлов проекта в один TXT."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / "combined_content.txt"
EXCLUDE_DIRS = {
    ".git",
    ".svn",
    ".hg",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "node_modules",
    ".venv",
    "venv",
    "env",
    ".idea",
    ".vscode",
    "dist",
    "build",
    "target",
    ".tox",
}
EXCLUDE_EXTENSIONS = {
    ".toml", ".txt",
    ".pyc", ".pyo", ".pyd",
    ".exe", ".dll", ".so", ".dylib", ".bin",
    ".o", ".obj", ".a", ".lib",
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico", ".webp", ".svg",
    ".mp3", ".mp4", ".avi", ".mkv", ".mov", ".wav", ".flac",
    ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz",
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    ".db", ".sqlite", ".sqlite3",
    ".class", ".jar",
    ".woff", ".woff2", ".ttf", ".otf", ".eot",
}
EXCLUDE_FILES = {
    "dump.py",
    "combined_content.txt",
    ".DS_Store",
    "Thumbs.db",
    ".gitignore",
    ".gitattributes",
    "package-lock.json",
    "yarn.lock",
    "poetry.lock",
    "Pipfile.lock",
}


def should_skip(path: Path) -> bool:
    """Проверяет, нужно ли пропустить файл/папку."""
    # Пропускаем по имени файла
    if path.name in EXCLUDE_FILES:
        return True

    # Пропускаем по расширению
    if path.suffix.lower() in EXCLUDE_EXTENSIONS:
        return True

    # Пропускаем, если любая родительская папка в списке исключений
    for parent in path.parents:
        if parent.name in EXCLUDE_DIRS:
            return True
        # Останавливаемся, когда дошли до BASE_DIR
        if parent == BASE_DIR:
            break

    return False


def get_paths(base: Path) -> list[Path]:
    """Собирает все пути к файлам."""
    paths = [
        path for path in base.rglob("*")
        if path.is_file()
        and not should_skip(path)
    ]
    return sorted(paths)


def get_file_content(file_path: Path) -> str:
    """Возвращает контент файла."""
    # Пробуем несколько кодировок
    encodings = ["utf-8", "utf-8-sig", "cp1251", "latin-1"]
    for enc in encodings:
        try:
            return file_path.read_text(encoding=enc)
        except (UnicodeDecodeError, LookupError):
            continue
    # Если ничего не подошло — читаем с игнорированием ошибок
    return file_path.read_text(encoding="utf-8", errors="ignore")


def main() -> None:
    """Создает TXT с контентом всех файлов."""
    if not BASE_DIR.exists():
        print(f"Ошибка: папка {BASE_DIR} не существует")
        return

    print(f"Сканирую: {BASE_DIR.resolve()}")
    files = get_paths(BASE_DIR)
    print(f"Найдено файлов для объединения: {len(files)}")

    with OUTPUT_FILE.open("w", encoding="utf-8") as out:
        for i, file_path in enumerate(files, 1):
            rel_path = file_path.relative_to(BASE_DIR)
            print(f"[{i}/{len(files)}] {rel_path}")

            content = get_file_content(file_path)

            # Заголовок с путём к файлу
            out.write("=" * 80 + "\n")
            out.write(f"FILE: {rel_path.as_posix()}\n")
            out.write("=" * 80 + "\n\n")
            out.write(content)
            out.write("\n\n")

    print(f"\nГотово! Результат сохранён в: {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    main()