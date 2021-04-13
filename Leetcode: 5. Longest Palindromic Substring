***
# This is a brute force solution running in O(n^3) time 
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        
        """
        max = 0 
        potentialPalnindrome = ""
        longestPalindrome = ""
        for i in range(len(s)):
            for j in range(i +1, len(s)+1):
                potentialPalindrome = s[i:j]
                if(potentialPalindrome[::-1] == potentialPalindrome and         len(potentialPalindrome) > max):
                    max = len(potentialPalindrome)
                    longestPalindrome = potentialPalindrome 
        
        return longestPalindrome
***
