import bisect
def findNumberOfLIS(nums: list[int]) -> int:
    tails = [-10000000]#Dummy head
    tailVariants = [[-10000000]]#Dummy head
    tailVariants_perms = [[1]]#Dummy head
    for i in nums:
        j = bisect.bisect_left(tails, i)
        if j >= len(tails):
            tails.append(i)#adding tail of new length, whose head is i
            tailVariants.append([i])
            m = bisect.bisect_left(tailVariants[j - 1], i)#index of first head in tailVariants[j - 1] which is >= to i
            tailVariants_perms.append([sum(tailVariants_perms[j - 1][:m])])#associating the number of valid subsequences of length j+1 with i

        else:
            tails[j] = i#new smallest head of tails[j]
            tailVariants[j] = [i] + tailVariants[j]#adding i as the new possible head of tails[j]
            m = bisect.bisect_left(tailVariants[j - 1], i)#index of first head in tailVariants[j - 1] which is >= to i
            tailVariants_perms[j] = [sum(tailVariants_perms[j - 1][:m])] + tailVariants_perms[j]##associating the number of valid subsequences of length j+1, and ending with i, with i

    return sum(tailVariants_perms[-1][:])

print(findNumberOfLIS([1,2,4,3,5,4,7,2]))
