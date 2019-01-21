.. _cli:

======================
Command Line Interface
======================

``serpentTools`` includes minor command line functionality. 
Provided you have installed according to :ref:`install`, you can
access this interface with::

    $ python -m serpentTools

.. note::
    
    Outputs here are accurate up to version ``0.6.1+12``
    Please alert the developers if any major differences
    are found, or a method to automatically update this
    can be found

Display the available options by passing the ``-h`` flag::

    $ python -m serpentTools -h
     usage: serpentTools [-h] [--version] [-v | -q] [-c CONFIG_FILE]
                         {seed,list,to-matlab} ...

     optional arguments:
       -h, --help            show this help message and exit
       --version             show program's version number and exit
       -v                    increase verbosity v: info, vv: debug
       -q                    suppress warnings and errors q: error, qq: critical
       -c CONFIG_FILE, --config-file CONFIG_FILE
                             path to settings file

     sub-commands:
       {seed,list,to-matlab}
                             sub-command help
         seed                copy an input file with unique random number seeds
         list                show the default settings
         to-matlab           convert output file to .mat file

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

.. _cli-to-matlab:

Conversion to Binary ``.mat`` files
===================================

Starting in version :release-tag:`0.6.2`, ``serpentTools`` can convert text
SERPENT output files and convert them to binary ``.mat`` files. This relies upon
:term:`scipy`, and can be called from the command line as follows:

.. code::

    $ python -m serpentTools to-matlab -h
    usage: serpentTools to-matlab [-h] [-o OUTPUT] [-a] [--format {4,5}] [-l]
                                  [--large] [--oned {col,row}]
                                  file
    
    positional arguments:
      file                  output file to read and convert
    
    optional arguments:
      -h, --help            show this help message and exit
      -o OUTPUT, --output OUTPUT
                            Name of output file to write. If not given, replace
                            extension with .mat
      -a, --append          Append to existing file if found. Otherwise overwrite.
                            Default: False
      --format {4,5}        Format of file to write. 4 for MATLAB 4, 5 for MATLAB
                            5+. Default: 5
      -l, --longNames       Allow variable names up to 63 characters. Otherwise,
                            enforce 31 character names. Default: False
      --large               Don't compress arrays when writing.
      --oned {col,row}      Write 1D arrays are row or column vectors

Conversion will exit with no errors if the file is able to be converted, or with
the following exit codes:

   * ``1``: :term:`scipy` not found
   * ``3``: That file type is not supported at this time.

If you desperately need a file type to be converted, please reach out to the developers
on the `GH Issue board <https://www.github.com/CORE-GATECH-GROUP/serpent-tools/issues>`_.
Alternatively, if you're feeling ambitious, follow through the :ref:`dev-guide` for guidelines
on adding the feature and submitting a pull request.
