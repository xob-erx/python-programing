h=float(input())
w=float(input())
t=w/(h**2)
if(t<18):
    print('underweight')
elif t<25:
    print('normal')
elif t<27:
    print('overweight')
else:
    print('obese')