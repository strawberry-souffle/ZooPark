import math

n = int(input())

def calculatePermutations(combination: list[int]):
    def getPermutationsOf(k, dict_, excluding: list[int]):
        n = 0
        output = 1
        for i in dict_:
            adding = dict_[i] - excluding.count(i)
            n += adding
            output /= math.factorial(adding)
        return math.factorial(n) * output
    def chooseNumberHigherThan(k, dict_):
        output = 0
        for i in dict_:
            if i > k:
                output += 1
        return output
    output = 0
    dict = {}
    max = max(combination)
    for i in range(0, len(combination)):
        if combination[i] in dict:
            dict[combination[i]] += 1
        else:
            dict[combination[i]] = 1
    for i in range(0, len(combination) - 1):
        prefix = chooseNumberHigherThan(combination[i])
        output += prefix * getPermutationsOf(dict, combination[:i] + prefix)
def calculateVariationsOne(n: int):
