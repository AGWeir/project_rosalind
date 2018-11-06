"""
Problem

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s
"""

dna_seq = 'AAAACCCGGT'
def reverse_complement(dna_seq):
    compliments = [('A','t'),('G','c'),('T','a'),('C','g')]
    reverse = dna_seq[::-1]
    for x in compliments:
        reverse = reverse.replace(x[0],x[1])
    return reverse.upper()

reverse_complement(dna_seq)
