# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def equalFrequency(self, word: str) -> bool:
        allFreq = {}
        for c in word:
            cFreq = word.count(c)
            if cFreq in allFreq:
                if c not in allFreq[cFreq]:
                    allFreq[cFreq].append(c)
            else:
                allFreq[cFreq] = [c]

        print()
        print(allFreq)

        return (len(allFreq) == 1 and (1 in allFreq or len(allFreq[list(allFreq.keys())[0]]) == 1) or
                len(allFreq) == 2 and len(allFreq) == 2 and max(allFreq.keys()) == min(allFreq.keys()) + 1 and len(allFreq[max(allFreq.keys())]) == 1 or
                len(allFreq) < 3 and 1 in allFreq and len(allFreq[1]) == 1)

test_cases = (
    {
        'input': ('aazz',),
        'output': (False,),
    },
    {
        'input': ('bac',),
        'output': (True,),
    },
    {
        'input': ('ddaccb',),
        'output': (False,),
    },
    {
        'input': ('abbcc',),
        'output': (True,),
    },
    {
        'input': ('cbcca',),
        'output': (False,),
    },
    {
        'input': ('zz',),
        'output': (True,),
    },
    {
        'input': ('cccd',),
        'output': (True,),
    },
    {
        'input': ('abcc',),
        'output': (True,),
    },
    {
        'input': ('babbdd',),
        'output': (False,),
    },
)