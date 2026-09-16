Component examples
==================

This page demonstrates small, reusable Sphinx directives. Each directive
produces static HTML styled with a scoped Canonical-inspired component stylesheet.

Hero
----

.. vanilla-hero:: Documentation building blocks
   :summary: Reusable, static components for clear and consistent documentation.
   :primary-label: Get started
   :primary-url: /tutorials/
   :secondary-label: Browse reference
   :secondary-url: /reference/

Buttons
-------

.. vanilla-button:: Primary action
   :href: /tutorials/
   :kind: primary

.. vanilla-button:: Secondary action
   :href: /reference/
   :kind: secondary

.. vanilla-button:: Destructive action
   :href: /contribute/
   :kind: negative

Card
----

.. vanilla-card:: Fast setup
   :href: /how-to/

   Start with a focused guide and adapt the component's content for your project.

Accordion
---------

.. vanilla-accordion:: What is a component?

   A reusable documentation building block with a focused purpose and a stable
   authoring interface. This accordion uses native HTML, so it works without
   JavaScript.

Table
-----

.. vanilla-table::
   :headers: Component | Purpose | JavaScript required

   Button | Links to another page or action | No
   Accordion | Reveals supporting content | No
   Table | Presents structured comparisons | No

Notice
------

.. vanilla-notice::
   :title: Build-time components
   :kind: information

   These components are rendered into static HTML during the Sphinx build. They
   do not require a client-side framework.

Call to action
--------------

.. vanilla-cta:: Ready to build documentation?
   :label: View the tutorials
   :href: /tutorials/
