class Solution(object):
    def isValid(self, s):
        valid = {"{":"}","[":"]","(":")"}
        stack = []
        for char in s:
            if char in valid:
                stack.append(valid[char])
            else:
                if len(stack) == 0 or stack[-1] != char:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
                        
                      
                       
                    
            
            