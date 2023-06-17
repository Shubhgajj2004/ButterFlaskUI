# ButterFlask-UI 🧈

[![PyPI version](https://badge.fury.io/py/butterflask.svg)](https://badge.fury.io/py/butterflask)

🌿 ButterFlask-UI is a modern and lightweight Python framework for creating highly responsive websites using widgets. It provides a seamless development experience, similar to Flutter, by leveraging the power of widgets to build interactive user interfaces. With ButterFlask-UI, you can easily create elegant and dynamic web applications by composing reusable widgets. The framework simplifies the process of handling API requests in the front-end through AJAX, enabling efficient data exchange and seamless user interactions.

## Motivation
Writing code for making responsive web interfaces is often a head-scratching problem. Traditional HTML/CSS/JS approaches can result in complex and hard-to-maintain code. Additionally, handling API requests asynchronously can be cumbersome and error-prone.

The goal of ButterFlask-UI is to address these challenges and provide a modern solution for building web applications. By adopting a widget-based approach, developers can focus on composing reusable components to create responsive and interactive interfaces. The framework abstracts away the complexities of handling API requests, making it easier to exchange data with the server and create seamless user interactions.

## Key Features

- 🧩 Intuitive widget-based approach for building web interfaces
- 🌐 Highly responsive design for optimal viewing across different devices
- 🚀 Effortless handling of API requests
- 🎨 Simplified widget composition and customization
- 📦 Easy integration with existing Flask and Django projects
- 🌈 Increased reusability and readability compared to traditional HTML/CSS/JS

ButterFlask-UI empowers developers to rapidly create feature-rich web applications with smooth user experiences. Whether you're building a personal project or a professional web application, ButterFlask-UI offers the flexibility and simplicity you need to bring your ideas to life.

## Installation

You can install ButterFlask-UI using pip:

```shell
pip install butterflask
```

## Getting Started

### Flask

To integrate ButterFlask-UI into your Flask application, follow these steps:

1. Create a new Flask project or open an existing one.

2. In your every HTML template file (ex-`index.html`), include the following code:

```html
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
    <title>My Web App</title>
</head>
<body style="margin: 0px; padding: 0%;">
    {{ ui | safe }}
    <script>
        {{ js | safe }}
    </script>
</body>
</html>
```

3. In your Flask `app.py` file, import the necessary modules and create a route:

```python
from flask import Flask, render_template

#Import widgets from butterflask
from butterflask.Widgets.Button import Button
from butterflask.widgets.Row import Row

app = Flask(__name__)

@app.route('/')
def home():
    js = [' '] #necessary to add

    #Actual font-end code
    ui = Row (
                children=[
                    Button("btn1"),
                    Button("btn2"),
                    Button("btn3")
                ],
                horizontal='space-between'
            ) # Make any hierarchy using widgets

    #render ui, javascript code and send to html code by passing ui and js
    return render_template('index.html', ui=ui.render(), js='\n'.join(js))

if __name__ == '__main__':
    app.run(debug=True)
```

4. Run your Flask application and navigate to `http://localhost:5000` in your web browser.

### Django

To integrate ButterFlask-UI into your Django project, follow these steps:

1. Create a new Django project or open an existing one.

2. In your HTML template file (ex-`index.html`), include the following code:

```html
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
    <title>My Web App</title>
</head>
<body>
    {{ ui | safe }}
    <script>
        // Retrieve the CSRF token from cookies
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    // Extract the token if found
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        // Include the CSRF token in all AJAX requests
        $(function() {
            $.ajaxSetup({
                headers: { 'X-CSRFToken': getCookie('csrftoken') }
            });
        });
        var csrfToken = getCookie('csrftoken');
        {{ js | safe }}
    </script>
</body>
</html>
```

3. In your Django `view.py` file, import the necessary modules and render the template:

```python
from django.shortcuts import render

#Import widgets from butterflask
from butterflask.Widgets.Button import Button
from butterflask.widgets.Row import Row

def home(request):

    js = [' '] #necessary to add

    #Actual font-end code
    ui = Row (
                children=[
                    Button("btn1"),
                    Button("btn2"),
                    Button("btn3")
                ],
                horizontal='space-between'
            ) # Make any hierarchy using widgets

    
    return render(request, 'index.html', {'ui': ui.render(), 'js': '\n'.join(js)})
```

4. Set up the appropriate URL mapping in your `urls.py` file to connect the view to a URL route.

5. Run your Django application and navigate to the appropriate URL in your web browser.

## Documentation

For detailed documentation and examples, please visit the ButterFlask-UI Documentation. We will shortly make proper easy documentation website.

## Contributing

We welcome contributions from the open-source community. If you find a bug or have a suggestion for improvement, please open an issue on the [GitHub repository](https://github.com/Shubhgajj2004/ButterFlaskUI).

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Shubhgajj2004/ButterFlaskUI/blob/main/LICENSE) file for more information.

👉 For more details, examples, and advanced usage, please refer to the [ButterFlask-UI Documentation](https://github.com/your-github-username/your-repo-name). (Shortly release)

Enjoy building beautiful and interactive web applications with ButterFlask-UI! 🚀🌐

[![LinkedIn](https://img.shields.io/badge/Connect%20with%20us%20on-LinkedIn-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/shubh-gajjar-1b0a19223/) 
