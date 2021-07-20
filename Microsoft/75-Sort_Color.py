'''
75. Sort Colors
Medium

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
 
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return nums
        
        #red = 0, white = 1, blue = 2
        red, blue, curr = 0, len(nums) - 1, 0
        
        while curr <= blue:
            if nums[curr] == 0:
                nums[curr], nums[red] = nums[red], nums[curr]
                curr += 1
                red += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                nums[curr], nums[blue] = nums[blue], nums[curr]
                blue -= 1
                
        return nums