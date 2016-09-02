import sys
lines = sys.stdin.read().splitlines() 
pattern = lines[0]
d = int(lines[1])

def hamming_distance(p,q):
    mismatch = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            mismatch +=1
    return mismatch

def neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
        
    neighborhood = set()
    nucleotide = ['A', 'C', 'G', 'T']
    suffix_neighbors = neighbors(pattern[1:], d)

    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for e in nucleotide:
                neighborhood.add(e+text)
        else:
            neighborhood.add(pattern[0]+text)
    return neighborhood

print("\n".join(neighbors(pattern,d)))
