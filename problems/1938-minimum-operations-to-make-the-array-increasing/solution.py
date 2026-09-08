class Solution:
    def minOperations(self, nums):
        operations = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                needed = nums[i - 1] + 1 - nums[i]
                nums[i] += needed
                operations += needed

        return operations
