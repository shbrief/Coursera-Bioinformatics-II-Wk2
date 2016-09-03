from collections import defaultdict

def freq_words_mismatch_ref(Text, k, d):
    freq_pattern = defaultdict(int)
    for i in range(len(Text)-k+1):
        pattern = Text[i:i+k]
        freq_pattern[pattern] += 1
    mismatch_count = defaultdict(int)
    for pattern, freq in freq_pattern.items():
        for mismatch in neighbors(pattern, d):
            mismatch_count[mismatch] += freq
    max_count = max(mismatch_count.values())
    return sorted([kmer for kmer, count in mismatch_count.items() if count == max_count])
        
