class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
             return False
        dicta = {}
        dicta2 ={}

        for i in s:
            dicta[i] = dicta.get(i,0) +1
        
        for i in t:
            if i in dicta:
                dicta2[i] = dicta2.get(i,0) +1
            else:
                return False
        
        return dicta == dicta2
        
        

        