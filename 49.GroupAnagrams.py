import collections


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = dict()
    anagram_output = dict()
    for i in strs:
        letters_dict = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'i': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'o': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'u': 0,
            'v': 0,
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0
        }
        frSet = frozenset(i)
        for l in range(len(i)):
            letters_dict[i[l]] += 1
        added = False
        if frSet in anagrams:
            for j in range(len(anagrams[frSet])):
                if letters_dict == anagrams[frSet][j]:
                    anagram_output[frSet][j].append(i)
                    added = True
                    break
            if not added:
                anagrams[frSet].append(letters_dict)
                anagram_output[frSet].append([i])

        else:
            anagrams[frSet] = [letters_dict]
            anagram_output[frSet] = [[i]]
    output = []
    for j in anagram_output.keys():
        output +=anagram_output[j]
    return output

# well, I didn't know you could do that
def groupAnagrams_alt(strs: list[str]) -> list[list[str]]:
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()

# that's smart
def groupAnagrams_smart(strs: list[str]) -> list[list[str]]:
    primes = {'a': 2,
              'b': 3,
              'c': 5,
              'd': 7,
              'e': 11,
              'f': 13,
              'g': 17,
              'h': 19,
              'i': 23,
              'j': 29,
              'k': 31,
              'l': 37,
              'm': 41,
              'n': 43,
              'o': 47,
              'p': 53,
              'q': 59,
              'r': 61,
              's': 67,
              't': 71,
              'u': 73,
              'v': 79,
              'w': 83,
              'x': 89,
              'y': 97,
              'z': 101
              }

    subLists = {}

    for string in strs:
        product = 1

        for character in string:
            product = primes[character] * product

        if product in subLists.keys():
            listA = subLists[product]
            listA.append(string)
            subLists[product] = listA
        else:
            subLists[product] = [string]

    listToReturn = []

    for value in subLists.keys():
        listToReturn.append(subLists[value])

    return listToReturn
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))