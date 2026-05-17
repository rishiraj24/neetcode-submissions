class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sortedNums = sorted(list(set(nums)))
        finalcnt = 0
        cnt = 1
        for i in range(len(sortedNums)-1):
            if sortedNums[i] + 1 == sortedNums[i+1]:
                cnt += 1
            else:
                finalcnt = max(finalcnt,cnt)
                cnt = 1
        return max(finalcnt,cnt)
