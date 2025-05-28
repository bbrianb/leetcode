class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def romanToInt(self, s: str) -> int:
        numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        output = 0
        length = len(s)
        for i in range(length):
            char = numerals[s[i]]
            if i < length - 1 and char < numerals[s[i + 1]]:
                output -= char
            else:
                output += char
        return output


# noinspection SpellCheckingInspection
test_cases = (
    {'input': 'III', 'output': 3},
    {'input': 'MCMXCIV', 'output': 1994}
)