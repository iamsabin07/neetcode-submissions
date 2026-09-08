class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2:
            return False
        stack = []
        map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        for i in s:
            if(i in map):
                if(len(stack) == 0):
                    return False
                if(stack.pop() != map[i]):
                    return False        
            else:
                stack.append(i)
            
        return len(stack) == 0
                