class Solution(object):
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        i = 0
        while i < len(nums):
            j = i + 1  # 🔁 reset j for every i
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1

# Test case
m = [2, 7, 11, 15]
t = 9
s = Solution()
print(s.twoSum(m, t))  # Output: [0, 1]
