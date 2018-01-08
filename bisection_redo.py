#bisection

#inputs c1, c2, c3, c4, a, b, epsilon are user inputs

def rootfunction(d1,d2,d3,d4,x):
    y=d1*(x**3)+d2*(x**2)+d3*x+d4
    return y

def bisection(e1,e2,e3,e4,a,b,eps):
    fa=rootfunction(e1,e2,e3,e4,a)
    fb=rootfunction(e1,e2,e3,e4,b)
    if fa*fb>0:
        return print('Zero is not in the interval')
    else:
        ya=fa
        yb=fb
        interval=abs(b-a)
        end=0
        while end==0:
            c=(a+b)/2
            yc=rootfunction(e1,e2,e3,e4,c)
            if ya*yc<0:
                b=c
                yb=yc
            else:
                a=c
                ya=yc
            interval=interval/2
            if interval<eps or yc==0:
                end=1
    return c    


print('The equation is of the form c1*x^3+c2*x^2+c3*x+c4=0.')

c1=float(input('Please input c1: '))
c2=float(input('Please input c2: '))
c3=float(input('Please input c3: '))
c4=float(input('Please input c4: '))

a1=float(input('Please input the lower limit, a: '))
b1=float(input('Please input the upper limit, b: '))

epsilon=float(input('Please input epsilon: '))

answer=bisection(c1,c2,c3,c4,a1,b1,epsilon)

print("The root of the function is "+str(answer)+".")

#for testing
# c1=1, c2=2, c3=-3, c4=-2, a=0, b=2
#  x=1.34292308277717, y=0





