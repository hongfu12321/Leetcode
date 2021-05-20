'''
283. Move Zeroes
Easy

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n, slow, fast = len(nums), 0, 0
        
        while fast < n and nums[slow] != 0:
            slow += 1
            fast += 1
        
        while slow < n:
            if nums[slow] == 0:
                while fast < n and nums[fast] == 0:
                    fast += 1
                if fast == n: return 
                nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

'''
Runtime: 52 ms, faster than 48.98% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.4 MB, less than 59.84% of Python3 online submissions for Move Zeroes.
'''

