#Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.The order of output does not matter.

##the idea is to count the apperance of given str and remove those charactors before len(p)
def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    S = [ord(x) - 97 for x in s]
    P = [ord(x) - 97 for x in p]

    f1 = [0] * 26
    for x in P:
        f1[x] += 1
    
    f2 = [0] * 26
    windowLength = len(P)
    res = []
    for i, x in enumerate(S):
        f2[x] += 1
        if i >= windowLength: f2[S[i - windowLength]] -= 1
        if f1 == f2: res.append(i - windowLength + 1)
    
    return res