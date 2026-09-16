"""Accordion component directive."""

from docutils.parsers.rst import Directive

from .base import html_node


class Accordion(Directive):
    """Render an accessible, JavaScript-free accordion."""

    required_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        body = "\n".join(self.content)
        html = (
            '<details class="vanilla-component-scope vanilla-component vanilla-component--accordion p-accordion">'
            f"<summary>{self.arguments[0]}</summary>"
            f'<div class="p-accordion__panel"><p>{body}</p></div>'
            "</details>"
        )
        return html_node(html)
