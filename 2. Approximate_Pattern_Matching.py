import sys
lines = sys.stdin.read().splitlines() 
pattern = lines[0]
text = lines[1]
d = int(lines[2])

def hamming_distance(p,q):
    mismatch = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            mismatch +=1
    return mismatch

def approximate_pattern_matching(pattern, text, d):
    start_position = []
    sub_string = [None]*(len(text)-len(pattern)+1)
    for i in range(len(text)-len(pattern)+1):
        sub_string[i] = text[i:i+len(pattern)]   
        if hamming_distance(pattern, sub_string[i]) <= d:
            start_position.append(i)
    return " ".join(str(e) for e in start_position)

print (approximate_pattern_matching(pattern, text, d))


# - Sample Input: ATTCTGGA  CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT  3
# - Sample Output: 6 7 26 27
