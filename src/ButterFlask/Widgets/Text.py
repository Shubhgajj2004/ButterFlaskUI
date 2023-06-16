import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Widget import Widget
class Text(Widget):
    """
    A class representing a text widget.

    Attributes:
        text (str): The text content of the widget.
        font_size (int): The font size of the text in vw (viewport width).
        style (dict): Custom CSS style properties for the text widget.
        id (str): The HTML id attribute for the text widget.
        classes (str): The CSS classes for the text widget.
        on_click (callable): The function to be called when the text widget is clicked.

    Methods:
        _format_style(): Formats the style properties into a CSS string.
        render(): Renders the text widget as HTML.

    """
    def __init__(self, text, font_size=4, style=None, id='', classes='', on_click=None):
        """
        Initializes a Text widget.

        Args:
            text (str): The text content of the widget.
            font_size (int): The font size of the text in vw (viewport width).
            style (dict): Custom CSS style properties for the text widget.
            id (str): The HTML id attribute for the text widget.
            classes (str): The CSS classes for the text widget.
            on_click (callable): The function to be called when the text widget is clicked.

        """
        # super().__init__([child])
        self.text = text
        self.font_size = font_size
        self.style = style or {}
        self.id = id
        self.classes = classes
        self.on_click = on_click

    def _format_style(self):
        """
        Formats the style properties into a CSS string.

        Returns:
            str: A string containing the formatted CSS style properties.

        """
        default_style = {
            'font-size': f'{self.font_size}vw'
        }
        merged_style = {**default_style, **self.style}
        return '; '.join(f'{key}:{value}' for key, value in merged_style.items())

    def render(self):
        """
        Renders the text widget as HTML.

        Returns:
            str: The HTML representation of the text widget.

        """
        style = self._format_style()
        return f'<span id="{self.id}" class="{self.classes}" style="{style}">{self.text}</span>'
