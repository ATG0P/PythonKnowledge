class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = [1,1,1,3,3,4,3,2,4,2]
        nums.sort()
        print(nums)
        r = False
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                r = True
                print(i)
                break
            else:
                pass
        return r