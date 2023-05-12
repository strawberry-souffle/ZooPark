# import math
#
# n = int(input())
#
# def calculatePermutations(combination: list[int]):
#     def getPermutationsOf(k, dict_, length, excludingAmount=0):
#         n = 0
#         output = 0
#         a = math.factorial(length - 1)
#         for i in dict_:
#             if i == k:
#                 a /= math.factorial(dict[i] - excludingAmount)
#             if i > k:
#                 a /= math.factorial(dict[i])
#                 output += (a*dict[i])
#         return output
#     output = 0
#     dict = {}
#     max = max(combination)
#     for i in range(0, len(combination)):
#         if combination[i] in dict:
#             dict[combination[i]] += 1
#         else:
#             dict[combination[i]] = 1
#     lastSameIndex = 0
#     for i in range(0, len(combination) - 1):
#         if i != 0:
#             if combination[i] != combination[i-1]:
#                 lastSameIndex = i
#         output += getPermutationsOf(combination[i], dict, len(combination) - i, excludingAmount=i-lastSameIndex)
# def calculateVariationsOne(n: int):
#     output = 0
#     def recurDown(previous, depth, totalSpent):
#         if totalSpent > n:
#             return
#         if n - totalSpent - previous - depth < 0:
#             return
#         if totalSpent == n:
#
#         for i in range(previous, (n - totalSpent) + 1):
#             recurDown(i, depth+1, totalSpent + i)
#     for total in range(2, n):
#         while True:
#             for