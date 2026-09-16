"""Table component directive."""

from docutils.parsers.rst import Directive, directives

from .base import html_node


class Table(Directive):
    """Render a compact table from pipe-separated headings and rows."""

    has_content = True
    option_spec = {"headers": directives.unchanged_required}

    @staticmethod
    def cells(value):
        return [cell.strip() for cell in value.split("|")]

    def run(self):
        headers = self.cells(self.options["headers"])
        rows = [self.cells(row) for row in self.content if row.strip()]
        if any(len(row) != len(headers) for row in rows):
            raise self.error("Each table row must contain the same number of cells as :headers:.")

        header_html = "".join(f"<th>{header}</th>" for header in headers)
        row_html = "".join(
            "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
            for row in rows
        )
        html = (
            '<div class="vanilla-component-scope vanilla-component vanilla-component--table p-table-wrapper">'
            '<table class="p-table"><thead><tr>'
            f"{header_html}</tr></thead><tbody>{row_html}</tbody></table></div>"
        )
        return html_node(html)
