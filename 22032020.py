def common_characters(strs):
  # Fill this in.
    MAX_CHAR = 26
    prim = [True] * MAX_CHAR  
      
    # for each strings  
    for i in range(len(strs)): 
          
        # secondary array for common characters  
        # Initially marked false  
        sec = [False] * MAX_CHAR  
  
        # for every character of ith strings  
        for j in range(len(strs[i])): 
  
            # if character is present in all  
            # strings before, mark it.  
            if (prim[ord(strs[i][j]) - ord('a')]) : 
                sec[ord(strs[i][j]) - 
                    ord('a')] = True
  
        # copy whole secondary array 
        # into primary  
        for i in range(MAX_CHAR): 
            prim[i] = sec[i] 
  
    # displaying common characters
    result = []  
    for i in range(26): 
        if (prim[i]) : 
            # print("%c " % (i + ord('a')), end = "") 
            result.append("%c " % (i + ord('a')))

    return result  

print(common_characters(['google', 'facebook', 'youtube']))
# ['e', 'o']
