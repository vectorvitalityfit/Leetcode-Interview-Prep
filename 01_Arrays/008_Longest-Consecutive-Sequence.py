"""
Problem: Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/description/

Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence where each element is exactly one greater than the previous element.
Elements do not appear consecutively in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums=[2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2,3,4,5]. 

Example 2:
Input: nums=[0,3,2,5,4,6,1,1]
Output: 7

Constraints:
0<=nums.length<=1000
-10^9<=nums[i]<=10^9
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Method 1: HashSet O(n)
        num_set=set(nums)
        longest=0
        for num in num_set:
            if num-1 not in num_set: #Start counting at the beginning of a sequence
                length=1
                current=num
                while current+1 in num_set:
                    current+=1
                    length+=1
                longest=max(longest,length)
        return longest
    
        # Time Complexity: O(n), each element is visited at most twice
        # Space Complexity: O(n) for the set

        # Method 2: Sorting O(nlogn)
        if not nums:
            return 0
        nums.sort()
        longest=1
        current_len=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue # skip duplicates
            elif nums[i]==nums[i-1]+1:
                current_len+=1
            else:
                longest=max(longest,current_len)
                current_len=1
        longest=max(longest,current_len)
        return longest
    
        # Time Complexity: O(nlogn)
        # Space Complexity: O(1) or O(n) depending on sort implementation