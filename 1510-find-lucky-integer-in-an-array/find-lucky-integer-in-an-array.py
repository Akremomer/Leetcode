from typing import List

class Solution: 
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        lucky = -1

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num in freq:
            if num == freq[num]:
                lucky = max(lucky, num)

        return lucky
            






                

                


                

            
                

        