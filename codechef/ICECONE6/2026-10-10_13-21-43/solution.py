# cook your dish here
for _ in range(int(input())):
    x,y,n=map(int,input().split())
    print(x-(y*n)) if x-(y*n)>0 else print(0)