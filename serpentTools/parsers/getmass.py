# This python function can grab isotope masses from the NIST isotopic data file found in this directory.

# definitely should have written something that uses regexes......too late :(
import os
# where is data file? This finds it.
dir_path = os.path.dirname(os.path.realpath(__file__)) 
datafile = dir_path + '/nistmasses.txt' # isotopic masses


def getIsoMass(zaid):
    """ grabs an isotopes mass in AMU. zaid should be in serpent format"""
    zaid = str(zaid) #coerce as string. serves as error checker/conversion

    #get z/a value
    if len(zaid) ==4:
        z=zaid[0]
        a=zaid[-2:]
        #remove leading zero if necessary
        if a[0]=='0':
            a=a[-1]
    elif len(zaid) ==5:
        z=zaid[:2]
        a=zaid[-3:]
        #leading zero maybe
        if a[0]=='0':
            a=a[-2:]
    else:
        raise Exception("Unidentifiable isotope {}".format(zaid) )

    # check if the nuclide is natural
    if '000' in zaid:
        return getNaturalMass(zaid, z)

    # now search the data file
    # should be the isotope mass one from the NIST website
    with open(datafile, 'r') as f:
        current_z='  '
        while current_z != z:
            l=next(f)
            current_z = l[-3:]
            current_z = current_z[:2] #remove newline
            current_z = current_z[-1] if current_z[0]==' ' else current_z
            if z != '1':
                while l != '\n' :
                    try:
                        l=next(f)
                    except StopIteration:
                        raise Exception("isotope {} not found".format(zaid))

        # ok, now we're on the right Z val. now just search for the right A.
        current_a = ''
        while current_a != a:
            try:
                l=next(f)
            except StopIteration:
                return 0.0
                #raise Exception('mass number not found for {}'.format(zaid))
            if l[:4]=='Mass':
                current_a = l[-4:]
                current_a = current_a[:3] # remove \n
                if current_a[:2]=='= ':
                    current_a=current_a[-1]
                elif current_a[0]==' ':
                    current_a=current_a[1:]

        # now finish the search by moving down one line.
        l=next(f)
        l=l.split()[4].split('(')[0]
        mass=float(l)
            


    return mass 

def getNaturalMass(zaid, z):
    """gets mass of a natural isotope. this is really meant
    to just be called by getIsoMass, so please use that function
    instead. """

    abundances = {}
    # add abundances by {zaid:abundance} pairs
    with open(datafile, 'r') as f:
        current_z='  '
        while current_z != z:
            l=next(f)
            current_z = l[-3:]
            current_z = current_z[:2] #remove newline
            current_z = current_z[-1] if current_z[0]==' ' else current_z
            if z != '1':
                while l != '\n' :
                    try:
                        l=next(f)
                    except StopIteration:
                        raise Exception("isotope {} not found".format(zaid))

        while current_z == z:
            l=next(f)
            current_z = l[-3:]
            current_z = current_z[:2] #remove newline
            current_z = current_z[-1] if current_z[0]==' ' else current_z
            if z != '1':
                while l != '\n' :
                    try:
                        l=next(f)
                        
                        if l[:4] == 'Mass':
                            current_a = l[-4:]
                            current_a = current_a[:3] # remove \n
                            if current_a[:2]=='= ':
                                current_a=current_a[-1]
                            elif current_a[0]==' ':
                                current_a=current_a[1:]

                        lsplit = l.split()
                        if len ( lsplit ) == 3 or lsplit == []:
                            continue # isotope does not occur in nature
                        try:
                            if lsplit[0]+lsplit[1] == 'IsotopicComposition':
                                thisZaid = str( int(z)*1000 + int(current_a) )
                                abundances[thisZaid] = float( lsplit[3].split('(')[0] )
                        except IndexError:
                            raise Exception('couldnt find abundance {}'.format(lsplit))
                    except StopIteration:
                        raise Exception("isotope {} not found".format(zaid))

    natMass = 0.0

    # add all weighted masses then
    for key in abundances.keys():
        natMass += getIsoMass(key) * abundances[key]

    return natMass

# run some examples
if __name__=='__main__':
    print('uranium 235: {}'.format(getIsoMass('92235')))
    print('H {}:'.format(getIsoMass('1001')))
    print('Kr 73: {}'.format(getIsoMass('36073')))
    print('Kr 79: {}'.format(getIsoMass('36078')))


