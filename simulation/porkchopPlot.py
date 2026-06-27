from astropy.time import Time
import numpy as np 
# pyrefly: ignore [missing-import]
from jplephem.spk import SPK 
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors

kernel = SPK.open("simulation/de432s.bsp") #Chebyshev polynomial coefficients

date = Time("2041-06-01", scale="tdb")
jd = date.jd #Julian date

earthPos1, earthVel1 = kernel[0, 3].compute_and_differentiate(jd)
earthPos2, earthVel2 = kernel[3, 399].compute_and_differentiate(jd)

marsPos, marsVel = kernel[0, 4].compute_and_differentiate(jd)

rEarth = (earthPos1 + earthPos2) #km
vEarth = (earthVel1 + earthVel2) #km/s

rMars = marsPos #km
vMars = marsVel #km/s

print(jd)