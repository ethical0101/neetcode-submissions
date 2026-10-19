class Solution:
    def isPalindrome(self, s: str) -> bool:
        strLower = s.lower()
        i = 0
        j = len(strLower) - 1

        while i <= j:
            while i < j and not self.checkUni(strLower[i]):
                i+=1
            
            while i < j and not self.checkUni(strLower[j]):
                j-=1  

            if strLower[i] != strLower[j]:
                return False
            
            i=i+1
            j=j-1          

        return True
    

    def checkUni(self, ch: str) -> bool:
        return (
            ord('a') <= ord(ch) <= ord('z') or
            ord('0') <= ord(ch) <= ord('9')
        )