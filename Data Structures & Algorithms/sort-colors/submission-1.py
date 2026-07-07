class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums

        l, r = 0, len(nums)-1
        mid = 0

        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while mid <=r:
            if nums[mid] == 0:
                swap(mid,l)
                l +=1
            elif nums[mid] == 2:
                swap(mid,r)
                r -=1
                mid -= 1
            mid += 1
        