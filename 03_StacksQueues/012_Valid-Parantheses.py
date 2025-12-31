"""
Problem: Valid Parantheses
Link: https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing only '(', ')', '{', '}', '[' and ']', determine if it is valid.
An input string is valid if:
    1. Every opening bracket is closed by the same type of bracket.
    2. Brackets are closed in the correct order.
    3. Every closing bracket has a corresponding opening bracket.

Example 1:
Input: s="[]"
Output: true

Example 2:
Input: s="([{}])"
Output: true

Example 3:
Input: s="[(])"
Output: true

Constraints:
1<=s.length<=1000
"""

class Solution(object):
    def isValid(self,s):
        """
        :type s:str
        :rtype: bool
        """
        # Map closing to opening
        match={')': '(', ']': '[', '}': '{'}
        stack=[]
        for char in s:
            if char in match:
                if not stack or stack[-1]!=match[char]: # If stack is empty or top is not the matching open, invalid
                    return False
                stack.pop()
            else: # It is an opening bracket
                stack.append(char)
        return not stack # All opens must be closed
    
    # Time Complexity: O(n), one pass through the string
    # Space Complexity: O(n), all opens go on the stack in the worst case scenario
