"""
Problem: Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the charactesr can be different.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]] 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from collections import defaultdict
class Solution(object):
    # Method 1: Sorting Approach
    def groupAnagrams(self,strs):
        anagram_map=defaultdict(list) #Use the sorted tuple of characters as a key
        for s in strs:
            key=tuple(sorted(s))
            anagram_map[key].append(s)
        return list(anagram_map.values())
    # Time Complexity: O(n*klogk) where n is the length of strs and k is the max length of a string in strs
    # Space Complexity: O(n*k) for storing the sorted keys and grouped output
    # Issue: Sorting each string can be costly when k is large

    # Method 2: Frequency Count Approach
    # Build a character count signature of length 26 for each string
        if not strs:
            return []
        anagram_map=defaultdict(list)
        for s in strs:
            counts=[0]*26 # Initialize count array for 26 Lowercase letters
            for char in s:
                counts[ord(char)-ord('a')]+=1
            key=tuple(counts)
            anagram_map[key].append(s)
        return list(anagram_map.values())
    # Time Complexity: O(n*k), single pass through each string and counting characters
    # Space Complexity: O(n*k+26), so O(n*k) overall for storing the keys and grouped output
    # Issue: Only works for lowercase English letters; for unicode, the count vector size u grows with the number of unique code points

    # Follow-up: How would you adapt for unicode characters?
    # - Sorting Method: Works as is, since sorting handles unicode
    # - Frequency Count Method: Replace fixed-size array with a hash map to count character frequencies, increasing space complexity to O(n*u) where u is the number of unique characters across all strings.