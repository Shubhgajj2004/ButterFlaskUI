from typing import Dict

def format_style(style: Dict[str, str]) -> str:
    """
    Formats the CSS styles as a string.

    Args:
        style (Dict[str, str]): The CSS styles.

    Returns:
        str: The formatted CSS styles.
    """
    return '; '.join(f'{key}: {value}' for key, value in style.items())
