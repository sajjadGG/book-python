Templatetags
============
* https://docs.djangoproject.com/en/dev/ref/templates/builtins/

.. csv-table:: Templatetags
    :header: Argument, Outputs

    openblock	    , {%
    closeblock	    , %}
    openvariable	, {{
    closevariable	, }}
    openbrace	    , {
    closebrace	    , }
    opencomment	    , {#
    closecomment	, #}



Filters
-------
* lower
* upper
* title
* date
* default
* timezone
* custom filters

.. code-block:: django

    {% load tz %}

    {{ value|timezone:"Europe/Paris" }}

.. code-block:: django

    {% load tz %}

    {{ value|utc }}

.. code-block:: django

    {% load tz %}

    {{ value|localtime }}


Float Format
------------
If the argument passed to floatformat has the g suffix, it will force grouping by the THOUSAND_SEPARATOR for the active locale. For example, when the active locale is en (English):

.. csv-table:: Float Format
    :header: Value, Template, Output

    34232.34, {{ value|floatformat:"2g" }}, 34,232.34
    34232.06, {{ value|floatformat:"g" }}, 34,232.1
    34232.00, {{ value|floatformat:"-3g" }}, 34,232


Simple Tags
-----------
* trans
* custom tags


Assignment tags
---------------



Block tags
----------
* custom block tags

.. code-block:: django

    {% load tz %}

    {% localtime on %}
        {{ value }}
    {% endlocaltime %}

    {% localtime off %}
        {{ value }}
    {% endlocaltime %}

.. code-block:: django

    {% load tz %}

    {% timezone "Europe/Paris" %}
        Paris time: {{ value }}
    {% endtimezone %}

    {% timezone None %}
        Server time: {{ value }}
    {% endtimezone %}
