import mesa_mag
import matplotlib.pyplot as plt

# test load meas
path = '/data/ceag/SNIa_MS_channel/data/MESA/20211229_heat3/2M3R'
data = mesa_mag.load_mesa(path)
print(data[0])
print(data[1])
print(data[2])
print(data[3])

# test load filter
filter_name = 'HST_ACS_HRC.F555W.dat'
#filter_path = "/cluster/home/pan/codes/mesa-mag/mesa_mag/filters"
fdata = mesa_mag.load_filter(filter_name,filter_path=None)

# compuate mag
age, abs_mag = mesa_mag.get_absolute_magnitude(path, filter_name)

distance = 100 # pc
A = 0          # Extinction

age, app_mag = mesa_mag.get_apparent_magnitude(distance, 
                                                path, 
                                                filter_name,
                                                extinction=A)

plt.plot(age, abs_mag,label='Abs Mag')
plt.plot(age, app_mag,label='App Mag')
plt.plot(data[0], data[1],label='logT')
plt.plot(data[0], data[2],label='logL')
plt.plot(data[0], data[3],label='logR')
plt.xlabel('Age [yr]')
plt.ylabel('Absolute Magnitude')
plt.xlim([1e-4,1e6])
plt.legend()
plt.xscale('log')
plt.show()

