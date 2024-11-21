import numpy as np
from mesa_mag import load_mesa, load_filter

def get_absolute_magnitude(sim_path, filter, history_file='history.data', filter_path=None):
    """
    Calculate the absolute magnitude of the star.

    ---
    Parameters:

    sim_path: str
        The path to the MESA simulation directory.

    filter: str
        The name of the filter to use.

    history_file: str
        The name of the history file. Default is 'history.data'.

    filter_path: str
        The path to the filter directory. Default is None.

    """

    # load the MESA data
    data = load_mesa(sim_path, filename=history_file)
    
    rsun = 6.955e8 # [m]
    lsun = 3.828e26 # [W]

    age = data[0]
    log_Teff = data[1]
    log_L = data[2]
    log_R = data[3]
    temperature = 10**log_Teff
    luminosity = 10**log_L * lsun # [L_sun to W]
    radius = 10**log_R * rsun # 

    # load the filter data
    filter_data = load_filter(filter, filter_path)
    wave_length = filter_data[0]*1e-10 # [nm to m]
    sensitivity = filter_data[1]
    
    # constants
    h = 6.62607015e-34 # [m^2 kg / s]
    c = 299792458 # [m/s]
    k = 1.380649e-23 # [m^2 kg s^-2 K^-1]
    pc = 3.086e16 # [m]
    
    black_body = lambda T: (2*h*c**2/wave_length**5) / (np.exp(h*c/(wave_length*k*T))-1)

    # calculate the absolute magnitude
    distance = 10*pc # [10 pc to m]
    f0 = 3.631e-20 # erg cm^-2 s^-1 Hz^-1

    ref_flux = np.trapz(f0*c/wave_length**2*sensitivity, x=wave_length)

    abs_mag = np.zeros_like(age)

    for i in range(len(age)):
        flux = np.trapz(np.pi*black_body(temperature[i])*sensitivity, wave_length)
        flux = (flux/ref_flux)*radius[i]**2 / distance**2
        abs_mag[i] = -2.5*np.log10(flux)

    return age, abs_mag
