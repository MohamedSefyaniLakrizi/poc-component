"""Shared helpers for Vanilla Framework component directives."""

from docutils import nodes


def link(url, label, class_name):
    return f'<a class="{class_name}" href="{url}">{label}</a>'


def html_node(html):
    return [nodes.raw("", html, format="html")]
