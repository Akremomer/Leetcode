class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        for num in nums:
            if num == count:
                count += 1
            else:
                break
        return count  







        

        