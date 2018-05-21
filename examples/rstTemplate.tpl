
{% extends 'rst.tpl' %}

{# update code block #}
{% block input scoped-%}
{%- if cell.source.strip() -%}
.. code:: 
    
{% for line in cell.source.split('\n') -%}
{%- if line[0] == ' ' -%}
{{ ("... " + line) |indent}}
{%- else -%}
{{ (">>> " + line) |indent}}
{%- endif %}
{% endfor -%}
{%- endif -%}
{%- endblock input -%}
    
{% block stream %}
.. parsed-literal::
 
{{ renderOutput(output.text) }}
{% endblock stream %}
    
{% block data_text scoped %}
.. parsed-literal::
 
{{ renderOutput(output.data['text/plain']) }}
{% endblock data_text %}
    
{% macro renderOutput(values) -%}
{% if "array" in values -%}
{{ values | indent }}
{% else %}
{{ values | wordwrap | indent }}
{% endif %}
{%- endmacro %}