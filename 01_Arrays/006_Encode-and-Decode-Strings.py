"""
Problem: Encode and Decode Strings
Link: https://leetcode.com/problems/encode-and-decode-strings/description/

Design an algorithm to encode a list of strings to a single string. The encoded string is sent over the network and decoded back to the original list of strings.

Implement the encode and decode methods:

Example 1:
Input: dummy_input=["Hello","World"]
Output: ["Hello", "World"]

Example 2:
Input: dummy_input=[""]
Output: ['']

Constraints:
0<=str.length<=100
0<=strs[i].length<200
strs[i] contains any possible characters out of 256 Valid ASCII characters.

Follow-up: Your solution should work for any possible set of characters.
"""
class Codec:
    def encode(self, strings):
        """
        :type strings: List[str]
        :rtype: str
        """
        # Prefix each string with its length and a delimiter '#'
        # e.g., ["Hi", ''] -> "2#Hi0#"
        encoded=[]
        for s in strings:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)
    
    def decode(self,s):
        """
        :type s: str
        :rtype: List[str]
        """
        result=[]
        i=0
        while i<len(s):
            j=s.find('#',i) # Read Length
            length=int(s[i:j])
            result.append(s[j+1:j+1+length]) # Extract the string of that length after the delimiter
            i=j+1+length # Move pointer past this segment
        return result
    
    # Time Complexity: encode: O(n+k), n=number of strings, k=total length of all strings, decode: O(n+k)
    # Space Complexity: O(n+k) for encoded string and output list
    # The use of a length prefix with a fixed delimiter '#' guarantees correctness even if the strings contain digits or '#' characters themselves. 
