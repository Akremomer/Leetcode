class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=nums1+nums2
        merged.sort()
        l=0
        h=len(merged)-1
        if len(merged)%2==0:
            m=(merged[h//2]+merged[(h//2)+1])/2
            return m
        else:
            m=int(h//2)
            return merged[m]
        




        