import mesa_mag
import matplotlib.pyplot as plt

# test load meas
path ='/lfs/data/pan/runs/snbinary/sn1a_post/pan2024/M07A20_sigma_0.05_eheat_2e+47_theat_0.00822'
data = mesa_mag.load_mesa(path)
print(data.shape)

# test load filter
filter_name = 'HST_ACS_HRC.F555W.dat'
#filter_path = "/cluster/home/pan/codes/mesa-mag/mesa_mag/filters"
data = mesa_mag.load_filter(filter_name,filter_path=None)

# compuate mag
age, mag = mesa_mag.get_absolute_magnitude(path, filter_name)
print(mag)

plt.plot(age, mag)
plt.xlabel('Age [yr]')
plt.ylabel('Absolute Magnitude')
plt.xscale('log')
plt.show()

