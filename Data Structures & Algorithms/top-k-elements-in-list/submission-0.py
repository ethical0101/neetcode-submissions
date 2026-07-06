class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        sorted_num = sorted(counter.items(), key=lambda x:x[1], reverse = True)

        res = [item[0] for item in sorted_num[:k]]

        return res
