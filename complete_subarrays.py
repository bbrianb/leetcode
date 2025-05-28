from collections import Counter
class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic,SpellCheckingInspection
    def countCompleteSubarrays(self, A: list[int]) -> int:
        n, k = len(A), len(set(A))
        res = leftIndex = 0
        count = Counter()
        for rightIndex in range(n):
            count[A[rightIndex]] += 1
            while len(count) == k:
                count[A[leftIndex]] -= 1
                if count[A[leftIndex]] == 0:
                    del count[A[leftIndex]]
                    # makes len(count) change!
                leftIndex += 1
            res += leftIndex
            # the number just to the left of the subarray we are looking at would make a complete subarray
            # adding the rest of the numbers that are to the left would also make complete arrays
        return res


test_cases = (
    {'input': ([1, 3, 1, 2, 2], ), 'output': 4},
    {'input': ([5, 5, 5, 5], ), 'output': 10}
)