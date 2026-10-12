# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input().lower()
    if n<=3:
        print('yes')
    else:
        for i in range(n-3):
            x=s[i:i+4]
            v='a' in x or 'e' in x or 'i' in x or 'o' in x or 'u' in x 
            if not v:
                print('no')
                break
        else:
            print('yes')