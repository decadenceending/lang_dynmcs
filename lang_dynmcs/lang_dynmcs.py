# -*- coding: utf-8 -*-
import math
import random
import os

ttot=200
xi=0
vi=1
temp=1
coeff=1
dtime=0.01
m=0.0001
jk=0

def force_net(vi,coeff,temp,Uenergy,jk):

    # Normally use potential energy in the following format Uenergy[j]
    Fnet = ((-vi*coeff)+random.random()*math.sqrt(2*coeff*temp)-Uenergy[jk])
    return Fnet

# Define acceleration function
def acceleration(Fnet,m):

    accl=Fnet/m
    return accl

# Define velocity function
def velocity(vi,dtime,accl):

    vi=vi+dtime*accl
    return vi

# Define position function
def position(xi,dtime,vi):

    xi=xi+dtime*vi
    return xi

def potential_energy():
    with open("Parameter_List.txt") as f:
        f=[x.strip() for x in f if x.strip()]
        data=[tuple(map(float,x.split())) for x in f[0:]]
        Uenergy=[x[2] for x in data]
    return Uenergy

#Define function for writing output
def write_output(index_out,time_out,position_out,velocity_out):

    f = open("Output.txt", "w")
    #Note {0}, {1}, etc, only neede for py26
    for i in range(len(index_out)):
        f.write("{0} {1} {2} {3}\n".format(index_out[i], time_out[i],position_out[i],velocity_out[i]))
    f.close()

def lang_dynmcs(xi, vi, temp, m, coeff, dtime,ttot,jk):

    #Initiate Arrays for Output
    index_out=[]
    time_out=[]
    position_out=[]
    velocity_out=[]

    #Perform a loop for the computations
    for dtime in [(float(j) / 100) for j in range(0, ttot, 1)]:
        Uenergy=potential_energy()
        Fnet = force_net(xi,coeff,temp,Uenergy,jk)
        accl = acceleration(Fnet,m)
        vi = velocity(xi,dtime,accl)
        xi = position(xi,dtime,vi)
        index_out.append(jk)
        time_out.append(dtime)
        position_out.append(xi)
        velocity_out.append(vi)
        jk+=1

    write_output(index_out,time_out,position_out,velocity_out)

lang_dynmcs(xi, vi, temp, m, coeff, dtime,ttot,jk)
print ("End of Computations!")
