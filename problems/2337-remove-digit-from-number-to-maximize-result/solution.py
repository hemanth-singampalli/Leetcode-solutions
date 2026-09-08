class Solution:
    def removeDigit(self, number, digit):
        for i in range(len(number) - 1):
            if number[i] == digit and number[i + 1] > digit:
                return number[:i] + number[i + 1:]

        # If no better position was found,
        # remove the last occurrence of digit
        i = number.rfind(digit)
        return number[:i] + number[i + 1:]
