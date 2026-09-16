import unittest

from docutils.core import publish_parts


class ComponentDirectiveTests(unittest.TestCase):
    def render(self, source):
        import component

        class App:
            def add_directive(self, name, directive):
                from docutils.parsers.rst import directives

                directives.register_directive(name, directive)

        component.setup(App())
        return publish_parts(source=source, writer_name="html5")["html_body"]

    def test_directives_render_vanilla_framework_components(self):
        html = self.render(
            """
.. vanilla-hero:: Documentation components
   :summary: Reusable, static components for Sphinx.
   :primary-label: Get started
   :primary-url: /getting-started/
   :secondary-label: Learn more
   :secondary-url: /learn-more/

.. vanilla-card:: Fast setup
   :href: /setup/

   Build a documentation site with a reusable card.

.. vanilla-notice::
   :title: Preview
   :kind: caution

   Components are rendered during the Sphinx build.

.. vanilla-cta:: Ready to build?
   :label: View the guide
   :href: /guide/
"""
        )

        self.assertIn(
            "vanilla-component-scope vanilla-component vanilla-component--hero",
            html,
        )
        self.assertIn("p-card", html)
        self.assertIn("p-notification--caution", html)
        self.assertIn("p-button--positive", html)
        self.assertIn('href="/guide/"', html)

    def test_small_components_render_reusable_markup(self):
        html = self.render(
            """
.. vanilla-button:: View the guide
   :href: /guide/
   :kind: primary

.. vanilla-accordion:: What is a component?

   A reusable documentation building block.

.. vanilla-table::
   :headers: Component | Purpose

   Button | Links to a guide
   Accordion | Reveals supporting content
"""
        )

        self.assertIn("vanilla-component--button", html)
        self.assertIn("p-button--positive", html)
        self.assertIn("vanilla-component--accordion", html)
        self.assertIn("<details", html)
        self.assertIn("<summary>What is a component?</summary>", html)
        self.assertIn("vanilla-component--table", html)
        self.assertIn("<th>Component</th>", html)
        self.assertIn("<td>Accordion</td>", html)

    def test_public_component_classes_have_clear_names(self):
        from component.accordion import Accordion
        from component.button import Button
        from component.card import Card
        from component.cta import Cta
        from component.hero import Hero
        from component.notice import Notice
        from component.table import Table

        for component in (Accordion, Button, Card, Cta, Hero, Notice, Table):
            self.assertEqual(component.__name__, component.__name__.title())


if __name__ == "__main__":
    unittest.main()
