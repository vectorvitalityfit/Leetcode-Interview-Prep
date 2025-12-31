"""
Problem: 3Sum
Link: https://leetcode.com/problems/3sum/description/

Given an integer array nums, return all the triplets [nums[i],nums[j],nums[k]] such that:
- i, j, k are distinct
- nums[i]+nums[j]+nums[k]==0

No duplicate triplets in the output. Return in any order.

Example 1:
Input: nums=[-1,0,1,2,-1,4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums=[0,1,1]
Output: []

Example 3:
Input: nums=[0,0,0]
Output: [[0,0,0]]

Constraints:
3<=nums.length<=1000
-10^5<=nums[i]<=10^5
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        nums.sort() # Sort to enable two-pointer and skip duplicates
        n=len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]: # Skip duplicate first elements
                continue
            target=-nums[i]
            left,right=i+1,n-1
            while left<right:
                s=nums[left]+nums[right]
                if s<target:
                    left+=1
                elif s>target:
                    right-=1
                else:
                    result.append([nums[i],nums[left],nums[right]]) # Found triplet
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
        return result
    
        # Time Complexity: O(n^2) due to the outer loop and inner two-pointer scan.
        # Space Complexity: O(1) extra space while ignoring input.
