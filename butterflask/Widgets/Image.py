from typing import Dict, Optional, List
from ..Widget import Widget
from ..style_formatter import format_style
from ..class_formatter import format_class_attr
from ..js_code_generator import generate_js_code

class Image(Widget):
    """
    A class representing an Image widget.

    Attributes:
        source (str): The source URL of the image.
        alt (str, optional): The alternative text for the image. Defaults to an empty string.
        style (Dict[str, str], optional): CSS styles for the image. Defaults to an empty dictionary.
        default (bool, optional): Whether to apply default styles to the image. Defaults to True.
        id (str, optional): The ID attribute of the image. Defaults to ''.
        classes (List[str], optional): The classes to apply to the image. Defaults to an empty list.
        func_name (str, optional): The name of the JavaScript function associated with the image's click event.
        method (str, optional): The HTTP method used for AJAX requests. Defaults to 'POST'.
        js (List[str], optional): Additional JavaScript code to be included. Defaults to an empty list.
        on_click (str, optional): JavaScript code to be executed on image click.
        route (str, optional): The URL for AJAX requests. Defaults to None.
        request_data (str, optional): Data to be sent with AJAX requests. Defaults to an empty string.
        before_send (str, optional): JavaScript code to be executed before sending AJAX requests.
        data_type (str, optional): The expected data type for AJAX responses. Defaults to 'json'.
        content_type (str, optional): The content type for AJAX requests. Defaults to 'application/json'.
        on_success (str, optional): JavaScript code to be executed on successful AJAX response.
        on_completed (str, optional): JavaScript code to be executed after AJAX request completes.
        on_error (str, optional): JavaScript code to be executed on AJAX error response.

    Inherits from:
        Widget: The base class for widgets.

    Methods:
        render(): Renders the Image as HTML.
        _apply_default_style(): Applies default CSS styles to the image.
    """

    def __init__(
        self,
        source: str,
        alt: str = '',
        style: Optional[Dict[str, str]] = None,
        default: bool = True,
        id: str = '',
        classes: List[str] = None,
        func_name: Optional[str] = None,
        method: str = 'POST',
        js: Optional[List[str]] = None,
        on_click: Optional[str] = None,
        route: Optional[str] = None,
        request_data: str = '',
        before_send: str = '',
        data_type: str = 'json',
        content_type: str = 'application/json',
        on_success: str = '',
        on_completed: str = '',
        on_error: str = ''
    ):
        """
        Initializes an Image instance.

        Args:
            source (str): The source URL of the image.
            alt (str, optional): The alternative text for the image. Defaults to an empty string.
            style (Dict[str, str], optional): CSS styles for the image. Defaults to an empty dictionary.
            default (bool, optional): Whether to apply default styles to the image. Defaults to True.
            id (str, optional): The ID attribute of the image. Defaults to ''.
            classes (List[str], optional): The classes to apply to the image. Defaults to an empty list.
            func_name (str, optional): The name of the JavaScript function associated with the image's click event.
            method (str, optional): The HTTP method used for AJAX requests. Defaults to 'POST'.
            js (List[str], optional): Additional JavaScript code to be included. Defaults to an empty list.
            on_click (str, optional): JavaScript code to be executed on image click.
            route (str, optional): The URL for AJAX requests. Defaults to None.
            request_data (str, optional): Data to be sent with AJAX requests. Defaults to an empty string.
            before_send (str, optional): JavaScript code to be executed before sending AJAX requests.
            data_type (str, optional): The expected data type for AJAX responses. Defaults to 'json'.
            content_type (str, optional): The content type for AJAX requests. Defaults to 'application/json'.
            on_success (str, optional): JavaScript code to be executed on successful AJAX response.
            on_completed (str, optional): JavaScript code to be executed after AJAX request completes.
            on_error (str, optional): JavaScript code to be executed on AJAX error response.
        """
        super().__init__(None)
        self.source = source
        self.alt = alt
        self.style = style or {}
        self.default = default
        self.id = id
        self.classes = classes or []
        self.func_name = func_name
        self.method = method
        self.js = js or []
        self.on_click = on_click
        self.route = route
        self.request_data = request_data
        self.before_send = before_send
        self.data_type = data_type
        self.content_type = content_type
        self.on_success = on_success
        self.on_completed = on_completed
        self.on_error = on_error

        if default:
            self._apply_default_style()

    def render(self) -> str:
        """
        Renders the image as HTML.

        Returns:
            str: The HTML representation of the image.
        """
        onclick = f"event.preventDefault(); {self.on_click}" if self.on_click else ""
        if self.js and self.route:
            js_code = generate_js_code(
                self.func_name,
                self.method,
                self.route,
                self.request_data,
                self.data_type,
                self.content_type,
                self.before_send,
                self.on_success,
                self.on_error,
                self.on_completed
            )
            self.js.append(js_code)
        style_attr = format_style(self.style)
        class_attr = format_class_attr(self.classes)
        return f'<img id="{self.id}" src="{self.source}" alt="{self.alt}" style="{style_attr}" class="{class_attr}" onclick="{onclick}">'

    def _apply_default_style(self):
        """
        Applies default CSS styles to the image.
        """
        default_style = {
            'max-width': '100%',
            'height': 'auto',
            'background-size': 'cover',
            'background-position': 'center',
            'border-radius': '7px'
        }
        self.style = {**default_style, **self.style}