# FASTA Sequence Analysis Script
# Calculates sequence length and GC content

def analyze_fasta(sequence):
    sequence = sequence.upper().replace("\n", "")
    length = len(sequence)

    gc_count = sequence.count("G") + sequence.count("C")
    gc_content = (gc_count / length) * 100 if length > 0 else 0

    print("Sequence Length:", length)
    print("GC Content: {:.2f}%".format(gc_content))


# Example DNA sequence
sequence = "ATGCGCGTAACCGGTT"

analyze_fasta(sequence)
