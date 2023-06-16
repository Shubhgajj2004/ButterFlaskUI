from typing import List, Dict, Optional
from Widget import Widget

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
        _generate_js_code(): Generates the JavaScript code for AJAX requests.
        _format_style(): Formats the CSS styles as a string.
        _format_class_attr(): Formats the classes as a string.
        _apply_default_style(): Applies default CSS styles to the button.
    """

    def __init__(
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
            js_code = self._generate_js_code()
            self.js.append(js_code) 
        class_attr = self._format_class_attr()
        return f'<button id="{self.id}" class="{class_attr}" style="{self._format_style()}" onclick="{onclick}">{self.text}</button>'

    def _generate_js_code(self) -> str:
        """
        Generates the JavaScript code for AJAX requests.

        Returns:
            str: The JavaScript code for AJAX requests.
        """
        js_code = f"""
                function {self.func_name}(event) {{
                    $.ajax({{
                        type: '{self.method}',
                        url: '{self.route}',
                        data: '{self.request_data}',
                        dataType: '{self.data_type}',
                        contentType: '{self.content_type}',
                        beforeSend: function(xhr) {{
                            {self.before_send}  // Add any custom headers or settings before sending the request
                        }},
                        success: function(response) {{
                            {self.on_success}  // Handle successful response
                        }},
                        error: function(xhr, status, error) {{
                            console.log(error);
                            {self.on_error}   // Handle error response
                        }},
                        complete: function() {{
                            {self.on_completed}
                        }}
                    }});
                }}
            """
        return js_code

    def _format_style(self) -> str:
        """
        Formats the CSS styles as a string.

        Returns:
            str: The formatted CSS styles.
        """
        return '; '.join(f'{key}: {value}' for key, value in self.style.items())
    
    def _format_class_attr(self) -> str:
        """
        Formats the classes as a string.

        Returns:
            str: The formatted class attribute.
        """
        classes = ' '.join(self.classes)
        return classes

    def _apply_default_style(self):
        """
        Applies default CSS styles to the button.
        """
        default_style = {
            'background-color': '#2196f3',
            'color': 'white',
            'padding': '10px 15px',
            'border': 'none',
            'border-radius': '4px',
            'cursor': 'pointer',
            'box-shadow': '0px 2px 5px rgba(0, 0, 0, 0.2)',
            'transition': 'background-color 0.3s ease'
        }
        self.style = {**default_style, **self.style}
