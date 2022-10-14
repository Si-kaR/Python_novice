from math import pi

#Formular being used for the computation is A = pi*(r**2)
def circleArea(r):
    A = pi*(r**2)
    print(f"The area of a circle is found using the formular pi*r**2 so by giving the radius to be {r} Your area is {A} units")

#Formular being used for the computation is C = 2*pi*r
def circleCircumference(r):
    C = 2*pi*r
    print(f"The Circumference of a circle is found using the formular 2*pi*r so by giving the radius to be {r} Your area is {C} units")

#Formular being used for the computation is TA = 0.5*(a + b)*h
def trapezoidArea(a, b, h):
    TA = 0.5*(a + b)*h
    print(f"The area of a trapezoid is found using the formular (1/2)*(a+b)*h so by giving the Perimeter at the top,a={a}, base length,b={b} and height,h={h}, Your area is {TA} units")

#Formular being used for the computation is TP = a + b + c + d
def trapezoidPerimeter(a, b, c, d):
    TP = a + b + c + d
    print(f"The perimeter of a trapezoid is found by finding the sum of all the four sides so by giving the perimeters a={a}, b={b}, c={c} and d={d}, Your perimeter is {TP} units")

#Formular being used for the computation is SA = (2*pi*(r**2))+(2*pi*r*h)
def cylinderSurfacearea(r, h):
    SA = (2*pi*(r**2))+(2*pi*r*h)
    print(f"The Surface Area of a cylinder is found using the formular (2*pi*(r**2))+(2*pi*r*h)so by giving the radius,r and height,h to be {r} and {h} respectively, Your surface area is {SA} units")

#Formular being used for the computation is CV = pi*(r**2)*h
def cylinderVolume(r, h):
    CV = pi*(r**2)*h
    print(f"The Volume of a cylinder is found using the formular pi*(r**2)*h so by giving the radius,r and height,h to be {r} and {h} respectively, Your Cylinder Volume is {CV} units")

#Formular being used for the computation is SA = 4*pi*(r**2)
def sphereSurfacearea(r):
    SA = 4*pi*(r**2)
    print(f"The Surface Area of a sphere is found using the formular 4*pi*(r**2) so by giving the radius,r={r}, Your surface area is {SA} units")

#Formular being used for the computation is SV = (4/3)*pi*(r**3)
def sphereVolume(r):
    SV = (4/3)*pi*(r**3)
    print(f"The Surface Volume of a sphere is found using the formular (4/3)*pi*(r**3) so by giving the radius,r={r}, Your surface volume is {SV} units")

#Formular being used for the computation is SA = 6*(x**2)
def cubeSurfacearea(x):
    SA = 6*(x**2)
    print(f"The Surface area of a cube is found using the formular 6*(x**2) so by giving the dimension,x = {x}, You get {SA} units as the surface Volume of your cube")

#Formular being used for the computation is CV = x**3
def cubeVolume(x):  
    CV = x**3
    print(f"The volume of a cube is found using the formular x**3 so by giving the dimension,x = {x}, You get {CV} units as the Volume of your cube")




