"""
Problem: Find Minimum in Rotated Sorted Array
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

An array nums of length n was originally sorted in ascending order and then rotated 1 to n times.
All elements are unique. Return the minimum element in O(log n) time.

Example 1:
Input: nums=[3,4,5,6,1,2]
Output: 1

Example 2:
Input: nums=[4,5,0,1,2,3]
Output: 0

Example 3:
Input: nums[4,5,6,7]
Output: 4

Constraints:
1<=nums.length<=1000
-1000<=nums[i]<=1000
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right=0,len(nums)-1
        if nums[left]<=nums[right]: # If array is strictly increasing and not rotated, the first element is min
            return nums[left]
        while left<right: # Binary search for inflection point
            mid=(left+right)//2 # If mid element is greater than right, min must be to the right
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid # nums[mid]<=nums[right], min is at mid or to the left
        return nums[left] # left==right is the index of the smallest value
    
    # Time Complexity: O(logn)
    # Space Complexity: O(1)