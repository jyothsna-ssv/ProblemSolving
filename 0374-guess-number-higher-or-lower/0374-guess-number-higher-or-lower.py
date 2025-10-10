# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left_limit = 1
        right_limit = n

        while left_limit <= right_limit:
            # middle value
            mid_value = (left_limit + right_limit) // 2

            feedback = guess(mid_value)

            if feedback == 0:
                # Correct guess
                return mid_value
            elif feedback == -1:
                # guess is too high, move search range lower
                right_limit = mid_value - 1
            else:
                # guess is too low, move search range higher
                left_limit = mid_value + 1