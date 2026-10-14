# cook your dish here
for _ in range(int(input())):
    n=int(input())
    e,o=0,0
    for i in range(1,n+1):
        if n%i==0:
            if i%2==0:
                e+=1
            else:
                o+=1
    print(o,e)