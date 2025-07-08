class Solution(object):
    def longestCommonPrefix(self, strs):
        # Brute fore solution
        # if not str:
        #     return ""
        
        # for i in range(len(strs[0])):
        #     char = strs[0][i]

        #     for s in strs[1:]:
        #         if i == len(s) or s[i] != char:
        #             return strs[0][:i]
        
        # return strs[0]
        
        
        # Optimized - reducing prefix with each comparision
        if not strs:
            return ""
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix=prefix[:-1]
                # which removes last character

                if not prefix:
                    return ""
        return prefix


        