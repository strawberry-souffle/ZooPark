import bisect

# genius. we can bring this problem down to a 300.LongestIncreasingSubsequence by iterating through the letters of text1
# and writing the index of corresponding letter in text2(if any) instead of it. Now if all the letters never repeated we could just find the LIS of that array
# but as some letters can be met several times in text2(so in text1 sa well, but it doesn't matter that much), we will write an array of all those corresponding indexes in place of letter in text1

# Now for each individual letter, we will still follow the previous logic, trying to append new element(smallest possible one) from array to tails[]

# Now we will do a procedure of tailoring tails[] with better heads from that array. But we will only take elements preceeding the one we added
# Because otherwise it would cause a problem of one letter inducing itself over tails[] - say we have only one letter "c" in text1 but 5 of them in text2(say at indexes [2, 3, 4, 5, 6]
# adding the first "c" at index 2 to tails will cause all other 4 letters to also be appended to tails[], generating a wrong output.

# Previous means were not sufficient though, as the step of tailoring still might imply some induction, say we are lookking at tails = [3, 8, 12, 20]
# and our shoveling array is [5, 7] if we substitute 8 with 5, then on second iteration we change 12 to 7, ending up with tails = [3, 5, 7, 20]
# which is not possible as the 7 can never be the head of tail of length 3([3, 5, 7] is not a valid tail). The correct tailoring looks like
# tails = [3, 5, 12, 20] which can be attained by reversing the order of shoveling
def longestCommonSubsequence(text1: str, text2: str) -> int:
    letters = dict()
    for i in range(len(text2)):
        if text2[i] in letters:
            letters[text2[i]].append(i)
        else:
            letters[text2[i]] = [i]
    tails = [-1]
    for i in list(text1):
        if i not in letters:
            continue
        addingIndex = bisect.bisect_right(letters[i], tails[-1])
        if addingIndex < len(letters[i]):
            tails.append(letters[i][addingIndex])
        for l in reversed(range(0, addingIndex)):
            ind = bisect.bisect_left(tails, letters[i][l])
            # if ind < len(tails): actually not needed because of reversed()
            tails[ind] = letters[i][l]
    return len(tails) - 1

print(longestCommonSubsequence("uvirivwbkdijstyjgdahmtutav", "apazcdspcnolsvmlorqxazglyjq"))