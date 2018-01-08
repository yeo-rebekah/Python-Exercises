#newton's method

#inputs c1, c2, c3, c4, a, b, epsilon are user inputs

def rootfunction(d1,d2,d3,d4,x):
    y=d1*(x**3)+d2*(x**2)+d3*x+d4
    return y

def firstder(d1,d2,d3):
    firstder_d1=3*d1
    firstder_d2=2*d2
    firstder_d3=d3
    return firstder_d1, firstder_d2, firstder_d3

def secder(d1,d2):
    secder_d1=3*2*d1
    secder_d2=2*d2
    return secder_d1, secder_d2

def newtons(e1,e2,e3,e4,a,b,eps):
    fa=rootfunction(e1,e2,e3,e4,a)
    fb=rootfunction(e1,e2,e3,e4,b)
    if fa*fb>0:
        print('zero is not in the interval')
    else:
        g1,g2= secder(e1,e2)
        secder_fa=rootfunction(0,0,g1,g2,a)
        if secder_fa*fb<0:
            x0=a
        else:
            x0=b
        end=0
        while end==0:
            fx0=rootfunction(e1,e2,e3,e4,x0)
            h1,h2,h3=firstder(e1,e2,e3)
            firstder_fx0=rootfunction(0,h1,h2,h3,x0)
            x1=x0-(fx0/firstder_fx0)
            interval=x0-x1
            interval=abs(interval)
            x0=x1
            if interval<eps:
                return x1
                end=1






print('The equation is of the form c1*x^3+c2*x^2+c3*x+c4=0.')

c1=float(input('Please input c1: '))
c2=float(input('Please input c2: '))
c3=float(input('Please input c3: '))
c4=float(input('Please input c4: '))

a1=float(input('Please input the lower limit, a: '))
b1=float(input('Please input the upper limit, b: '))

epsilon=float(input('Please input epsilon: '))

answer=newtons(c1,c2,c3,c4,a1,b1,epsilon)

print(answer)

#for testing
# c1=1, c2=2, c3=-3, c4=-2, a=0, b=2
#  x=1.34292308277717, y=0
