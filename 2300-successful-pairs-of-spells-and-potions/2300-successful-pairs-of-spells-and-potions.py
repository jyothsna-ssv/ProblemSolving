# sort potions
# for each spell, calculate the minimum potion strength needed to reach success.
# Binary search
# first potion >= need , all potions to the right form valid pairs
# Append the count

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()

        m= len(potions)
        res=[]

        def lower_bound(arr, k):
            l,r=0,len(arr)
            while l<r:
                mid=(l+r) // 2
                if arr[mid]< k:
                    l=mid+1
                else:
                    r=mid
            return l
        for s in spells:
            need=(success + s -1)//s
            i = lower_bound(potions, need)
            res.append(m-i)
        return res