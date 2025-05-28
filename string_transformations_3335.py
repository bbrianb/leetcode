class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9+7

        letters = [0]*26
        for ch in s:
            letters[ord(ch) -97] += 1

        for _ in range(t):
            cur = [0]*26
            z = letters[25] # how many zs there are
            if z:
                # z becomes ab
                cur[0] = (cur[0] + z) % mod
                cur[1] = (cur[1] + z) % mod
            # all other letters move up 1
            for j in range(25):
                letterCount = letters[j]
                if letterCount:
                    cur[j+1] = (cur[j+1] + letterCount) % mod
            letters = cur

        output = 0
        for letter in letters:
            output = (output + letter) % mod
        return output


# noinspection SpellCheckingInspection
test_cases = (
    {'input': ('abcyy', 2), 'output': 7},
    {'input': ('azbk', 1), 'output': 5},
    {'input': ("jqktcurgdvlibczdsvnsg", 7517), 'output': 79033769}
)