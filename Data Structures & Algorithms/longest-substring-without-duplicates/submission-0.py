class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        charSet = set()
        for r in range(len(s)):
            if(s[r] in charSet):
                while(s[r] in charSet):
                    charSet.discard(s[l])
                    l+=1
            
            charSet.add(s[r])
            longest = max(longest, r-l+1)
        
        return longest