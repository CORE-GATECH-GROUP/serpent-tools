"""Parser responsible for reading the ``*bumat<n>.m`` files"""
from serpentTools.objects.readers import MaterialReader
from serpentTools.settings.messages import debug, error

class BumatReader(MaterialReader):
    """
    Parser responsible for reading and working with burned material files.

    Parameters
    ----------
    filePath: str
        path to the depletion file
    """

    def __init__(self, filePath, readerSettingsLevel):
        MaterialReader.__init__(self, filePath, readerSettingsLevel)
        self.filePath = filePath
        self.grabMaterials()
        self.data['materialnames'] = [] # mat names found in file
        for matname in self.materials.keys():
            self.read1mat(matname)

    def grabMaterials(self):
        """ Searches for all material names present in a bumat file."""

        # loop through file
        with open(self.filePath, 'r') as bumat_file:
            for line in bumat_file:
                if line[:3]=='mat':
                    line.rstrip()
                    splitline = line.split()
                    thismaterial = splitline[1]

                    # important part:
                    self.data['materialnames'].append(thismaterial)

        # ensure all names unique
        # set conversion keeps only unique values
        u = len(self.data['materialnames'])>len(set(self.data['materialnames']))
        if not u:
            error("Non-unique material names in {}".format(filePath))


    def read1mat(self, materialname):
        """ reads one material composition from the bumat file
        """
        if materialname==None or materialfile==None:
            raise Exception("A material file and material name in that file must be specified in order to read in serpent material data as a salt.")
        self.materialname=materialname

        with open(self.directory+'/'+materialfile, 'r') as bumat_file:

            #this for loop will iterate through all lines in the
            #burned material output
            on_correct_material=False #used to see if the line has isotopes fractions to be read in
            for line in bumat_file:
                if '%' ==line[0]:
                    continue #skip comments
                #see if the line defines a material. if it is the one
                #of interest, record its isotopics, atom density, temp
                #library, etc.

                #firstly, if the correct material was already found,
                #and the current line is a new material definition,
                #then this loop is done reading for the material of
                #interest.

                if (line[:3]=='mat' or line[:3]=='set') and on_correct_material:
                    debug("finished finding material {0}".format(materialname))
                    break #leave the for loop, material was found
                if line[:3]=='mat':

                    line.rstrip() #remove trailing whitespace
                    #split the line to read in separate words.
                    splitline=line.split() #now is list data type
                    thismaterialname=splitline[1] #grab material name
                    debug("found material {0}".format(thismaterialname))

                    #if the material here is the one that we want to
                    #read, record the atom density and other data. begin recording isotopics
                    debug("now comparing:")
                    debug(thismaterialname)
                    debug(materialname)
                    if thismaterialname==materialname:
                        on_correct_material=True
                        self.atomdensity=float(splitline[2])
                        debug("these two should match: ---------")
                        debug(float(splitline[2]))
                        debug(self.atomdensity)
                        debug("these three should match: --------")
                        debug(thismaterialname)
                        debug(self.materialname)
                        debug(materialname)
                        debug("data from line:")
                        debug(splitline)

                        if 'vol' in splitline:

                            #now grab the material volume
                            i=0
                            for item in splitline:
                                if item== 'vol':
                                    break
                                i+=1
                            self.volume=float(splitline[i+1])
                        if 'tmp' in splitline or 'tms' in splitline:
                            i=0
                            for item in splitline:
                                if item=='tmp' or item=='tms':
                                    break
                                i+=1
                            self.tempK=float(splitline[i+1])
                        if self.atomdensity < 0.0:
                            self.massdensity=-1. * self.atomdensity
                            self.atomdensity=None
                        if self.atomdensity==0.0:
                            self.massdensity=0.0
                        continue

                #if on the correct material, then read in whatever isotope is encountered.
                if on_correct_material:
                    line.rstrip() #remove trailing whitespace
                    line=line.split() #turn into list format
                    line=[i for i in line if i!='']#remove blank space

                    if line==[] or line[0]=='therm':
                        continue #pass blank line or thermal scattering library
                    zaid=line[0] #should contain ZAID first
                    atomfraction=line[1] #then fraction
                    #now strip off the temp library.
                    #assuming it is just the last
                    #four chars in the zaid string.
                    zaid=zaid[:-4]
                    #now add it on to the material definition within this object.
                    self.isotopic_content[zaid]=float(atomfraction)
        if self.atomdensity == None and self.massdensity ==None:
            error("An error was encountered in reading the material {}'s density."
                  .format(materialname) )

    debug('Read material {}'.format(materialname))
