import bisect

class Solution(object):
    def maxEnvelopes(self, envelopes):
        def sort_key(env):
            return (env[0], -env[1]) 

        envelopes.sort(key=sort_key)

        heights = [h for w, h in envelopes]

        dp = []
        for h in heights:
            i = bisect.bisect_left(dp, h)
            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h

        return len(dp)
