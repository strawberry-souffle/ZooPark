import bisect


def minDistance(word1: str, word2: str) -> int:
    n = max(len(word1), len(word2))
    letters = dict()
    for i in range(len(word2)):
        if word2[i] in letters:
            letters[word2[i]].append(i)
        else:
            letters[word2[i]] = [i]
    penalty = [(1 + i) for i in range(0, len(word2))]
    relativePenalty = [1] * len(word2)
    indexes = [i for i in range(0, len(word2))]
    for i in range(0, len(word1)):
        if word1[i] not in letters:
            continue
        ind = letters[word1[i]][0]
        if ind <= 0:
            newPenalty = i
            newRelPenalty = 0
            if newRelPenalty >= relativePenalty[ind]:
                continue
            penalty[ind] = newPenalty
            relativePenalty[ind] = newRelPenalty
            indexes[ind] = i
            for j in range(1, len(word2) - ind):
                if relativePenalty[ind] >= relativePenalty[ind + j]:
                    break
                penalty[ind + j] = penalty[ind] + j
                relativePenalty[ind + j] = relativePenalty[ind]
                indexes[ind + j] = i + j
        elif indexes[ind - 1] >= i:
            newPenalty = max(i, ind)
            newRelPenalty = newPenalty - i
            if newRelPenalty >= relativePenalty[ind]:
                continue
            penalty[ind] = newPenalty
            relativePenalty[ind] = newRelPenalty
            indexes[ind] = i
            for j in range(1, len(word2) - ind):
                if relativePenalty[ind] >= relativePenalty[ind + j]:
                    break
                penalty[ind + j] = penalty[ind] + j
                relativePenalty[ind + j] = relativePenalty[ind]
                indexes[ind + j] = i + j
        else:
            newPenalty = relativePenalty[ind - 1] + i - 1
            newRelPenalty = newPenalty - i
            if newRelPenalty >= relativePenalty[ind]:
                continue
            penalty[ind] = newPenalty
            relativePenalty[ind] = newRelPenalty
            indexes[ind] = i
            for j in range(1, len(word2) - ind):
                if relativePenalty[ind] >= relativePenalty[ind + j]:
                    break
                penalty[ind + j] = penalty[ind] + j
                relativePenalty[ind + j] = relativePenalty[ind]
                indexes[ind + j] = i + j
    return penalty[-1] + (len(word1) - indexes[-1] - 1)

def minDistance_alt(word1: str, word2: str) -> int:
    if len(word1) <= 0:
        return len(word2)
    if len(word2) <= 0:
        return len(word1)
    letters = dict()
    for i in range(len(word2)):
        if word2[i] in letters:
            letters[word2[i]].append(i)
        else:
            letters[word2[i]] = [i]
    tails = []  # Dummy head
    tailVariants = []  # Dummy head
    tailVariants_Penalties = []  # Dummy head
    tailVariants_Indexes = []
    for i in range(len(word1)):
        if word1[i] not in letters:
            continue
        if len(tails) <= 0:
            tails.append(letters[word1[i]][0])
            tailVariants.append([letters[word1[i]][0]])
            tailVariants_Indexes.append([i])
            tailVariants_Penalties.append([max(0, letters[word1[i]][0] - i)])

            for l in range(1, len(letters[word1[i]])):
                tailVariants[0].append(letters[word1[i]][l])
                tailVariants_Indexes[0].append(i)
                tailVariants_Penalties[0].append(max(0, letters[word1[i]][l] - i))
            continue
        addingIndex = bisect.bisect_right(letters[word1[i]], tails[-1])
        if addingIndex < len(letters[word1[i]]):
            tails.append(letters[word1[i]][addingIndex])
            m = bisect.bisect_left(tailVariants[-1], letters[word1[i]][addingIndex])
            tailVariants_Penalties.append([min(1 + max(0, letters[word1[i]][addingIndex] - i), min(
                tailVariants_Penalties[-1][j] + max(0, (letters[word1[i]][addingIndex] - tailVariants[-1][j]) - (
                            i - tailVariants_Indexes[-1][j])) for j in range(0, m)))])
            tailVariants.append([letters[word1[i]][addingIndex]])
            tailVariants_Indexes.append([i])
            for l in range(addingIndex + 1, len(letters[word1[i]])):
                ind = len(tails) - 1
                tailVariants[ind].append(letters[word1[i]][l])
                tailVariants_Indexes[ind].append(i)
                if ind > 0:
                    tailVariants_Penalties[ind].append(min(1 + max(0, letters[word1[i]][l] - i), min(
                        tailVariants_Penalties[ind - 1][j] + max(0,
                                                                 (letters[word1[i]][l] - tailVariants[ind - 1][j]) - (
                                                                         i - tailVariants_Indexes[ind - 1][j])) for
                        j in range(0, len(tailVariants[ind - 1])))))
                else:
                    tailVariants_Penalties[ind].append(max(0, letters[word1[i]][l] - i))
        for l in reversed(range(0, addingIndex)):
            ind = bisect.bisect_left(tails, letters[word1[i]][l])

            tails[ind] = letters[word1[i]][l]
            tailVariants[ind] = [letters[word1[i]][l]] + tailVariants[ind]
            tailVariants_Indexes[ind] = [i] + tailVariants_Indexes[ind]
            if ind > 0:
                m = bisect.bisect_left(tailVariants[ind - 1], letters[word1[i]][l])
                # tailVariants_Penalties[ind] = [min(tailVariants_Penalties[ind - 1][j] + max(0, (letters[word1[i]][l] - tailVariants[ind - 1][j]) - (i - tailVariants_Indexes[ind - 1][j])) for j in range(0, m))] + tailVariants_Penalties[ind]
                tailVariants_Penalties[ind] = [min(1 + max(0, letters[word1[i]][l] - i), min(
                    tailVariants_Penalties[ind - 1][j] + max(0, (letters[word1[i]][l] - tailVariants[ind - 1][j]) - (
                                i - tailVariants_Indexes[ind - 1][j])) for j in range(0, m)))] + tailVariants_Penalties[
                                                  ind]
            else:
                tailVariants_Penalties[ind] = [max(0, letters[word1[i]][l] - i)] + tailVariants_Penalties[ind]
    if len(tails) > 0:
        return min(tailVariants_Penalties[-1][j] + max(0, (len(word2) - tailVariants[-1][j]) - (
                    len(word1) - tailVariants_Indexes[-1][j])) for j in range(0, len(tailVariants[-1]))) + (
                    len(word1) - len(tails))
    else:
        return len(word1)

# print(minDistance_alt("teacher", "teaseler"))
# print(minDistance_alt("teacher", "fecche"))
# print(minDistance_alt("distance", "beholder"))
print(minDistance_alt("distance", "substance"))

