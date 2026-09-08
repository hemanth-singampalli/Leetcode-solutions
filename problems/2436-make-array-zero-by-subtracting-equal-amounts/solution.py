class Solution:
    def minimumOperations(self, nums):
        values = set()

        for num in nums:
            if num > 0:
                values.add(num)

        return len(values)
