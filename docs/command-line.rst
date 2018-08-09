.. _cli:

======================
Command Line Interface
======================

``serpentTools`` includes minor command line functionality. 
Provided you have installed according to :ref:`install`, you can
access this interface with::

    $ python -m serpentTools

.. note:
    
    Outputs here are accurate up to version 0.5.2+14.
    Please alert the developers if any major differences
    are found, or a method to automatically update this
    can be found

Display the available options by passing the ``-h`` flag::

    $ python -m serpentTools -h
    usage: serpentTools [-h] [--version] [-v | -q] [-c CONFIG_FILE]
                        {seed,list} ...

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      -v                    increase verbosity v: info, vv: debug
      -q                    suppress warnings and errors q: error, qq: critical
      -c CONFIG_FILE, --config-file CONFIG_FILE
                            path to settings file

    sub-commands:
      {seed,list}           sub-command help
        seed                copy an input file with unique random number seeds
        list                show the default settings

Random Seed Generation
======================

The ``seed`` subcommand utilizes the :mod:`serpentTools.seed` module to
produced repeated input files with unique random seeds
This is helpful for running repeated analyses to reduce the stochastic nature of
Monte Carlo calculations. Options for forcing the number of digits,
utilizing the ``SERPENT`` 
`include <http://serpent.vtt.fi/mediawiki/index.php/Input_syntax_manual#include_.28read_another_input_file.29>`_
command rather than fully copying the file,
and new output directories are afforded to the user.

.. code::

    $ python -m serpentTools seed -h
    usage: serpentTools seed [-h] [--seed SEED] [-l LENGTH]
                             [--output-dir OUTPUT_DIR] [--link]
                             file N

    positional arguments:
      file                  input file to copy
      N                     integer number of files to create

    optional arguments:
      -h, --help            show this help message and exit
      --seed SEED           Seed to start with the builtin random generator
      -l LENGTH, --length LENGTH
                            Number of digits in random seeds
      --output-dir OUTPUT_DIR
                            Copy files into this directory
      --link                Reference input file with include statement, rather
                            than copying the whole file
