# -*- coding: utf-8 -*-

import math

import random



ttot=200

xi=0

vi=1

temp=1

coeff=1

dtime=0.01

Uenergy=0.5

m=0.0001



def lang_dynmcs(xi, vi, temp, coeff, dtime,ttot):

    #crs = open(langinput.py, "r")

    #Attempt to take potential energy file and split its columns and create

    #an array

    #UIndex=[]; Upos=[]; Uenergy=[]; UForce=[];

    #i = open(Uenergy.txt,'r')

    #for line in i:

    #w, x, y, z = line.split(' ',' ',' ',' ',' ')

    #UIndex.append(float(w))

    #Upos.append(float(x))

    #Uenergy.append(float(y))

    #UForce.append(float(z))

    #Perform a loop for the computations



    def force_net(vi,coeff,temp,Uenergy):



        # Normally use potential energy in the following format Uenergy[j]



        Fnet = ((-vi*coeff)+random.random()*math.sqrt(2*coeff*temp)-Uenergy)

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



    #Perform a loop for the computations

    for dtime in [(float(j) / 100) for j in range(0, ttot, 1)]:

        Fnet = force_net(xi,coeff,temp,Uenergy)

        accl = acceleration(Fnet,m)

        vi = velocity(xi,dtime,accl)

        xi = position(xi,dtime,vi)



        #index.append(j)

        #position.append(xi)

        #velocity.append(vi)

    #ldout = open('Output.txt', 'w')

    #for j in index:

        #ldout.write("%s\n" % j)

    #for j in position:

        #ldout.write("%s\n" % j)

    #for j in velocity:

        #ldout.write("%s\n" % j)

    #ldout.close()



print ("End of Computations!")



lang_dynmcs(xi, vi, temp, coeff, dtime,ttot)
