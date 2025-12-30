"""
Problem: Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word, phrase or name formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

class Solution(object):
    def isAnagram(self,s,t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Method 1: Sorting Method
        if len(s)!=len(t): # Edge Case: If lengths differ, cannot be anagrams
            return False
        return sorted(s)==sorted(t)
    
        # Time Complexity: O(nlogn) for string with n characters with Timsort algorithm.
        # Space Complexity: O(n) for sorted copies of the strings.
        # Issue: Not optimal for very large strings due to sorting overhead.

        # Method 2: Frequency Count using Hash Map
        if len(s)!=len(t):
            return False
        counts={}
        for char in s: # Count characters in s
            counts[char]=counts.get(char,0)+1
        for char in t: # Decreases counts based on characters in t
            if char not in counts or counts[char]==0:
                return False
            counts[char]-=1
        for count in counts.values(): # Check if all counts are zero
            if count!=0:
                return False
        return True
    
    # Time Complexity:  O(n) since we go through a single pass for each string
    # Space Complexity: O(1) since max 26 distint lowercase characters in english alphabet.
    # Issue: Slightly more complex implementation compared to sorting method
