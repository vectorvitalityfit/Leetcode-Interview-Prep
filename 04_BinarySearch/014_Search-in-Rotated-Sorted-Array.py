"""
Problem: Search in Rotated Sorted Array
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

Given a rotated sorted array nums of unique integers and a target, return the index
of target if present; otherwise, return -1.
Your algorithm must run in O(logn) time.

Example 1:
Input: nums=[3,4,5,6,1,2], target=1
Output: 4

Example 2:
Input: nums=[3,5,6,0,1,2], target=4
Output: -1

Constraints:
1<=nums.length<=1000
-1000<=nums[i],target<=1000
All nums are unique and originally sorted in ascending order.
"""

class Solution(object):
    def search(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]: # Determine which half is properly sorted
                if nums[left]<=target<nums[mid]: # Left half is sorted
                    right=mid-1
                else:
                    if nums[mid]<target<=nums[right]: # Right half is sorted
                        left=mid+1
                    else:
                        right=mid-1
        return -1
    
    # Time Complexity: O(logn) due to binary search
    # Space Complexity: O(1), only pointers used