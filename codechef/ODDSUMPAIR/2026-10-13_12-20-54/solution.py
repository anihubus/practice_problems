class Solution:
    def check_odd_pairs(self,a,b,c):
        # write your code here
        self.a=a;self.b=b;self.c=c
        if (self.a+self.b)%2!=0 or (self.a+self.c)%2!=0 or (self.b+self.c)%2!=0:
            return 'yes'
        return 'no'