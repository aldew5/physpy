"""
Projectile
"""

from matplotlib import pyplot as plt
import math


        
def graphXY(v, angle, h):
    """ Takes in initial velocity, angle of launch and initial height and graphs
        the motion of the projectile in an XY graph"""
    fig = plt.figure()
            
    axes = fig.add_subplot(111)
    axes.set_ylabel('Change in y')
    axes.set_xlabel('Change in x')
    axes.set_title("Projectile Motion DT Graph")

    v_0y = v*math.sin(angle)
    v_x = v*math.cos(angle)
    v_y = math.sqrt(v_0y**2 - 19.6*-1*h)


    a, b = [], []
    x = 0
    while True:
        y = h - 4.9* (x/v*math.cos(angle*math.pi/180))**2 + math.tan(angle * math.pi/180) * x 

        if y >= 0:
            a.append(x)
            b.append(y)
            x += 0.01
        else:
            break


    axes.plot(a,b)
    plt.show()

