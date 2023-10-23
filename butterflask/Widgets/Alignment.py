from typing import List, Dict, Optional
from ..Widget import Widget
from ..style_formatter import format_style
from ..class_formatter import format_class_attr
from ..js_code_generator import generate_js_code

class Button(Widget):
    """
    A class representing a Button widget.

    Attributes:
        text (str): The text displayed on the button.
        default (bool, optional): Whether to apply default styles to the button. Defaults to True.
        id (str, optional): The ID attribute of the button. Defaults to ''.
        classes (List[str], optional): The classes to apply to the button. Defaults to an empty list.
        func_name (str, optional): The name of the JavaScript function associated with the button's click event.
        method (str, optional): The HTTP method used for AJAX requests. Defaults to 'POST'.
        js (List[str], optional): Additional JavaScript code to be included. Defaults to an empty list.
        on_click (str, optional): JavaScript code to be executed on button click.
        style (Dict[str, str], optional): CSS styles for the button. Defaults to an empty dictionary.
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
        render(): Renders the button as HTML.
        _apply_default_style(): Applies default CSS styles to the button.
    """

    def __init__(
        alignment,
        self,
        text: str,
        default: bool = True,
        id: str = '',
        classes: List[str] = None,
        func_name: Optional[str] = None,
        method: str = 'POST',
        js: Optional[List[str]] = None,
        on_click: Optional[str] = None,
        style: Optional[Dict[str, str]] = None,
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
        Initializes a Button instance.

        Args:
            text (str): The text displayed on the button.
            default (bool, optional): Whether to apply default styles to the button. Defaults to True.
            id (str, optional): The ID attribute of the button. Defaults to ''.
            classes (List[str], optional): The classes to apply to the button. Defaults to an empty list.
            func_name (str, optional): The name of the JavaScript function associated with the button's click event.
            method (str, optional): The HTTP method used for AJAX requests. Defaults to 'POST'.
            js (List[str], optional): Additional JavaScript code to be included. Defaults to an empty list.
            on_click (str, optional): JavaScript code to be executed on button click.
            style (Dict[str, str], optional): CSS styles for the button. Defaults to an empty dictionary.
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
        self.text = text
        self.id = id
        self.classes = classes or []  # Initialize as empty list if None is provided
        self.func_name = func_name
        self.method = method
        self.js = js or []
        self.on_click = on_click
        self.style = style or {}
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
        Renders the button as HTML.

        Returns:
            str: The HTML representation of the button.
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
        class_attr = format_class_attr(self.classes)
        style_attr = format_style(self.style)
        return f'<div id="{self.id}" class="{class_attr}" style="{style_attr}" onclick="{onclick}">{self.text}</div>'

    def _apply_default_style(self):
        """
        Applies default CSS styles to the button.
        """
        if(self.alignement == 'top'):
            default_style = {
                'position':'absolute',
                'top':'0px'
            }
        elif(self.alignment == 'bottom'):
            default_style = {
                'position':'absolute',
                'bottom':'0px'
            }
        elif(self.alignment == 'left'):
            default_style = {
                'position':'absolute',
                'left':'0px'
            }
        elif(self.alignment == 'bottom'):
            default_style = {
                'position':'right',
                'right':'0px'
            }
        self.style = {**default_style, **self.style}
