class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)

        result=[]
        for c in candies:
            result.append(c+ extraCandies >= max_candies)
        return result