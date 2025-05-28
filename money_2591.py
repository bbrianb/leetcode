# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        childrenMoney = [0 for _ in range(children)]
        for i, _ in enumerate(childrenMoney):
            childrenMoney[i] += 1
            money -= 1
        if money < 0:
            return -1
        elif money < 1:
            return 0
        else:
            for i, _ in enumerate(childrenMoney):
                if money > 6:
                    childrenMoney[i] += 7
                    money -= 7
                else:
                    childrenMoney[i] += money
                    money = 0
                    eights = childrenMoney.count(8)
                    if childrenMoney[-1] == 4:
                        if i == len(childrenMoney) - 1:
                            return eights - 1
                        else:
                            return eights
            else:
                eights = childrenMoney.count(8)
                if money == 0:
                    return eights
                else:
                    return eights - 1

test_cases = (
    {
        'input': (20, 3),
        'output': (1,)
    },
    {
        'input': (1, 2),
        'output': (-1,)
    },
    {
        'input': (17, 2),
        'output': (1,)
    },
    {
        'input': (3, 2),
        'output': (0,)
    },
    {
        'input': (10, 2),
        'output': (1,)
    },
)