# mesa-mag

Compute the absolute magnitude for a given filter from MESA' history file.
We assume using the AB magnitude system and no extincition.  

Copyright: Kuo-Chuan Pan, Hsin-Pei Chen, and Shiau-Jie Rau

## Installation

### Install the package

1. Conle the repository by

```
git clone git@github.com:kuochuanpan/mesa-mag.git
```

2. `cd` to the package path and install the package by

```
pip install .
``` 

### Download filters

1. Download the necessary filters (ascii format) from the [SVO filter website](http://svo2.cab.inta-csic.es/svo/theory/fps3/index.php?mode=browse&gname=HST)

2. Put the filter data under `./mesa_mag/filters/`

## Quick start

1. Get the absolute magnitudes

```python
import mesa_mag
import matplotlib.pyplot as plt

path   = 'mesa_job_path'
filter = 'HST_ACS_HRC.F555W.dat'
age, mag = mesa_mag.get_absolute_magnitude(path, filter)

plt.plot(age, mag)
plt.xlabel('Age [yr]')
plt.ylabel('Absolute Magnitude')
plt.xscale('log')
plt.show()
```

2. Get the apparent magnitude

```python
import mesa_mag
import matplotlib.pyplot as plt

path   = 'mesa_job_path'
filter = 'HST_ACS_HRC.F555W.dat'
distance = 10 # pc
A = 0         # mag

age, app_mag = mesa_mag.get_apparent_magnitude(distance, 
                                                path, 
                                                filter,
                                                extinction=A)
```

3. Get the filter information

```python
import mesa_mag
import matplotlib.pyplot as plt

filter_name = 'HST_ACS_HRC.F555W.dat'
data = mesa_mag.load_filter(filter_name)

plt.plot(data[0],data[1])
plt.xlabel('Wavelength [nm]')
plt.ylabel('Transmission')
plt.show()
```

## References

* Please cite [Pan, Ricker, & Taam (2014)](https://ui.adsabs.harvard.edu/abs/2014ApJ...792...71P/abstract) and [Chen, Rau, & Pan (2023)](https://ui.adsabs.harvard.edu/abs/2023ApJ...949..121C/abstract).
