#assuming FASTS files in dict in header:sequence key:value pairs

def calculate_gc_content(sequence):
    return '{:.2%}'.format((sequence.upper().count('G') + sequence.upper().count('C')) / len(sequence))

def compare_gc(sequences):
    # takes dict of format header:sequence
    for header, seq in sequences.items():
        print(header, calculate_gc_content(seq))

compare_gc(seqs_dict)
