class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = float('-inf')
        sum =0
        for num in nums:
            sum = sum + num
            largest = max(largest, sum)
            if(sum<0):
                sum = 0
        
        return largest