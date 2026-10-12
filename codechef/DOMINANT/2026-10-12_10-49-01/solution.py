# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    print('yes') if a>b+c or b>a+c or c>a+b else print('no')