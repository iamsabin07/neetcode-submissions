class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
             return False
        dicta = {}

        for i in s:
            if i in dicta:
                dicta[i] = dicta[i] + 1
            else:
                dicta[i] = 1
        
        for i in t:
            if i in dicta:
                dicta[i] = dicta[i] - 1
            else:
                return False
        
        if any(value != 0 for value in dicta.values()):
            return False
        else:
            return True

        