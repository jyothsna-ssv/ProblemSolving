class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n=len(nums)
        res=[]

        for i in range(n-k+1):
            #subarray
            window = nums[i:i+k]

            #count occurrences
            occurrences = Counter(window)

            sorted_items = sorted(occurrences.items(), key=lambda item: (-item[1], -item[0]))

            summ=0
            for val, count in sorted_items[:x]:
                summ += val * count
            res.append(summ)
        return res
