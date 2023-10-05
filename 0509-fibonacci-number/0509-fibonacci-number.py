class Solution:
    def fib(self, n: int) -> int:
        i = 0
        j = 1
        if n == 0:
            return 0
        k = 1
        for m in range(n - 1):
            k = i + j
            i = j
            j = k
        return k
        