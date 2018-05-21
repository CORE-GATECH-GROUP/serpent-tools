
{% extends 'rst.tpl' %}

{# update code block #}
{% block input scoped-%}
{%- if cell.source.strip() -%}
.. code:: 
    
{% for line in cell.source.split('\n') %}
{%- if line[0] == ' ' -%}
{{ ("... " + line) |indent}}
{%- else -%}
{{ (">>> " + line) |indent}}
{%- endif %}
{% endfor -%}
{%- endif -%}
{%- endblock input -%}