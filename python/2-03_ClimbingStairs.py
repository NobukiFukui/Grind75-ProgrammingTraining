
# %%
class Solution:
    def climbStairs(self, n: int) -> int:
        # n <= 1 (including 0 stair) -> a(n) = 1
        if n <= 1:
            return 1
        # n >= 2 -> a(n) = a(n-2) + a(n-1)
        ways_current = 1 # no. of ways to climb current stairs (a(n-1))
        ways_lower = 1   # no. of ways to climb lower stairs   (a(n-2))
        # main loop
        for i in range(2, n+1):
            tmp = ways_current          # memorize no. of ways to climb current stairs
            ways_current += ways_lower  # renew no. of ways to climb current stairs
            ways_lower = tmp            # renew no. of ways to climb lower stairs
        return ways_current

# %%
solution = Solution()
n = 15
print(solution.climbStairs(n))
# %%
