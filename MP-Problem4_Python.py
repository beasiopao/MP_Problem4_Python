import matplotlib.pyplot as plt
import numpy as np
import sys as s

#inputs
in_height = float(input('Enter the initial height of the projectile above the ground in meters: '))
in_vel = float(input('Enter the velocity of the projectile in m/s: '))
theta = float(input('Enter the angle (in degrees w/ respect to the +x-axis) at which the projectile is fired: '))
acc_x = float(input('Enter the x-component of the acceleration in m/s^2 (NOTE: consider the sign!): '))
acc_y = float(input('Enter the y-component of the acceleration in m/s^2 (NOTE: consider the sign!): '))

#code for possible errors
if acc_y==0:
    print('------------------')
    print('ERROR: Invalid Input! If the vertical acceleration is zero (y-acc=0), there would be no free fall.')
    s.exit()
if in_height<=0:
    print('------------------')
    print('ERROR: Invalid Input! Initial height of the projectile must be above the ground.')
    s.exit()

#Values of vox(initial velocity at x) and voy(initial velocity at y)
vox = in_vel*np.cos(theta)
voy = in_vel*np.sin(theta)

#Non-ideal Trajectory of the Projectile
d1 = np.sqrt((voy**2) - 4*(acc_y/2)*in_height)
tmax1 = (d1-voy)/acc_y
t1 = np.linspace(0,tmax1)
if tmax1<=0:
    tmax1 = (-d1-voy)/acc_y
t1= np.linspace(0,tmax1)

x = (vox*t1) + ((1/2)*(acc_x)*(t1**2))
y = (voy*t1) + ((1/2)*(acc_y)*(t1**2)) + in_height

#Ideal Trajectory of the Projectile
acc_yi = (-9.8)
d2 = np.sqrt((voy**2) - 4*(acc_yi/2)*in_height)
tmax2 = (d2-voy)/acc_yi
t2 = np.linspace(0,tmax2)
if tmax2<=0:
    tmax2 = (-d2-voy)/acc_yi
t2= np.linspace(0,tmax2)

xi = (vox*t2)
yi = (voy*t2) + ((1/2)*acc_yi*(t2**2)) + in_height

#Graphing of Trajectory
plt.plot(x, y,'-b', label='Non-ideal Trajectory')
plt.plot(xi, yi,'--r', label='Ideal Trajectory')
plt.title('The Ideal and Non-Ideal Trajectory of the Projectile')
plt.xlabel('Range (x-axis)')
plt.ylabel('Height (y-axis)')
plt.grid()
plt.legend(loc='upper right')