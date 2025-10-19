# pattern_matcher.py
# Provides naive_search and kmp_search implementations.

def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    res = []
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            res.append(i)
    return res

def kmp_lps(pattern):
    lps = [0]*len(pattern)
    length = 0
    i=1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length+=1
            lps[i]=length
            i+=1
        else:
            if length!=0:
                length = lps[length-1]
            else:
                lps[i]=0
                i+=1
    return lps

def kmp_search(text, pattern):
    n,m = len(text), len(pattern)
    lps = kmp_lps(pattern)
    res=[]
    i=j=0
    while i<n:
        if text[i]==pattern[j]:
            i+=1; j+=1
            if j==m:
                res.append(i-j)
                j = lps[j-1]
        else:
            if j!=0:
                j = lps[j-1]
            else:
                i+=1
    return res

if __name__ == "__main__":
    t = "ABABDABACDABABCABAB"
    p = "ABABCABAB"
    print("Naive:", naive_search(t,p))
    print("KMP  :", kmp_search(t,p))
