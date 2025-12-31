"""
Problem: Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/description/

Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome reads the same forward and backward, is case-sensitive, and ignores
all non-alphanumeric characters.

Example 1:
Input: s="Was it a car or a cat I saw?"
Output: true
Explanation: Filtering to "wasitacaroracatisaw", which is a palindrome.

Example 1:
Input: s="tab a cat"
Output: false
Explanation: Filtering to "tabacat", which is not a palindrome.

Constraints:
1<=s.length<=1000
s consists of printable ASCII characters.
"""

class Solution(object):
    def isPalindrome(self,s):
        """
        :type s: str
        :rtype: bool
        """
        # Method 1: Two-pointer scan in O(n) time, O(1) extra space
        left,right=0,len(s)-1
        while left<right:
            while left<right and not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
    
        # Method 2: Filter + Reverse in O(n) time, O(n) space
        filtered=[]
        for char in s:
            if char.isalnum():
                filtered.append(char.lower())
        return filtered==filtered[::-1] # Check if filtered list equals its reverse