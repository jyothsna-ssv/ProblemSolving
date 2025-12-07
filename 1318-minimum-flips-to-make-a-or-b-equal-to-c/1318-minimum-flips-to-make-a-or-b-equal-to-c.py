# bit by bit
# if c needs a 1 -> atleast one of a or b must be 1 otherwise flip one
# if c needs a 0 -> both a and b must be 0, flip whichever are 1

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips=0
        while a or b or c:
            bitA=a&1
            bitB=b&1
            bitC=c&1

            if bitC == 1:
                if bitA == 0 and bitB == 0:
                    flips += 1
            else:
                flips += bitA+bitB
            a >>= 1
            b >>= 1
            c >>= 1
        return flips