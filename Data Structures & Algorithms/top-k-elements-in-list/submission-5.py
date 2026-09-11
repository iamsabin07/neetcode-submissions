class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for i in nums:
            count[i] = count.get(i,0) + 1
        
        bucket = {x:[] for x in range(len(nums)+1)}

        for i in count:
             bucket[count[i]].append(i)
        
        for i in range(len(nums),0,-1):
            for j in range(len(bucket[i])):
                res.append(bucket[i][j])
                if(len(res)==k):
                    return res
        
        return res






