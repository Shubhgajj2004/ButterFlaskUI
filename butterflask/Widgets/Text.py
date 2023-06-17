from ..Widget import Widget

class Text(Widget):
    """
    A class representing a text widget.

    Attributes:
        text (str): The text content of the widget.
        font_size (str): The font size of the text in rem (e.g., '1.4rem').
        style (dict): Custom CSS style properties for the text widget.
        id (str): The HTML id attribute for the text widget.
        classes (str): The CSS classes for the text widget.
        on_click (callable): The function to be called when the text widget is clicked.

    Methods:
        _format_style(): Formats the style properties into a CSS string.
        render(): Renders the text widget as HTML.

    """
    def __init__(self, text, font_size='1.0rem', style=None, id='', classes='', on_click=None):
        """
        Initializes a Text widget.

        Args:
            text (str): The text content of the widget.
            font_size (str): The font size of the text in rem (e.g., '1.4rem').
            style (dict): Custom CSS style properties for the text widget.
            id (str): The HTML id attribute for the text widget.
            classes (str): The CSS classes for the text widget.
            on_click (callable): The function to be called when the text widget is clicked.

        """
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
            'font-size': self.font_size,
            'line-height': '1.5em',
            'font-family': r'&quot;Lato&quot;, &quot;Corbel&quot;, &quot;Avenir&quot;, &quot;Lucida Grande&quot;, &quot;Lucida Sans&quot;, sans-serif',
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
