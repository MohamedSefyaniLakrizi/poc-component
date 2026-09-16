"""Hero component directive."""

from docutils.parsers.rst import Directive, directives

from .base import html_node, link


class Hero(Directive):
    """Render a Vanilla Framework hero strip."""

    required_arguments = 1
    final_argument_whitespace = True
    has_content = False
    option_spec = {
        "summary": directives.unchanged_required,
        "primary-label": directives.unchanged_required,
        "primary-url": directives.uri,
        "secondary-label": directives.unchanged,
        "secondary-url": directives.uri,
    }

    def run(self):
        actions = link(
            self.options["primary-url"],
            self.options["primary-label"],
            "p-button--positive",
        )
        if "secondary-label" in self.options and "secondary-url" in self.options:
            actions += " " + link(
                self.options["secondary-url"],
                self.options["secondary-label"],
                "p-button",
            )
        html = (
            '<section class="vanilla-component-scope vanilla-component vanilla-component--hero p-strip--accent">'
            '<div class="row"><div class="col-8">'
            f"<h1>{self.arguments[0]}</h1><p>{self.options['summary']}</p>"
            f'<p class="u-no-margin--bottom">{actions}</p>'
            "</div></div></section>"
        )
        return html_node(html)
