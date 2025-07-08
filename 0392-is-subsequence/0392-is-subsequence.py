class Solution(object):
    def isSubsequence(self, s, t):
        i=0 # its the pointer for s
        for char in t:
            if i<len(s) and s[i]==char:
                i+=1
        return i==len(s)
        