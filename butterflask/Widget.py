# import sys
# import os

# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))


#Widget is the baseclass inherited by all other Widget classes

class Widget:
    def __init__(self, children=None):
        self.children = children or []

    def render(self):
        rendered_children = ''.join(child.render() for child in self.children)
        return rendered_children