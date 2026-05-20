class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        newNums = sorted(nums)
        res = []
        for i in range(len(newNums)):
            if i > 0 and newNums[i] == newNums[i-1]:
                continue
            l,r = i+1, len(newNums)-1
            while l<r:
                if (newNums[l] + newNums[r] + newNums[i]) == 0:
                    res.append([newNums[i], newNums[l],newNums[r]])
                    l += 1
                    while l < r and newNums[l] == newNums[l-1]:
                        l += 1
                elif (newNums[l] + newNums[r] + newNums[i]) > 0:
                    r -= 1
                elif (newNums[l] + newNums[r] + newNums[i]) < 0:
                    l += 1
        return res
