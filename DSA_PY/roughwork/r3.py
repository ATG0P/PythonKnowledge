nums1 = [1,2,3,0,0,0]
nums1 = [i for i in nums1 if i!=0]
n = len(nums1)
nums2= [2,5,6]
nums2 = [i for i in nums2 if i!=0]
m = len(nums2)
nums1+=nums2
print(nums1)