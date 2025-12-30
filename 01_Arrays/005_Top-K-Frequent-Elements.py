"""
Problem: Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/description/

Given an integer array nums and an integer k, return the k most frequent elements.
The test cases are generated such that the answer is always unique.
You may return the answer in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k=2
Output: [2,3]

Example 2:
Input: nums = [7,7], k=1
Output: [7]

Constraints:
1<=nums.length<=10^4
-1000<=nums[i]<=1000
1<=k<=number of distinct elements in nums
"""
from collections import Counter, defaultdict
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Method 1: Using Counter and heapq.nlargest
        frequency=Counter(nums) # Count frequency of each element
        return heapq.nlargest(k,frequency.keys(),key=frequency.get) # Extract k keys with highest counts
    
        # Time Complexity: O(n+dlogk), n=len(nums), D=# of distinct elements
        # Space Complexity: O(d) since we store counts for each distinct element
        # Issue: Efficient for moderate size inputs, but might struggle with very Large inputs due to heap operations

        # Method 2: Bucket Sort by Frequency Approach
        if not nums:
            return []
        frequency=Counter(nums)
        max_frequency=max(frequency.values())
        buckets=[[] for _ in range(max_frequency+1)] # buckets[i] will hold elements with frequency i
        for num, count in frequency.items():
            buckets[count].append(num)
        result=[] # Collect top k frequent elements from buckets highest to lowest frequency
        for i in range(max_frequency,0,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result)==k:
                    return result
        return result
    
        # Time Complexity: O(n+d+m), where m=max frequency<=n
        # Spacce Complexity: O(n+m) for frequency map and buckets
        # Issue: More complex implementation, but very efficient for large inputs with limited distint elemeents.