# -*- coding: utf-8 -*-
import math
from langinput.py import *
def lang_dynmcs(xi, vi, temp, Kd, dtime, Ttot, Uenergy, Fnet)
#Calculate position
    def position(xi,dtime)
        xnext=xi + dtime*xi
#Calculate new velocity
    def velocity(vi,dtime)
        vnext=vi+ dtime*vi
#Calculate acceleration
    def forcenet(m,vnext,vi,dtime)
    Fnet=m(vnext-vi/dtime)

#Defining For Loop
#for T in range(0,Ttot)
    #lang_dynmcs
    #vi=vnext
    #xi=xnext
    #T=T+dtime
