class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicta = {}

        for i in range(len(nums)):
            req = target-nums[i]
            if req in dicta:
                return [dicta[req], i]
            else:
                dicta[nums[i]] = i
        
        return []