Theory UML ERD
==============


Rationale
---------
* UML - Unified Modeling Language
* ERD - Entity Relationship Diagram


Mermaid
-------
* ``mermaid`` - Markdown extension [#mermaidAbout]_

Theming [#mermaidTheme]_:

.. code-block:: md

    %%{init: { 'theme': 'dark' } }%%
    %%{init: { 'theme': 'forest' } }%%

Config [#mermaidConfig]_:

.. code-block:: md

    %%{init: { 'logLevel': 'debug' } }%%
    %%{config: { 'fontFamily': 'Menlo', 'fontSize': 18, 'fontWeight': 400} }%%


Entity Relationship Diagram
---------------------------
* ERD - Entity Relationship Diagram [#mermaidERD]_

.. code-block:: md

    ```mermaid
      erDiagram

        CUSTOMER }|..|{ DELIVERY-ADDRESS : has
        CUSTOMER ||--o{ ORDER : places
        CUSTOMER ||--o{ INVOICE : "liable for"
        DELIVERY-ADDRESS ||--o{ ORDER : receives
        INVOICE ||--|{ ORDER : covers
        ORDER ||--|{ ORDER-ITEM : includes
        PRODUCT-CATEGORY ||--|{ PRODUCT : contains
        PRODUCT ||--o{ ORDER-ITEM : "ordered in"
    ```

.. figure:: img/uml-mermaid-erd.png


References
----------
.. [#mermaidAbout] Sveidqvist, Knut et al. Mermaid Documentation: About. Year: 2022. Retrieved: 2022-01-26. URL: https://mermaid-js.github.io/mermaid/#/README
.. [#mermaidTheme] Sveidqvist, Knut et al. Mermaid Documentation: Theming. Year: 2022. Retrieved: 2022-01-26. URL: https://mermaid-js.github.io/mermaid/#/theming
.. [#mermaidConfig] Sveidqvist, Knut et al. Mermaid Documentation: SyntaxReference. Year: 2022. Retrieved: 2022-01-26. URL: https://mermaid-js.github.io/mermaid/#/n00b-syntaxReference
.. [#mermaidERD] Sveidqvist, Knut et al. Mermaid Documentation: Entity Relationship Diagrams. Year: 2022. Retrieved: 2022-01-26. URL: https://mermaid-js.github.io/mermaid/#/entityRelationshipDiagram
