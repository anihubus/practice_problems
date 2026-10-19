# cook your dish here
for _ in range(int(input())):
    w,p,k=map(int,input().split())
    a=0
    for _ in range(k):
        if w>=1:
            a+=2
            w-=1
        else:
            a+=1
            p=-1
        k-=1
    print(a)