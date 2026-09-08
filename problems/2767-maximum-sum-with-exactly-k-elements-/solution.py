class Solution:
    def maximizeSum(self, nums, k):
        largest = max(nums)
        score = 0

        for i in range(k):
            score += largest
            largest += 1

        return score
