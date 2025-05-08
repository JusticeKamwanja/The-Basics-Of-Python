def get_formatted_name(first, last, middle=''):
    """Return a neatly formatted name."""
    full_name = f'{first} {middle} {last}' if middle else f'{first} {last}'
    return full_name.title().strip()
