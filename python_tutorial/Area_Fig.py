def Sqr(a):
    ''' Function to get the area of square'''
    s = a**2
    p = a * 4
    print(f"Area of Square is: {s} & perimeter is: {p}")

def Rect(l, b):
    ''' Function to get the area of rectangle'''
    arr=l*b
    p = 2*(l+b)
    print(f"Area of Rectangle is: {arr} & perimeter is: {p}")

def Tri(a, b, c, height):
    ''' Function to get the area of triangle'''
    art=(1/2)*b*height          # b = base 
    p = a + b + c
    print(f"Area of Triangle is: {art} & perimeter is: {p}")

def Cir(r):
    ''' Function to get the area of circle'''
    arc=3.14*(r**2)
    c = 2*3.14*r
    print(f"Area of Circle is: {arc} & Circumference is: {c}")