class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Pre - post fix solution
        res = [1] * len(nums)
        pre = 1
        for i in range(1,len(nums)):
            pre = pre*nums[i-1]
            res[i] *= pre

        post = 1

        for i in range(len(nums)-1, 0 , -1):
            post = post*nums[i]
            res[i-1] *= post
        
        return res

        
        # product = 1
        # cnt0 = 0 
        # for i in nums:
        #     if i != 0:
        #         product *= i
        #     else:
        #         cnt0 += 1
        # res = []
        # if cnt0 > 1:
        #     return [0] * len(nums)
        # elif cnt0 == 1:
        #     for i in nums:
        #         if i != 0:
        #             res.append(0)
        #         else:
        #             res.append(product)
        # else:
        #     for i in nums:
        #         res.append(product//i)
        
        # return res
