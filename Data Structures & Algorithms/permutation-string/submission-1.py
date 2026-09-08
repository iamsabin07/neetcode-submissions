class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s2)<len(s1)):
            return False
        l,r = 0,len(s1)
        sort1 = sorted(s1)
        while(r<=len(s2)):
            sort2 = sorted(s2[l:r])
            if(sort1==sort2):
                return True
            l,r = l+1, r+1

        return False