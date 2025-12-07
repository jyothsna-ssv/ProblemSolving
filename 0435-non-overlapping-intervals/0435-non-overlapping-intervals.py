#sort by start time
# if two intervals overlap -> remove one, specially the one with the larger end, because it blocks more future intervals
# count(removed intervals)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count=0
        prev=intervals[0]

        for i in range(1, len(intervals)):
            curr=intervals[i]
            if curr[0] < prev[1]:
                count += 1
                if curr[1] < prev[1]:
                    prev=curr
            else:
                prev=curr
        return count