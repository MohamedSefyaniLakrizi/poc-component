"""Button component directive."""

from docutils.parsers.rst import Directive, directives

from .base import html_node, link


class Button(Directive):
    """Render a reusable Canonical-styled button."""

    required_arguments = 1
    final_argument_whitespace = True
    has_content = False
    option_spec = {
        "href": directives.uri,
        "kind": lambda value: directives.choice(
            value, ("primary", "secondary", "negative")
        ),
    }

    def run(self):
        kind = self.options.get("kind", "primary")
        class_name = {
            "primary": "p-button--positive",
            "secondary": "p-button",
            "negative": "p-button--negative",
        }[kind]
        html = (
            '<span class="vanilla-component-scope vanilla-component vanilla-component--button">'
            f'{link(self.options["href"], self.arguments[0], class_name)}'
            "</span>"
        )
        return html_node(html)
