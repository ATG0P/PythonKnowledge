class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1 = [1,2,3,0,0,0]
        nums1 = [i for i in nums1 if i!=0]
        n = len(nums1)
        nums2= [2,5,6]
        nums2 = [i for i in nums2 if i!=0]
        m = len(nums2)
        nums1+=nums2
