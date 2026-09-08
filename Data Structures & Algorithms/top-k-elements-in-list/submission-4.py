class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        res = []
        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums)+1)]
        for key, value in map.items():
            bucket[value].append(key)
        
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if(len(res)== k):
                    return res
        
        return res



