# hold -> max profit - if curr holding a stock
# free -> max profit if not holding one
# Each day you either buy, sell or do nothing
# answer = profit when youre free


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold=-prices[0]
        free=0

        for p in prices[1:]:
            free=max(free, hold + p -fee)
            hold=max(hold, free-p)
        return free
    
        