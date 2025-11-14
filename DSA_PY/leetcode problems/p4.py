class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.nums1 = nums1
        self.nums2 = nums2
        nums1+=nums2
        nums1.sort()
        n = len(nums1)
        if n%2==0:
            n=n//2
            r =  (nums1[n-1]+nums1[n])/2.0
            return r
        else:
            r = nums1[(n+1)//2 - 1]
            return r    