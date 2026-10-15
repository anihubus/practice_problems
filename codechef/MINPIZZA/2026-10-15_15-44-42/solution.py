# cook your dish here
from math import ceil
for _ in range(int(input())):
    n,x=map(int,input().split())
    print(ceil((n*x)/4))