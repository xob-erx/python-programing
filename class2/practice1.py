# 切蛋糕
def qie (a):
        if a==1:
            return 2
        return qie(a-1)+a
n=int(input())
print(qie(n))

