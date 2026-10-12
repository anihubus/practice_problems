# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    x=n*k;h,m=0,0
    if x<60:
        m=x
    else:
        while x>0:
            if x>=60:
                x-=60
                h+=1
            else:
                m=x
                x-=x
    print(h,m)