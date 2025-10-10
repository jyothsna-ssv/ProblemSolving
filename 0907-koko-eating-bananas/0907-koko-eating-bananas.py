class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left_speed = 1
        right_speed = max(piles)
        optimal_speed = right_speed
        while left_speed <= right_speed:
            mid_speed = (left_speed + right_speed) // 2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid_speed)

            if total_hours <= h:
                optimal_speed = mid_speed
                right_speed = mid_speed - 1
            else:
                left_speed = mid_speed + 1

        return optimal_speed