"""
Problem: Longest Repeating Character Replacement
Link: https://leetcode.com/problems/longest-repeating-character-replacement/description/

Given a string s of uppercase English letters and an integer k, you can replace up to k characters in s
with any uppercase letter. Return the length of the longest substring containing only one distinct character after
at most k replacements.

Example 1:
Input: s='XYYX', k=2
Output: 4
Explanation: Replace both 'X's with 'Y's or both 'Y's with 'X's to get 'YYYY' or 'XXXX'.

Example 2:
Input: s='AAABABB', k=1
Output: 5
Explanation: Change the 'B' to an 'A' to get 'AAAAABB', longest=5('AAAAA').

Constraints:
1<=s.length<=1000
0<=k<=s.length
"""