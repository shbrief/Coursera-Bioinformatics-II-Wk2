def skew_diagram(Genome):
    skew = [0]*(len(Genome)+1)
    origin = []
    for i in range(len(Genome)):
        if Genome[i] == "C":
            skew[i+1] = skew[i]-1
        elif Genome[i] == "G":
            skew[i+1] = skew[i]+1
        else:
            skew[i+1] = skew[i]
    min_skew = min(skew)  
          
    for i in range(len(Genome)+1):
        if skew[i] == min_skew:
            origin.append(i)
    return " ".join(str(e) for e in origin)
    

# - Sample Input: TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT
# - Sample Output: 11 24
