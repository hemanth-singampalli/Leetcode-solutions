class Solution:
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        # Take 1s first
        take_ones = min(numOnes, k)
        total = take_ones
        k -= take_ones

        # Take 0s next
        take_zeros = min(numZeros, k)
        k -= take_zeros

        # Take -1s last
        total -= k

        return total
