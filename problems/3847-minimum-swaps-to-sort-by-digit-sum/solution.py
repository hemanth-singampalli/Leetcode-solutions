
class Solution:
    def digitSum(self, n):
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s

    def minSwaps(self, nums):
        n = len(nums)

        arr = sorted(nums, key=lambda x: (self.digitSum(x), x))

        pos = {num: i for i, num in enumerate(nums)}
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or pos[arr[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[arr[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps


