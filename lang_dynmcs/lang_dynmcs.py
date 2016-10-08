# -*- coding: utf-8 -*-
import math
import random
def lang_dynmcs(xi, vi, temp, coeff, dtime,ttot):
    crs = open(langinput.py, "r")
    #Attempt to take potential energy file and split its columns and create
    #an array
    UIndex=[]; Upos=[]; Uenergy=[]; UForce=[];
    i = open(Uenergy.txt,'r')
    for line in i:
    w, x, y, z = line.split(' ',' ',' ',' ',' ')
    UIndex.append(float(w))
    Upos.append(float(x))
    Uenergy.append(float(y))
    UForce.append(float(z))
    #Perform a loop for the computations
    for dtime in [(float(j) / 100) for j in range(0, ttot, 1)]:
        random.random()
        Fnet = ((-vi*coeff)+random*sqrt(2*coeff*temp)-Uenergy[j])
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
