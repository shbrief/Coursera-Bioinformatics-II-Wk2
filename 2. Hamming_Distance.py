import sys
lines = sys.stdin.read().splitlines() # read in the input from STDIN
p = lines[0]
q = lines[1]

def hamming_distance(p,q):
    mismatch = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            mismatch +=1
    return mismatch

print(hamming_distance(p,q))
