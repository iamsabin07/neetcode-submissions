class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        currentLongest = nums[0]
        for i in range(k):
            currentLongest = max(nums[i], currentLongest)     
        res = [currentLongest]
        l,r=0,k
        while(r<len(nums)):
            currentLongest=max(currentLongest, nums[r])
            if(nums[l]> nums[r] and nums[l] == currentLongest):
                l+=1
                temp = nums[l:r+1]
                temp.sort()
                currentLongest = temp[-1]
            else:
                l+=1
            r+=1
            res.append(currentLongest)
        return res



        