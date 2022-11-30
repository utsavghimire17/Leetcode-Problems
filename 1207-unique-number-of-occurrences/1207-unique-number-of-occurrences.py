class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hash_map = {}
        temp = set()
        for i in arr:
            hash_map[i] = 1 + hash_map.get(i,0)
        
        for val in hash_map.values():
            if val in temp:
                return False
            temp.add(val)
        return True