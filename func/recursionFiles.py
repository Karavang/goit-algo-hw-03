from pathlib import Path
from sys import argv
from shutil import copy2


def display_tree(path: Path, indent: Path) -> None:

    if path.is_dir() & indent.is_dir():

        for child in path.iterdir():
            display_tree(child, indent) if child.is_dir() else cloneInNew(child, indent)


def cloneInNew(file: Path, indent: Path) -> None:
    target_dir = indent / file.suffix[1:]
    if not target_dir.exists():
        target_dir.mkdir(parents=True, exist_ok=True)
    copy2(file, target_dir / file.name)


if __name__ == "__main__":
    try:
        if len(argv[1:]) >= 2:
            display_tree(Path(argv[1]), Path(argv[2]))
        elif len(argv[1:]) == 1:
            dist_path = Path(argv[1]).parent / "dist"
            if not dist_path.exists():
                dist_path.mkdir(parents=True, exist_ok=True)
            display_tree(Path(argv[1]), dist_path)
        else:
            print("Please provide a valid path.")
    except PermissionError:
        print("Немає дозволу на доступ до файлу.")
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
