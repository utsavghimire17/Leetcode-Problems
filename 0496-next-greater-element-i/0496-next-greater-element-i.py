class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        temp = {}
        res = [-1] * len(nums1)
        for idx,elem in enumerate(nums1):
            temp[elem] = idx
        for num in nums2:
            while stack and num > stack[-1]:
                if stack[-1] in temp:
                    res[temp[stack[-1]]] = num
                stack.pop()
            stack.append(num)
        return res