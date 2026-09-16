"""Call-to-action component directive."""

from docutils.parsers.rst import Directive, directives

from .base import html_node, link


class Cta(Directive):
    """Render a Vanilla Framework call-to-action strip."""

    required_arguments = 1
    final_argument_whitespace = True
    has_content = False
    option_spec = {
        "label": directives.unchanged_required,
        "href": directives.uri,
    }

    def run(self):
        html = (
            '<section class="vanilla-component-scope vanilla-component vanilla-component--cta p-strip is-deep">'
            '<div class="row">'
            f'<div class="col-8"><h2>{self.arguments[0]}</h2></div>'
            '<div class="col-4 u-vertically-center">'
            f'{link(self.options["href"], self.options["label"], "p-button--positive")}'
            "</div></div></section>"
        )
        return html_node(html)
