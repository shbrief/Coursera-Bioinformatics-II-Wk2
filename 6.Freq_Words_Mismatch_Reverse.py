from 7_Neighbors import neighbors

def freq_words_mismatch_reverse_sorting(Text, k, d):
    frequent_pattern = []
    neighborhood = []
    
    # all k-mers (both fwd & rev) in Text with maximum d mismatches
    for i in range(len(Text)-k+1):
        reverse = reverse_complement(Text[i:i+k])
        neighborhood.append(neighbors(Text[i:i+k], d))
        neighborhood.append(neighbors(reverse, d))
    neighborhood_array = reduce(lambda x, y: x+y, neighborhood)
    
    # assign index and count to all possible k-mers  
    index = [0]*len(neighborhood_array)
    count = [0]*len(neighborhood_array) 
    for i in range(len(neighborhood_array)):
        pattern = neighborhood_array[i]
        index[i] = pattern_to_number(pattern)
        count[i] = 1
    sorted_index = sorted(index)
    
    # combine counts for same patterns 
    for i in range(1, len(neighborhood_array)):
        if sorted_index[i] == sorted_index[i-1]:
            count[i] = count[i-1]+1
    max_count = max(count)
    
    # using index of maximum counted pattern, withdraw pattern
    for i in range(len(neighborhood_array)):
        if count[i] == max_count:
            pattern = number_to_pattern(sorted_index[i], k)
            frequent_pattern.append(pattern)
    return frequent_pattern
