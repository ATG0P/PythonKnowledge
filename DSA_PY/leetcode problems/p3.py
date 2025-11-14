class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        b =  []
        k = 0
        r=0
        for i in range(0,len(s)):
            if s[i] in b:
                if r>k:
                    b.clear()
                else:
                    r=k
                k=1
            else:
                k+=1
                b.append(s[i])
        return r