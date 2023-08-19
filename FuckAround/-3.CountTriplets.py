from collections import defaultdict


def count_triplets(arr):
    n = len(arr)
    arr.sort()  # Ensure the array is sorted
    count = 0

    # Frequency map
    freq = {}

    # Initialize frequency map
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Iterate over the array from right to left
    for i in range(n - 1, -1, -1):
        # Reset frequency of current element
        freq[arr[i]] -= 1

        # Two pointers
        j = i - 1
        k = 0

        while k < j:
            # If a valid triplet is found
            if arr[i] == arr[j] + arr[k]:
                count += freq[arr[j]]
                j -= 1
            elif arr[i] > arr[j] + arr[k]:
                k += 1
            else:
                j -= 1

    return count




print(count_triplets([1, 2, 1, 2, 3, 1, 2, 1, 3, 1]))
# print(count_triplets([2, 3, 2, 1, 3, 2]))