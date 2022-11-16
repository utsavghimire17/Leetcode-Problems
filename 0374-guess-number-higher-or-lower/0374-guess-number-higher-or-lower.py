# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 0
        end = n
        guess_num = 0
        while start + 1 < end:
            guess_num = (start + end)//2
            p = guess(guess_num)
            
            if p == -1:
                end = guess_num
            elif p == 1:
                start = guess_num
            elif p == 0:
                return guess_num
        return n