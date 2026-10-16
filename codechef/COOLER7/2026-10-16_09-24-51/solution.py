# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    x=0
    while n>m:
       x+=n
       n-=1
    print(x)