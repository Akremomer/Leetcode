class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        length = []
        for i in range(len(s)):
            if s[i] != " ":
                count += 1
            else:
                if count > 0:  
                    length.append(count)
                count = 0
        if count > 0: 
            length.append(count)
        return length[-1] if length else 0
        
        