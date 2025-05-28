class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        minimum = maximum = 0
        y = 0

        for i in differences:
            y += i
            if y < minimum:
                minimum = y
            if y > maximum:
                maximum = y

        output = upper-lower-maximum+minimum+1

        if output > 0:
            return output
        else:
            return 0


test_cases = (
    {'input': ([1, -3, 4], 1, 6), 'output': 2},
    {'input': ([3,-4,5,1,-2], -4, 5), 'output': 4},
    {'input': ([4, -7, 2], 3, 6), 'output': 0}
)