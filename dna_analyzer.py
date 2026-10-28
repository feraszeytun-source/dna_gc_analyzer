def analyze_dna(sequence):
    # Clean sequence: convert to uppercase and strip whitespace
    sequence = sequence.upper().strip()
    
    # Calculate sequence length and nucleotide counts
    length = len(sequence)
    a_count = sequence.count('A')
    t_count = sequence.count('T')
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    
    # Calculate GC content percentage
    gc_content = ((g_count + c_count) / length) * 100 if length > 0 else 0
    
    return {
        "Total Length (bp)": length,
        "A": a_count,
        "T": t_count,
        "G": g_count,
        "C": c_count,
        "GC Content (%)": round(gc_content, 2)
    }

# Interactive user input
sample_seq = input("Enter DNA Sequence: ")

# Run analysis
results = analyze_dna(sample_seq)

# Print formatted report
print("\n--- DNA Analysis Report ---")
for key, value in results.items():
    print(f"{key}: {value}")
