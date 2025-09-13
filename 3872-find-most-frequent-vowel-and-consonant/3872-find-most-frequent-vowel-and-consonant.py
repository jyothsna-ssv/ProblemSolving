class Solution:
    def maxFreqSum(self, s: str) -> int:
        v=set("aeiou")
        count = Counter(s)

        max_vowel=0
        max_consonant=0

        for ch, c in count.items():
            if ch in v:
                max_vowel = max(max_vowel,c)
            else:
                max_consonant=max(max_consonant,c)
        return max_vowel + max_consonant