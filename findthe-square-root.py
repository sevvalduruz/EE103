x=int(input("What x to find the square root of? "))
g=int(input("What guess to start with? "))
y=g*g-x
if y==0:
    print("The square root of",x,"is",g)
    nextg = g- (g*g-x)/(2*g)
    print("The next guess is",nextg)