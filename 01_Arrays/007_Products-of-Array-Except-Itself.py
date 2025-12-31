"""
Problem: Product of Array Except Itself
Link: https://leetcode.com/problems/product-of-array-except-itself/description/

Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product fits in a 32-bit integer.
Follow-up: Solve in O(n) time without using division.

Example 1:
Input: nums=[1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums=[-1,0,1,2,3]
Output: [0,-6,0,0,0]

Constraints: 
2<=nums.length<=1000
-20<=nums[i]<=20
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        output=[1]*n
        prefix=1 # First pass: Calculate prefix products
        for i in range(n):
            output[i]=prefix
            prefix*=nums[i] # Holds product of all nums[0] to nums[i-1]
        suffix=1 # Second pass: Multiply by suffix products
        for i in range(n-1,-1,-1):
            output[i]*=suffix
            suffix*=nums[i] # Holds product of all nums[i+1] to nums[n-1]
        return output

    # Time Complexity: O(n) since there are two linear passes through the array
    # Space Complexity: O(1) extra space if we do not count the output array since we only use two scalar variables (prefix and suffix)
    # This approach avoids division and efficiently computes the product of all elements except the current one by leveraging prefix and suffix products.
