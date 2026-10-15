# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    a=[x,y,z].count(0)
    print('Water filling time') if a>=2 else print('Not now')