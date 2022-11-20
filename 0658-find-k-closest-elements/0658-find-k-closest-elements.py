class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        def binary_search(arr, k, x):
            start = 0
            end = len(arr) - 1
            mid = 0
            while start <= end:
                mid = (start + end)//2
                if arr[mid] == x:
                    return mid 
                elif arr[mid] > x:
                    end = mid - 1
                elif arr[mid] < x:
                    start = mid + 1
            return mid

        def closest_number(arr, k, x):
            mid_index = binary_search(arr, k, x)
            # if mid_index == 0:
            #     return arr[mid_index : k]
            # elif mid_index == len(arr) - 1:
            #     return arr[len(arr) - k :]
            start = mid_index - k
            end = mid_index + k
            if mid_index - k < 0:
                start = 0
            if mid_index + k >= len(arr):
                end = len(arr) - 1
            while end - start + 1 > k:
                if abs(arr[start] - x) <= abs(arr[end] - x):
                    end -= 1
                else:
                    start += 1
            return arr[start:end+1] 
        binary_search(arr,k,x)
        return closest_number(arr,k,x)
                