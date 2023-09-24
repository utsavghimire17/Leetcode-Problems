class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        def binarySearch(arr,x):
            start = 0
            end = len(arr) - 1
            while start <= end:
                mid = (start + end) // 2
                if arr[mid] == x:
                    return mid
                elif arr[mid] < x:
                    start = mid + 1
                elif arr[mid] > x:
                    end = mid - 1
            return mid
        
        def closestElement(arr, k ,x):
            mid = binarySearch(arr,x)
            start = mid - k 
            if start < 0:
                start = 0
            end = mid + k
            if end >= len(arr):
                end = len(arr) - 1
            while end - start + 1 != k:
                if abs(arr[start] - x) < abs(arr[end] - x):
                    end -= 1
                elif abs(arr[start] - x) > abs(arr[end] - x):
                    start += 1
                else:
                    end -= 1
            return arr[start:end+1]
        return closestElement(arr,k,x)
            
                