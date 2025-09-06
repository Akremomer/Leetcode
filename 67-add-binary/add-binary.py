class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=int(a, 2)
        d=int(b, 2)
        sum=c+d
        return bin(sum)[2:]

        