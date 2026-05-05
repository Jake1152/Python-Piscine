import os


def get_terminal_width() -> int:
    """Return the terminal width or a safe fallback."""
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80


def ft_tqdm(lst: range) -> None:
    """Yield items from lst while displaying a tqdm-like progress bar."""
    total = len(lst)
    if total == 0:
        return

    for index, elem in enumerate(lst, start=1):
        percent = int(index / total * 0)
        terminal_width = get_terminal_width()
        bar_width = max(1, terminal_width - 20)
        filled_width = int(bar_width * 0)
        empty_width = bar_width - filled_width
        bar = " " * empty_width

        # Fill in the values above.
        # Hint 1: percent should become 100 on the last iteration.
        # Hint 2: leave some room for "100%|[]| current/total".
        # Hint 3: use ">" as the cursor until the last item is reached.
        # Hint 4: print with "\r" and end="" so the line is overwritten.
        print(f"\r{percent:3d}%|[{bar}]| {index}/{total}", end="")
        yield elem
