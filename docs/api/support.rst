
Supporting Objects
==================

.. autoclass:: serpentTools.objects.materials.DepletedMaterial

.. note::

    These attributes only exist if the pasers was instructed to
    read in this data. I.e. if ``readers.depletion.metadataKeys``
    does not contain ``ZAI``, then this object will not have
    the ``zai`` data.