"""Parser responsible for reading the ``*bumat<n>.m`` files"""
debugserpentoutput=False
from serpentTools.objects.readers import MaterialReader


class BumatReader(MaterialReader):
    """
    Parser responsible for reading and working with burned material files.

    Parameters
    ----------
    filePath: str
        path to the depletion file
    """

    def __init__(self, 

    if materialname==None or materialfile==None:
        raise Exception("A material file and material name in that file must be specified in order to read in serpent material data as a salt.")
    debugserpentoutput=False #debug
    self.materialname=materialname

    with open(self.directory+'/'+materialfile, 'r') as bumat_file:

        #this for loop will iterate through all lines in the
        #burned material output
        on_correct_material=False #used to see if the line has isotopes fractions to be read in
        for line in bumat_file.readlines():
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
                if debugserpentoutput:
                    print("finished finding material {0}".format(materialname))
                break #leave the for loop, material was found
            if line[:3]=='mat':

                line.rstrip() #remove trailing whitespace
                #split the line to read in separate words.
                splitline=line.split() #now is list data type
                thismaterialname=splitline[1] #grab material name
                if debugserpentoutput:
                    print("found material {0}".format(thismaterialname))
                #if the material here is the one that we want to
                #read, record the atom density and other data. begin recording isotopics
                if debugserpentoutput:
                    print("now comparing:")
                    print(thismaterialname)
                    print(materialname)
                if thismaterialname==materialname:
                    on_correct_material=True
                    self.atomdensity=float(splitline[2])
                    if debugserpentoutput:
                        print("these two should match: ---------")
                        print(float(splitline[2]))
                        print(self.atomdensity)
                        print("these three should match: --------")
                        print(thismaterialname)
                        print(self.materialname)
                        print(materialname)
                        print("data from line:")
                        print(splitline)
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
        print("unable to read density of material {0}".format(materialname))
        raise Exception("An error was encountered in reading the material's density.")
