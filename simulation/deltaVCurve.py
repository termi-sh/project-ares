import numpy
import matplotlib.pyplot as plt


deltaV = 8400 #requirement using figure from  https://www.nasa.gov/wp-content/uploads/2015/09/373665main_nasa-sp-2009-566.pdf pg 23 (bottom of the page)
grav = 9.80665 #standard acceleration of gravity per https://physics.nist.gov/cgi-bin/cuu/Value?gn

isp = numpy.linspace(300,1000,71) #isp values with increment 10 between 300 and 1000 
ve = isp * grav

mr = numpy.exp(deltaV/ve)
hydroloxMR = numpy.exp(deltaV/(450*grav))
ntrMR = numpy.exp(deltaV/(850*grav))

print(f"Hydrolox: 450s, {hydroloxMR} \nNTR: 850s, {ntrMR}")

plt.figure(figsize=(12, 8))
plt.plot(isp, mr)
plt.xticks(numpy.arange(300, 1001, 50))
plt.yticks(numpy.arange(0, 19, 1))

plt.title("Engine Specific Impulse vs Mass Ratio (Lower is better)")
plt.xlabel("Specific Impulse / Seconds")
plt.ylabel("Mass Ratio / -")

plt.axvline(x=450, color='red', linestyle='--', label='RL-10/J-2X (~450s)') #Per Wikipedia
plt.axvline(x=850, color='green', linestyle='--', label='NTR (~850s)') #Estimate from DRACO
plt.axhline(y=hydroloxMR, color='red', linestyle='--')
plt.axhline(y=ntrMR, color='green', linestyle='--')

plt.legend()


plt.savefig("figures/deltaVCurve.png", dpi=300, bbox_inches='tight')
plt.show()


