# simple_regex_match.py
# Implements regex matching for patterns with '.' and '*' (like LeetCode 10).
def is_match(text, pattern):
    # dp[i][j] = text[:i] matches pattern[:j]
    n, m = len(text), len(pattern)
    dp = [[False]*(m+1) for _ in range(n+1)]
    dp[0][0] = True
    # handle patterns like a*, a*b*, etc for empty text
    for j in range(2, m+1):
        if pattern[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if pattern[j-1] == '.' or pattern[j-1] == text[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif pattern[j-1] == '*':
                dp[i][j] = dp[i][j-2] or ((pattern[j-2]==text[i-1] or pattern[j-2]=='.') and dp[i-1][j])
    return dp[n][m]

if __name__ == "__main__":
    txt = input("Text: ")
    pat = input("Pattern (supports . and *): ")
    print("Match:", is_match(txt, pat))
