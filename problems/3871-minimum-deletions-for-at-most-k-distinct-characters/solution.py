class Solution:
    def minDeletion(self, s, k):
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        frequencies = sorted(count.values())

        deletions = 0
        remove = len(frequencies) - k

        for i in range(remove):
            deletions += frequencies[i]

        return deletions
