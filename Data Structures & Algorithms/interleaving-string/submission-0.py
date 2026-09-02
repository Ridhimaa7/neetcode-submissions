class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        def dp(i,j,k,cache):
            if k == len(s3):
                return (i == len(s1) and j == len(s2))
            if (i,j,k) in cache:
                return cache[(i,j,k)]
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = res or dp(i+1,j,k+1,cache)
            if j < len(s2) and s2[j] == s3[k]:
                res = res or dp(i,j+1,k+1,cache)
            cache[(i,j,k)] = res
            return cache[(i,j,k)]
        return dp(0,0,0,{})