# cook your dish here
for _ in range(int(input())):
    w,x,y,z=map(int,input().split())
    print('overflow') if (x-w)<(y*z) else print('filled') if (x-w)==(y*z) else print('unfilled')