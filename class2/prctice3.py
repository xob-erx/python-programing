n=int(input())
a =n%10
b =int((n/10))%10
c=int((n/100))%10
if a**3+b**3+c**3==n:
    print('YES')
else:
    print('NO')