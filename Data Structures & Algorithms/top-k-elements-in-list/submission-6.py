class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        pairs = list(dic.items())

        pairs.sort(key=lambda p:p[1], reverse=True)

        return [pairs[i][0] for i in range(k)]
