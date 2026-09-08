class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, maxF = 0,0
        map = {}
        res = 0
        for right in range(len(s)):
            map[s[right]] = map.get(s[right],0)+1
            maxF = max(maxF, map[s[right]])
            curr = right-left+1
            if(curr-maxF > k):
                
                map[s[left]] -=1
                left+=1
            res = max(res, right-left+1)
        return res


        