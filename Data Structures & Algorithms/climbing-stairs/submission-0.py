class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0] * (n + 1)
        def climbStairsAux(n):
            if n <= 0:
                return 1
            if ways[n] > 0:
                return ways[n]
            if n == 1:
                ways[n] = 1
            else:
                ways[n] += climbStairsAux(n - 1)
                ways[n] += climbStairsAux(n - 2)
            return ways[n]
        for i in range(n):
            climbStairsAux(i)
        return climbStairsAux(n)

