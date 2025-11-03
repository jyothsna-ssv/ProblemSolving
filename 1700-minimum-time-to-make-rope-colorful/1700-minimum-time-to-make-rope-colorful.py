class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_removal_time=0
        prev_color=colors[0]
        max_time=neededTime[0]

        for i in range(1, len(colors)):
            curr_color = colors[i]
            curr_time = neededTime[i]

            if curr_color == prev_color:
                total_removal_time += min(max_time, curr_time)
                max_time = max(max_time, curr_time)
            else:
                prev_color=curr_color
                max_time = curr_time
        return total_removal_time