class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ''
        for letter in strs[0]:
            for word in strs:
                if not word.startswith(prefix + letter):
                    return prefix
            prefix += letter
        return prefix


test_cases = (
    {'input': (['flower', 'flow', 'flight'],), 'output': 'fl'},
)