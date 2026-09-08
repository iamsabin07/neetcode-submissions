class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dicta = {}

        for num in nums:
            dicta[num] = dicta.get(num, 0) + 1

        bucket = {i: [] for i in range(1, len(nums) + 1)}

        for key, value in dicta.items():
            bucket[value].append(key)

        answer = []

        for key in range(len(nums), 0, -1):
            for value in bucket[key]:
                answer.append(value)

                if len(answer) == k:
                    return answer

        return answer