class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        for i in range(2,numRows):
            res.append(self.calculate(res[-1]))
        
        return res
        
    def calculate(self,arr):
        new_res = []
        for i in range(len(arr)):
            if i == 0:
                new_res.append(arr[i])
            if i != len(arr) - 1:
                new_res.append(arr[i] + arr[i+1])
            if i == len(arr) - 1:
                new_res.append(arr[i])
            
        return new_res