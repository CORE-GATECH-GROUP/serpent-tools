ZAI_MAP = {
    1: "H",
    2: "He",
    3: "Li",
    4: "Be",
    5: "B",
    6: "C",
    7: "N",
    8: "O",
    9: "F",
    10: "Ne",
    11: "Na",
    12: "Mg",
    13: "Al",
    14: "Si",
    15: "P",
    16: "S",
    17: "Cl",
    18: "Ar",
    19: "K",
    20: "Ca",
    21: "Sc",
    22: "Ti",
    23: "V",
    24: "Cr",
    25: "Mn",
    26: "Fe",
    27: "Co",
    28: "Ni",
    29: "Cu",
    30: "Zn",
    31: "Ga",
    32: "Ge",
    33: "As",
    34: "Se",
    35: "Br",
    36: "Kr",
    37: "Rb",
    38: "Sr",
    39: "Y",
    40: "Zr",
    41: "Nb",
    42: "Mo",
    43: "Tc",
    44: "Ru",
    45: "Rh",
    46: "Pd",
    47: "Ag",
    48: "Cd",
    49: "In",
    50: "Sn",
    51: "Sb",
    52: "Te",
    53: "I",
    54: "Xe",
    55: "Cs",
    56: "Ba",
    57: "La",
    58: "Ce",
    59: "Pr",
    60: "Nd",
    61: "Pm",
    62: "Sm",
    63: "Eu",
    64: "Gd",
    65: "Tb",
    66: "Dy",
    67: "Ho",
    68: "Er",
    69: "Tm",
    70: "Yb",
    71: "Lu",
    72: "Hf",
    73: "Ta",
    74: "W",
    75: "Re",
    76: "Os",
    77: "Ir",
    78: "Pt",
    79: "Au",
    80: "Hg",
    81: "Tl",
    82: "Pb",
    83: "Bi",
    84: "Po",
    85: "At",
    86: "Rn",
    87: "Fr",
    88: "Ra",
    89: "Ac",
    90: "Th",
    91: "Pa",
    92: "U",
    93: "Np",
    94: "Pu",
    95: "Am",
    96: "Cm",
    97: "Bk",
    98: "Cf",
    99: "Es",
    100: "Fm",
    101: "Md",
    102: "No",
    103: "Lr",
    104: "Rf",
    105: "Db",
    106: "Sg",
    107: "Bh",
    108: "Hs",
    109: "Mt",
    110: "Ds",
    111: "Rg",
    112: "Cn",
    113: "Nh",
    114: "Fl",
    115: "Mc",
    116: "Lv",
    117: "Ts",
    118: "Og",
}


def decodeZai(zai):
    """
    Return a compact isotope label from a ZAI/ZA identifier.

    Parameters
    ----------
    zai : str or int
        Isotope identifier as ``ZZAAA`` or ``ZZAAAI``.
        If an isomeric state is present, an ``m#`` suffix is used.

    Returns
    -------
    str
        Isotope label such as ``²³⁵U`` or ``²³⁵Um1``. Returns the input
        string if decoding fails.
    """
    if zai is None:
        return ""
    zai_str = "".join(ch for ch in str(zai).strip() if ch.isdigit())
    if len(zai_str) < 4:
        return str(zai).strip()

    if len(zai_str) >= 6:
        z = int(zai_str[:-4])
        a = int(zai_str[-4:-1])
        isomer = int(zai_str[-1])
    else:
        z = int(zai_str[:-3])
        a = int(zai_str[-3:])
        isomer = 0

    symbol = ZAI_MAP.get(z)
    if symbol is None:
        return str(zai).strip()

    superscripts = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    mass = str(a).translate(superscripts)
    label = "{}{}".format(mass, symbol)
    if isomer:
        label = "{}m{}".format(label, isomer)
    return label
