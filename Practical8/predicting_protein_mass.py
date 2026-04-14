ALLaa = {
   'G': 57.02,   # Glycine
    'A': 71.04,   # Alanine
    'S': 87.03,   # Serine  
    'P': 97.05,   # Proline
    'V': 99.07,   # Valine
    'T': 101.05,  # Threonine
    'C': 103.01,  # Cysteine
    'I': 113.08,  # Isoleucine
    'L': 113.08,  # Leucine
    'N': 114.04,  # Asparagine
    'D': 115.03,  # Aspartic Acid
    'Q': 128.06,  # Glutamine
    'K': 128.09,  # Lysine
    'E': 129.04,  # Glutamic Acid
    'M': 131.04,  # Methionine
    'H': 137.06,  # Histidine
    'F': 147.07,  # Phenylalanine
    'R': 156.10,  # Arginine
    'Y': 163.06,  # Tyrosine
    'W': 186.08   # Tryptophan
}


def prepromas():
    """Calculate the mass of a protein based on its amino acid sequence."""
    ipsq = input("Enter your a.a. sequence: ")
    if any(aa not in ALLaa.keys() for aa in list(ipsq)):
        return "ERROR:not a valid sequence"
    else:
        mass = 0
        for aa in ipsq:
            mass += ALLaa[aa]
        return round(mass,2)

    


print(prepromas())
