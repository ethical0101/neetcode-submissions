class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sortedres = ''.join(sorted(s))
            res[sortedres].append(s)
        return list(res.values()) 
