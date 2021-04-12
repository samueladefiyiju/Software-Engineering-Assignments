class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0 
        j = 0
        maximum = 0
        
        dict = []
        
        while (j < len(s)):
            if (s[j] not in dict):
                dict.append(s[j])
                j = j+1
                maximum = max(maximum, len(dict))
                
            else: 
                dict.remove(s[i])
                i = i+1 
                
        
        return maximum 
      
