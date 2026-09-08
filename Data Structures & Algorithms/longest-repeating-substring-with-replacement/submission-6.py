class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        l = 0
        longest = 0
        currentMax = 0
        for r in range(len(s)):
            map[s[r]] = map.get(s[r],0) + 1
            currentMax = max(currentMax,map[s[r]])
            while(r-l+1-currentMax>k):
                map[s[l]] = map[s[l]]-1
                l+=1
            
            longest = max(r-l+1, longest)
        return longest

        