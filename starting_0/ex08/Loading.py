import os


def get_terminal_width() -> int:
    """Return the terminal width or a safe fallback for captured output."""
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80


def ft_tqdm(lst: range) -> None:
    """Yield items from lst while displaying a simple progress bar."""
    total = len(lst)
    if total == 0:
        return

    for index, elem in enumerate(lst, start=1):
        percent = int(index / total * 100)
        terminal_width = get_terminal_width()
        bar_width = max(1, terminal_width - 20)
        filled_width = int(bar_width * index / total)
        empty_width = bar_width - filled_width

        if index == total:
            bar = "=" * filled_width
        else:
            bar = "=" * max(0, filled_width - 1) + ">" + " " * empty_width

        print(f"\r{percent:3d}%|[{bar}]| {index}/{total}", end="")
        yield elem
