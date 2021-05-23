class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        for c in s:
            if c not in dict:
                dict[c] = 1
            else:
                dict[c] += 1
        for c in t:
            if c not in dict:
                return False 
            else:
                dict[c] -= 1
        for key, val in dict.items():
            if val != 0:
                return False 
        return True 