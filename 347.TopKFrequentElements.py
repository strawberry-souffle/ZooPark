import bisect
import collections


def topKFrequent(nums: list[int], k: int) -> list[int]:
    occurences = collections.defaultdict(lambda: 0)
    for i in nums:
        occurences[i] += 1
    arr = list(occurences.keys())
    index = 0

    # noinspection DuplicatedCode
    def quickSort(start, end, k):
        nonlocal index
        if start >= end:
            return
        pivot = occurences[arr[end]]
        j = end
        for i in range(start, end + 1):
            if i >= j:
                arr[i], arr[end] = arr[end], arr[i]
                if (end - i) + 1 < k:
                    quickSort(start, i - 1, k - ((end - i) + 1))
                    return
                elif end - i > k:
                    quickSort(i + 1, end, k)
                    return
                else:
                    index = end - (k - 1)
            if occurences[arr[i]] > pivot:
                for j in reversed(range(i, j)):
                    if occurences[arr[j]] <= pivot:
                        arr[i], arr[j] = arr[j], arr[i]
                        break
                if occurences[arr[i]] > pivot:
                    arr[i], arr[end] = arr[end], arr[i]
                    if (end - i) + 1 < k:
                        quickSort(start, i - 1, k - ((end - i) + 1))
                        return
                    elif end - i > k:
                        quickSort(i + 1, end, k)
                        return
                    else:
                        index = end - (k - 1)
                    return
    quickSort(0, len(arr)-1, k)
    return [arr[i] for i in range(index, len(arr))]

print(topKFrequent([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 10))