def count_nucleotides(dna_sequence):
    count_A = dna_sequence.count('A')
    count_C = dna_sequence.count('C')
    count_G = dna_sequence.count('G')
    count_T = dna_sequence.count('T')

    return count_A, count_G, count_T, count_C

dna_sequence = "ACACGTCGTACGTACGTGATC"

result = count_nucleotides(dna_sequence)
print(result)