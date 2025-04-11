def ft_tqdm(lst: range) -> None:
    """
    A simple progress bar generator that mimics tqdm behavior.

    Args:
        lst (range): A range of items to iterate over.

    Yields:
        Each item from the input range, while printing progress to the console.
"""
    total = len(lst)
    for i, item in enumerate(lst, 1):
        progress = int((i/total) * 100)
        print(f'\r{progress}%|{"█" * progress}{" " * (100 - progress)}'
              f'|{i}/{total}', end='')
        yield item
