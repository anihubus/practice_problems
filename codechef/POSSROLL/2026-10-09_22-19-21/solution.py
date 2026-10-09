# cook your dish here
x,k,y=map(int,input().split())
print('yes') if y<=(x*k) and y%k==0 else print('no')