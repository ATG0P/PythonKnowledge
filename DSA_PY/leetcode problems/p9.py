class Solution(object):
    def isPalindrome(self, x):
        self.x = x
        y = x
        a = []
        while y>0:
            a.append(y%10)
            y = y//10
        b=[]
        l = len(a)-1
        while l>=0:
            b.append(a[l])
            l-=1
        if b==a and x>=0:
            return True
        else:
            return False