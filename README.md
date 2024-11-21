# mesa-mag
Compute the absolute magnitude for a given filter from MESA' history file. 

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

1. import the package

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
