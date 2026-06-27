from astropy.time import Time
import numpy as np 
from jplephem.spk import SPK 
import matplotlib.pyplot as plt

startDate = Time("2035-01-01", scale="tdb")
endDate = Time("2050-01-01", scale="tdb")

startDateJD = startDate.jd
endDateJD = endDate.jd

dateArray = np.arange(startDateJD,endDateJD,1)
distanceArray = []

dateTBD = Time(dateArray, format="jd", scale="tdb")
decYears = dateTBD.decimalyear


kernel = SPK.open("simulation/de432s.bsp") #Chebyshev polynomial coefficients

distance = 0

for jd in dateArray:
    earthPos1, earthVel1 = kernel[0, 3].compute_and_differentiate(jd)
    earthPos2, earthVel2 = kernel[3, 399].compute_and_differentiate(jd)

    marsPos, marsVel = kernel[0, 4].compute_and_differentiate(jd)

    rEarth = (earthPos1 + earthPos2) #km
    vEarth = (earthVel1 + earthVel2) #km/s

    rMars = marsPos #km
    vMars = marsVel #km/s

    distance = np.linalg.norm(rMars - rEarth)

    distanceArray.append(distance)

distanceRounded = [val / 100000000 for val in distanceArray]

plt.figure(figsize=(12, 8))
plt.plot(decYears, distanceRounded)
plt.xticks(np.arange(2035, 2051, 1))
plt.yticks(np.arange(0, 5, 0.5))


plt.title("Distance between Earth and Mars over time between 2035 and 2050")
plt.xlabel("Year / years")
plt.ylabel("Distance / x10^11 m")

plt.savefig("simulation/figures/distanceGraph.png", dpi=300, bbox_inches='tight')
plt.show()