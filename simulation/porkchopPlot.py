from astropy.time import Time
import numpy as np 
# pyrefly: ignore [missing-import]
from jplephem.spk import SPK 


kernel = SPK.open("simulation/de432s.bsp") #Chebyshev polynomial coefficients

date = Time("2041-06-01", scale="tdb")
jd = date.jd 


