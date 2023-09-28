class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        curr_sum = 0
        seen = {1}
        if num == 1:
            return False
        for i in range(2,int(num/2) + 1):
            if i in seen:
                break
            if num % i == 0:
                curr_sum += i
                seen.add(num//i)
        if seen:
            curr_sum += sum(seen)
        return curr_sum == num