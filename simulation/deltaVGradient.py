import numpy
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors

grav = 9.80665 #standard acceleration of gravity per https://physics.nist.gov/cgi-bin/cuu/Value?gn

isp = numpy.linspace(300,1000,71) #isp values with increment 10 between 300 and 1000 
ve = isp * grav
dvValues = numpy.arange(4000,12001,10)

colours = cm.plasma(numpy.linspace(0, 1, len(dvValues)))

norm = mcolors.Normalize(vmin=dvValues.min(), vmax=dvValues.max())
sm = cm.ScalarMappable(cmap="plasma", norm=norm)
sm.set_array([])

fig, ax = plt.subplots(figsize=(12,8))

for dv, colour in zip(dvValues, colours):
    mr = numpy.exp(dv/ve)
    ax.plot(isp, mr, color = colour)

plt.colorbar(sm, ax=ax, label="Δv (m/s)")

plt.xticks(numpy.arange(300, 1001, 50))
plt.yticks(numpy.arange(0, 61, 5))

plt.title("Isp vs Mass Ratio for varying Δv")
plt.xlabel("Specific Impulse (s)")
plt.ylabel("Mass Ratio (-)")

plt.savefig("simulation/figures/deltaVGradient.png", dpi=300, bbox_inches='tight')
plt.show()


