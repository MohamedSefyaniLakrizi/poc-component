"""Sphinx directives for reusable Vanilla Framework components."""

from .accordion import Accordion
from .button import Button
from .card import Card
from .cta import Cta
from .hero import Hero
from .notice import Notice
from .table import Table


def setup(app):
    app.add_directive("vanilla-accordion", Accordion)
    app.add_directive("vanilla-button", Button)
    app.add_directive("vanilla-card", Card)
    app.add_directive("vanilla-cta", Cta)
    app.add_directive("vanilla-hero", Hero)
    app.add_directive("vanilla-notice", Notice)
    app.add_directive("vanilla-table", Table)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
