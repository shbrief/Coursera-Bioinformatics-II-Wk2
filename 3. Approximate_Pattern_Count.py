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

def approximate_pattern_count(pattern, text, d):
    count = 0
    sub_string = [None]*(len(text)-len(pattern)+1)
    for i in range(len(text)-len(pattern)+1):
        sub_string[i] = text[i:i+len(pattern)]
        if hamming_distance(pattern, sub_string[i]) <= d:
            count += 1
    return count 

print (approximate_pattern_count(pattern, text, d))


# - Sample Input: GAGG  TTTAGAGCCTTCAGAGG  2
# - Sample Output: 4
