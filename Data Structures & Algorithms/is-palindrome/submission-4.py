class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while(l<r):
            while(r>0 and s[r].isalnum() == False):
                r -=1
            while(l<len(s) and s[l].isalnum() == False):
                l +=1
            if(r>0 and l<len(s)):
                if(s[l].lower() != s[r].lower()):
                    return False
                
                l+=1
                r-=1
        return True
        