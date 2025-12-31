"""
Problem: Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/description/

You are given an integer array height where height[i] represents the height of the ith bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:
Input: height=[1,7,2,5,4,7,3,6]
Output: 36
Explanation: The container formed by bars at indices 1 and 7 holds min(7,6)*(7-1)=6*6=36.

Example 2:
Input: height=[2,2,2]
Output: 4
Explanation: Any two bars 2 units apart hold min(2,2)*1=2*1=2; best is the outermost pair:2*2=4.

Constraints:
2<=height.length<=1000
0<=height[i]<=1000
"""

class Solution(object):
    def maxArea(self,height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Two-pointer approach in O(n) time, O(1) space
        left,right=0,len(height)-1
        max_water=0
        while left<right:
            width=right-left # Width between bars
            current_height=min(height[left],height[right]) # Height is limited by shorter bar
            max_water=max(max_water,width*current_height) # Calculate area
            if height[left]<height[right]: # Move the pointer for the shorter bar inwards since the taller bar cannot increase the area
                left+=1
            else:
                right-=1
        return max_water
    
        # Time Complexity: O(n), one pass with two pointers
        # Space Complexity: O(1) extra space
