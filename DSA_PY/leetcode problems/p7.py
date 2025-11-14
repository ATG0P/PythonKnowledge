class Solution(object):
    def reverse(self, x):
        self.x = x
        r=0
        if x>0:
            n=x
            s = []
            while n>0:
                s.append(n%10)
                n=n//10
            k=len(s)-1
            for i in range(0,len(s)):
                r+=s[i]*(10**k)
                k-=1
            print(r)
        else:
            n=-x
            s = []
            while n>0:
                s.append(n%10)
                n=n//10
            k=len(s)-1
            for i in range(0,len(s)):
                r+=s[i]*(10**k)
                k-=1
        if x<0:
            r =-r
        if r > 2**31 - 1 or r < -2**31:
            return 0
        else:
            return r