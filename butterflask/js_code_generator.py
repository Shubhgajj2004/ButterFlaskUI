def generate_js_code(
    func_name: str,
    method: str,
    route: str,
    request_data: str,
    data_type: str,
    content_type: str,
    before_send: str,
    on_success: str,
    on_error: str,
    on_completed: str
) -> str:
    """
    Generates the JavaScript code for AJAX requests.

    Args:
        func_name (str): The name of the JavaScript function.
        method (str): The HTTP method for the request.
        route (str): The URL route for the request.
        request_data (str): The data to be sent with the request.
        data_type (str): The expected data type of the response.
        content_type (str): The content type of the request.
        before_send (str): Any custom headers or settings to be added before sending the request.
        on_success (str): JavaScript code to handle a successful response.
        on_error (str): JavaScript code to handle an error response.
        on_completed (str): JavaScript code to be executed when the request is completed.

    Returns:
        str: The JavaScript code for AJAX requests.
    """
    js_code = f"""
        function {func_name}(event) {{
            $.ajax({{
                type: '{method}',
                url: '{route}',
                data: '{request_data}',
                dataType: '{data_type}',
                contentType: '{content_type}',
                beforeSend: function(xhr) {{
                    {before_send}
                }},
                success: function(response) {{
                    {on_success}
                }},
                error: function(xhr, status, error) {{
                    console.log(error);
                    {on_error}
                }},
                complete: function() {{
                    {on_completed}
                }}
            }});
        }}
    """
    return js_code
