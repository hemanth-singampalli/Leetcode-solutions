class Solution:
    def getLongestSubsequence(self, words, groups):
        answer = []
        last_group = -1

        for i in range(len(words)):
            if groups[i] != last_group:
                answer.append(words[i])
                last_group = groups[i]

        return answer
