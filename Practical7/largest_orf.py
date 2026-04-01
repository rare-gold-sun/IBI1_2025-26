seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

import re
ORF = re.findall('AUG.*UAA|AUG.*UAG|AUG.*UGA', seq)
bp = len(ORF[0])
print(ORF)
print(bp)