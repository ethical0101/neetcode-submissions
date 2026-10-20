class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = set()

        nums.sort()

    
        for i in range(len(nums)-2):
            j = i + 1

            k = len(nums) - 1

            target = -nums[i]

            while j < k:
                if nums[j] + nums[k] > target:
                    k-=1
                elif nums[j] + nums[k] < target:
                    j+=1
                else:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplet)
                    j += 1
                    k -= 1
                

        return [list(triplet) for triplet in result]