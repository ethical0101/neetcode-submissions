class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}
        result = []

        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums)+1) ]

        for num, freq in dic.items():
            buckets[freq].append(num)
        
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

