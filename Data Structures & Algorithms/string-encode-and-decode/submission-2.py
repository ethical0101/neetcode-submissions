class Solution:

    def encode(self, strs: List[str]) -> str:

        resultString = ''

        for x in strs:
            lenX = len(x)
            resultString=resultString+str(lenX)+'#'+x
        
        # print(resultString)

        return resultString

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        result = []
        while i < len(s):
            j=i
            while s[j] != '#':
                j=j+1
            size = int(s[i:j])
            result.append(s[j+1:j+1+size])
            i = j + 1 + size
        
        return result
