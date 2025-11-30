class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v={"a","e","i","o","u"}

        count=sum(1 for i in range(k) if s[i] in v)
        best=count

        left=0

        for right in range(k,len(s)):
            if s[right] in v:
                count += 1
            if s[left] in v:
                count -= 1
            left += 1
            best = max(best, count)
        return best