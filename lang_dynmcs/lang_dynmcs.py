# -*- coding: utf-8 -*-
import math
import random
#from langinput.py import *
def lang_dynmcs(xi, vi, temp, coeff, dtime,Uenergy,ttot):
    crs = open(langinput.py, "r")
    for dtime in [float(j) / 100 for j in range(0, ttot, 1)]:
        Fnet=((-vi*coeff)+random*sqrt(2*coeff*temp)-Uenergy)
        accl = Fnet/m
        vi = vi + dtime*accl
        xi = xi + dtime*vi
        index.append(j)
        position.append(xi)
        velocity.append(vi)
    ldout = open('Output.txt', 'w')
    for j in index:
        ldout.write("%s\n" % j)
    for j in position:
        ldout.write("%s\n" % j)
    for j in velocity:
        ldout.write("%s\n" % j)
    ldout.close()
print ("End of Computations!")
