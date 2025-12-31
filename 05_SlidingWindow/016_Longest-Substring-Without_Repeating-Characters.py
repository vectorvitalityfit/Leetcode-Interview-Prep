"""
Problem: Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s='zxyzxyz"
Output: 3
Explanation: "xyz" is the longest

Example 2:
Input: s="xxxx"
Output: 1

Constraints:
0<=s.length<=1000
s consists of printable ASCII characters.
"""

class Solution(object):
    def lengthOfLongestSubstring(self,s):
        """
        :type s:str
        :rtype: int
        """
        last_seen={} # Map each character to its last seen index
        left=0 # Left bound of current window
        max_len=0
        for right, char in enumerate(s):
            if char in last_seen and last_seen[char]>=left:
                left=last_seen[char]+1
            last_seen[char]=right
            max_len=max(max_len,right-left+1)
        return max_len
    
    # Time Complexity: O(n), each character is visited once
    # Space Complexity: O(min(n,m)), at most, one entry per character
