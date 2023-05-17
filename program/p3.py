def volume(r,h):
    volume=3.14*r*r*h
    return volume
def surface (r,h):
    surface=((2*3.14*r)*h)+((3.14*r**2)*2)
    return surface
r=float(input("enter the radius:"))
h=float(input("enter the height" ))
volume= volume(r,h)
area= surface(r,h)
print("volume=",volume)
print("area=",area)