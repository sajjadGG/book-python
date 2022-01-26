UML ERD
=======


Rationale
---------
* UML - Unified Modeling Language
* ERD - Entity Relationship Diagram


Mermaid
-------
* ``mermaid`` - Markdown extension
* https://mermaid-js.github.io/mermaid/#/entityRelationshipDiagram

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
* Entity Relationship
* Database

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
.. [#mermaidTheme] Sveidqvist, Knut et al. Mermaid Documentation. Retrieved: 2022-01-26. Year: 2022. URL: https://mermaid-js.github.io/mermaid/#/theming
.. [#mermaidConfig] Sveidqvist, Knut et al. Mermaid Documentation. Retrieved: 2022-01-26. Year: 2022. URL: https://mermaid-js.github.io/mermaid/#/n00b-syntaxReference
