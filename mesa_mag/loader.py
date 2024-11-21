import numpy as np
import pathlib

def load_mesa(sim_path, filename='history.data', 
              vars=['star_age','log_Teff', 'log_L', 'log_R']):
    """
    Load the MESA data from the data directory.

    ---
    Parameters:

    sim_path: str
        The path to the MESA simulation directory.

    filename: str
        The name of the file to load. Default is 'history.data'.
        Here, we assume the file is in the 'sim_path/LOGS/' directory.

    vars: list
        The variables to load. Default is ['star_age', 'log_Teff', 'log_L', 'log_R'].

    Returns:
    data: np.ndarray
        The data with the requested variables.

    """
    
    # check the path exist
    path = pathlib.Path(sim_path)
    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {sim_path}")
    
    # check the file exist
    file = path / 'LOGS' / filename
    if not file.exists():
        raise FileNotFoundError(f"File does not exist: {file}")
    
    # load the header (the sixth row)
    with open(file, 'r') as f:
        headers = f.readlines()[5].split()
    #print(headers)

    # we need log_Teff, log_L, Log_R and the star_age
    # find the corresponding 
    indexs = [headers.index(var) for var in vars]
    #print(indexs)

    # load the data
    # the first 6 rows are the header
    data = np.loadtxt(file, skiprows=6, 
                      usecols=tuple(indexs),
                      unpack=True)

    return data
    
def load_filter(filter_name, filter_path=None):
    """
    Load the filter data from the filter directory.

    ---
    Parameters:

    filter_name: str
        The name of the filter file to load.

    filter_path: str
        The path to the filter directory.

    Returns:
    data: np.ndarray
        The filter data with two columns: wavelength [nm] and transmission

    """
    
    if filter_path is None:
        filter_path = pathlib.Path(__file__).parent / 'filters'

    # check the path exist
    path = pathlib.Path(filter_path)
    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {filter_path}")
    
    # check the file exist
    file = path / filter_name
    if not file.exists():
        raise FileNotFoundError(f"File does not exist: {file}")
    
    # load the data
    data = np.loadtxt(file, unpack=True)

    return data


if __name__ == '__main__':
    
    path ='/lfs/data/pan/runs/snbinary/sn1a_post/pan2024/M07A20_sigma_0.05_eheat_2e+47_theat_0.00822'
    data = load_mesa(path)

    filter = 'HST_ACS_HRC.F555W.dat'
    data = load_filter(filter)
    print(data)

