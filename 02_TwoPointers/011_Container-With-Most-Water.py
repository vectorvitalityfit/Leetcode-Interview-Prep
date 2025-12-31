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