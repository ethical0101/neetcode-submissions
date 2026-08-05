class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapOne = {}
        mapTwo = {}

        for num in s:
            if num in mapOne:
                mapOne[num] += 1
            else:
                mapOne[num] = 1

        for num in t:
            if num in mapTwo:
                mapTwo[num] += 1
            else:
                mapTwo[num] = 1

        return mapOne == mapTwo