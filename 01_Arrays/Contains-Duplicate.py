class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Method 1: Brute Force Approach (Nested Loops)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False
    
    # Time Complexity: O(n^2) since outer loop runs n times and for each of those n times, inner loop runs n-i-1 times which is roughly n times.
    # Space Complexity: O(1) since no extra space is used.
    # Issue: Inefficient for large lists since as input size increases, comparisons increase quadratically.

        # Method 2: Sorting Approach
        nums.sort() # Sort the array first
        for i in range(1,len(nums)): # check adjacent elements for deuplicates
            if nums[i]==nums[i+1]: # if adjacet elements are equal, duplicate found
                return True
        return False # No duplicates found
    
    # Time Complexity: O(nLogn) due to sorting step.
    # Space Complexity: O(1) if sorting is done in place, otherwise O(n) if new array is created.
    # Issue: Still not optimal due to sorting step, which is unncessary for just checking duplicates.

        # Method 3: Hash Set Approach
        seen=set() # Initialize empty set to store seen elements
        for num in nums:
            if num in seen:
                return True
            seen.add(num) # Add current number to the set
        return False # No duplicates found
    
    # Time Complexity: O(n) since we go through the list once.
    # Space Complexity: O(n) in worst case if all elements are unique and stored in the set.
    # Issue: Uses extra space, which can be an issue for very large lists, but is efficient in time.

        # Method 4: Pythonic One-Liner
        return len(set(nums))!=len(nums)
    
    # Time Complexity: O(n) for creating the set from the list.
    # Space Complexity: O(n) for storing the unique elements in the set.

    # Summary: method 3 and 4 are the most efficient in terms of time complexity, with method 4 being the most concise. 
    # However, they both use extra space. Method 1 is the least efficient, and method 2 is a compromise but still not optimal.

