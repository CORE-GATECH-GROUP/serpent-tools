"""Parser responsible for reading the ``*coe.m`` files"""

from serpentTools.objects.readers import BaseReader


class BranchingReader(BaseReader):
    """
    Parser responsible for reading and working with automated branching files.

    Parameters
    ----------
    filePath: str
        path to the depletion file
    """
    pass

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
