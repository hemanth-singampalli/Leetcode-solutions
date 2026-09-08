class Solution:
    def maxSum(self, nums):
        unique = set()
        total = 0

        for num in nums:
            if num > 0 and num not in unique:
                unique.add(num)
                total += num

        if total == 0:
            return max(nums)

        return total
