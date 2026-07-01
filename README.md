# project-ares
Research project exploring what a potential Mars program might look like in the near future, it serves as a companion to my work in progress RAeS Aerotube entry.

Each simulation file when run should produce a figure into the figure folder.

Includes JPL Ephemeris data used under the NASA Open Source Agreement and is included within the repository, and will not require you to download it separately.

Also includes Izzo Lambert solver from https://github.com/jorgepiloto/lamberthub, used under the GPLv3 license, it would be used as a dependency but this project was writen for Python 3.14.5, which isnt supported by lamberthub.

Dependencies:
-python 3.14.5
-numpy 2.5
-matplotlib
-astropy
-jplephem

Everything should be available through pip or your package manager of choice. 
