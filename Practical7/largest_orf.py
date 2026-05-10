import re

seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

pattern = r'AUG(?:...)*?(?:UAA|UAG|UGA)'
# non-capturing group combined with a quantifier
orfs = re.findall(pattern, seq)

if orfs:
    longest_orf = max(orfs, key=len)
    print(f"The largest ORF is {len(longest_orf)} nucleotides long.")
    print(f"ORF sequence: {longest_orf}")
else:
    print("No ORF found.")