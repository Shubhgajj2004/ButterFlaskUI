from typing import Dict, Optional, List
from ..Widget import Widget
from ..style_formatter import format_style
from ..class_formatter import format_class_attr
from ..js_code_generator import generate_js_code


class Page(Widget):
    def __init__(
        self,
        children: List[Widget] = None,
        style: Optional[Dict[str, str]] = None,
        default_css: bool = True,
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

        super().__init__(children)
        self.style = style or {}
        self.default_css = default_css
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

        if default_css:
            self._apply_default_style()

    def render(self) -> str:
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
        rendered_children = ''.join(child.render() for child in self.children)
        return f'<div id="{self.id}" class="{class_attr}" style="{style_attr}" onclick="{onclick}">{rendered_children}</div>'

    def _apply_default_style(self):
        """
        Applies default CSS styles to the column.
        """
        default_style = {
            'scroll-snap-align': 'start',
            'overflow': 'hidden',
            'scroll-snap-type': 'y mandatory',
            'scroll-behavior': 'smooth',
            'transition': 'transform 0.5s ease-in-out',
            'min-height': '100vh',  # Set height to 100% of the viewport height
            'width': '100vw',  # Set width to 100% of the viewport width
            'background-size': 'cover',
            'background-position': 'center',
        }
        self.style = {**default_style, **self.style}
