"""Card component directive."""

from docutils.parsers.rst import Directive, directives

from .base import html_node


class Card(Directive):
    """Render a linked Vanilla Framework card."""

    required_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {"href": directives.uri}

    def run(self):
        title = self.arguments[0]
        href = self.options["href"]
        body = "\n".join(self.content)
        html = (
            '<div class="vanilla-component-scope vanilla-component vanilla-component--card p-card">'
            f'<h3 class="p-card__title"><a href="{href}">{title}</a></h3>'
            f"<p>{body}</p>"
            f'<p><a href="{href}">Learn more</a></p>'
            "</div>"
        )
        return html_node(html)
