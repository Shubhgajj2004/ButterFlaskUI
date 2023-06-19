from typing import List, Dict, Optional
from ..Widget import Widget
from ..style_formatter import format_style
from ..class_formatter import format_class_attr
from ..js_code_generator import generate_js_code

class Center(Widget):
    """
    A widget representing a centered div.



    Attributes:
        id (str): ID attribute for the div.
        classes (List[str]): List of CSS class names for the div.
        func_name (str): Name of the JavaScript function to be called on click event.
        method (str): HTTP method for the AJAX request.
        js (List[str]): List of additional JavaScript code snippets.
        on_click (str): JavaScript code to be executed on click event.
        style (Dict[str, str]): Dictionary of CSS styles for the div.
        route (str): URL route for the AJAX request.
        request_data (str): Data to be sent in the AJAX request body.
        before_send (str): JavaScript code to be executed before sending the AJAX request.
        data_type (str): Expected data type in the AJAX response.
        content_type (str): Content type of the AJAX request.
        on_success (str): JavaScript code to be executed on successful AJAX response.
        on_completed (str): JavaScript code to be executed after AJAX request completion.
        on_error (str): JavaScript code to be executed on AJAX request error.

    """

    def __init__(
        self,
        child,
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
        Initializes a Center widget.
        
        Args:
            default (bool): Whether to apply default styles to the div. Default is True.
            id (str): ID attribute for the div. Default is an empty string.
            classes (List[str]): List of CSS class names for the div. Default is an empty list.
            func_name (str, optional): Name of the JavaScript function to be called on click event.
            method (str): HTTP method for the AJAX request. Default is 'POST'.
            js (List[str], optional): List of additional JavaScript code snippets.
            on_click (str, optional): JavaScript code to be executed on click event.
            style (Dict[str, str], optional): Dictionary of CSS styles for the div.
            route (str, optional): URL route for the AJAX request.
            request_data (str): Data to be sent in the AJAX request body.
            before_send (str): JavaScript code to be executed before sending the AJAX request.
            data_type (str): Expected data type in the AJAX response. Default is 'json'.
            content_type (str): Content type of the AJAX request. Default is 'application/json'.
            on_success (str): JavaScript code to be executed on successful AJAX response.
            on_completed (str): JavaScript code to be executed after AJAX request completion.
            on_error (str): JavaScript code to be executed on AJAX request error.
        """
        super().__init__(children=[child])
        self.id = id
        self.classes = classes or []
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
        Renders the HTML representation of the centered div.

        Returns:
            str: HTML string representing the centered div.
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
        return f'<div id="{self.id}" class="{class_attr}" style="{style_attr}" onclick="{onclick}">{super().render()}</div>'

    def _apply_default_style(self):
        """
        Applies default CSS styles to the centered div.
        """
        default_style = {
            'display': 'flex',
            'justify-content': 'center'
        }
        self.style = {**default_style, **self.style}
