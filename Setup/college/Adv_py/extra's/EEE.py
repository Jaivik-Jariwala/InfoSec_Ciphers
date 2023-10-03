import math

Vh = float(input("Enter the mean voltage: "))
Ih = float(input("Enter the mean current: "))

R = Vh / Ih
print("Value of mean resistance = ", R)

B = 1600
Rh = R / B
print("Value of Rh = ", Rh)

x = 0.16 * Rh
n = 1 / x
print("Value of concentration = ", n)

b = 0.004
l = 0.006
t = 0.0005
w = b * t
v = w / l
r = R * v
print("Value of resistivity = ", r)

m = Rh / r
print("The value of mobility = ", m)

z = m * B
theta = math.atan(z)
print("The hall angle = ", theta)
