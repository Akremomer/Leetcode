class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n1=len(haystack)
        n2=len (needle)
        l=0
        while n2<=n1:
            if haystack[l:n2]==needle:
                return l
            else:
                l+=1
                n2+=1
        return -1
        