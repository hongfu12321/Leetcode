'''
238. Product of Array Except Self
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        product, count_0 = 1, 0
        
        for num in nums:
            if num != 0:
                product *= num
            else:
                count_0 += 1
        if count_0 == len(nums): product = 0
        
        for i, num in enumerate(nums):
            if num != 0 and count_0 == 0:
                output[i] = product // num
            elif num != 0 and count_0 != 0:
                output[i] = 0
            elif num == 0 and count_0 > 1:
                output[i] = 0
            elif num == 0 and count_0 == 1:
                output[i] = product
            
        return output

'''
Runtime: 236 ms, faster than 66.77% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 21.3 MB, less than 39.12% of Python3 online submissions for Product of Array Except Self.
'''