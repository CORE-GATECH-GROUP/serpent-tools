"""Parser responsible for reading the ``*coe.m`` files"""

from serpentTools.objects.readers import XSReader


class BranchingReader(XSReader):
    """
    Parser responsible for reading and working with automated branching files.

    Parameters
    ----------
    filePath: str
        path to the depletion file
    """

    def __init__(self, filePath):
        XSReader.__init__(self, filePath, 'branching')

    def write(self, template=None):
        """
        Write the data from the branching sequence using a specified template.

        Parameters
        ----------
        template: str
            Will attempt to make a template in the following order:

                #. By reading the template from the file pointed to by
                   ``template``, or
                #. Making a template directly from the string

            If neither of these succeeds, the method will fail and raise an
            exception.

        Returns
        -------

        """
        raise NotImplementedError

def print_coe(coedict, short=True):
    """ Pretty prints a dictionary returned
    by parse_coe. Use this to visualize its
    nested structure.

    This function wraps __print_coe_sub so that
    its __print_coe_sub's recursive argument gets
    hidden.

    Parameters
    ----------
    coedict : dict
        particularly, one returned by parse_coe,
        although it will work on any nested dict.
    short : bool
        short print, only prints first few params
        found. Set to false for a full STDOUT.

    Returns
    -------
    None
    """
    __print_coe_sub(coedict, lvl=0, short=short)

def __print_coe_sub(coedict, lvl=0, short=True):
    """ Recursive function used in print_coe.
    """
    keys = list(coedict.keys())
    if isinstance(coedict[keys[0]], Mapping):
        for k in keys:
            print(str('    '*lvl) + str(k))
            __print_coe_sub(coedict[k], lvl=lvl+1)
    else:
        if short:
            keys = keys[:5]
        for k in keys:
            print(str('    '*lvl) + str(k) + ' : ' + str(coedict[k]))
