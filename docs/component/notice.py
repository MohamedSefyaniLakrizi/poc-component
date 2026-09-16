"""Notice component directive."""

from docutils.parsers.rst import Directive, directives

from .base import html_node


class Notice(Directive):
    """Render a Vanilla Framework notification."""

    has_content = True
    option_spec = {
        "title": directives.unchanged_required,
        "kind": lambda value: directives.choice(
            value, ("information", "positive", "caution", "negative")
        ),
    }

    def run(self):
        body = "\n".join(self.content)
        kind = self.options.get("kind", "information")
        html = (
            f'<div class="vanilla-component-scope vanilla-component vanilla-component--notice p-notification--{kind}">'
            '<div class="p-notification__content">'
            f'<h5 class="p-notification__title">{self.options["title"]}</h5>'
            f'<p class="p-notification__message">{body}</p>'
            "</div></div>"
        )
        return html_node(html)
