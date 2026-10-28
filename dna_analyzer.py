def analyze_dna(sequence):
    # تحويل الأحرف لكبيرة وإزالة المسافات الزائدة
    sequence = sequence.upper().strip()
    
    # حساب أطوال التسلسل وأعداد القواعد النيتروجينية
    length = len(sequence)
    a_count = sequence.count('A')
    t_count = sequence.count('T')
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    
    # حساب نسبة GC
    gc_content = ((g_count + c_count) / length) * 100 if length > 0 else 0
    
    return {
        "Total Length (bp)": length,
        "A": a_count,
        "T": t_count,
        "G": g_count,
        "C": c_count,
        "GC Content (%)": round(gc_content, 2)
    }

# تسلسل تجريبي (جزء من جين TP53 البشري)
sample_seq = "ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCC"

# تشغيل التحليل
results = analyze_dna(sample_seq)

# طباعة التقرير
print("--- DNA Analysis Report ---")
for key, value in results.items():
    print(f"{key}: {value}")
    