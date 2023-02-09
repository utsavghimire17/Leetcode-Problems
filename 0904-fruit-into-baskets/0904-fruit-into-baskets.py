class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        end = 0
        temp = {}
        max_fruits = 0
        while end < len(fruits):
            temp[fruits[end]] = 1 + temp.get(fruits[end],0)
            
            while len(temp) > 2:
                temp[fruits[start]] -= 1
                if temp[fruits[start]] == 0:
                    del temp[fruits[start]]
                start += 1
            max_fruits = max(max_fruits, end- start + 1)
            end += 1
        return max_fruits
                    
                    