class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  #Index:value

        for i,n in enumerate(nums): #i->index and n->Value
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        return 

