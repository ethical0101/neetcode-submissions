class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1;
        s = s.lower()

        while i < j:
            if not self.an(s[i]):
                i+=1
            elif not self.an(s[j]):
                j-=1
            elif s[i]!=s[j]:
                return False
            else:
                i += 1
                j -= 1

        return True

    def an(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
                
            
