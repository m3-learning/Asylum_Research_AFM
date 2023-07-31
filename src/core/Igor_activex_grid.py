import win32com.client as win32
import pywintypes
import numpy as np
from typing import List


def get_wave_data(wave_name:str, wave_folder:str,) -> dict[str,float]:
    """ It pulls the Wave Parameters from the local Igor pro application 
    NOTE: can only be run on windows on the same machine as the igor application
    Igor must be properly set up for activeX control
    Note: This function presumes you already have the igor application open and running and have already selected the experiment type
    Args: 
        wave_name (str): name of the specfic wave you are trying to access (Case sensitive)
        wave_folder (str): colon sperated folder path directly from the igor application (not case sensitive)

    Returns:
        dict[str,float]: Parameters of Scan/Wave
    """
    try: 
        igor = win32.Dispatch('IgorPro.Application')
        try:
            my_df = igor.DataFolder(wave_folder)
        except pywintypes.com_error as e:
            if "Can't find data folder." in e.excepinfo[2]:
                print(f'No folder by the name {wave_folder}')
                return {}
            raise e
        my_waves = my_df.Waves
        this_wave = None
        for i in range(my_waves.Count):
            if my_waves.Item(i).Name == wave_name:
                this_wave = my_waves.Item(i)
        if this_wave is None:
            print(f'No Wave named {wave_name}')
            return {}
        return_value = {}
        all_values = this_wave.GetNumericWaveDataAsDouble()
        for i in range(this_wave.GetDimensions()[1]):
            dimension_name = this_wave.DimensionLabel(0,i,0)
            return_value[dimension_name] = all_values[i][0]
        return return_value
    finally:
        igor = None

def create_grid_params(param_list: List[str], param_dict:dict):
        grid_params = {}
        for key, value in param_dict.items():
            if key in param_list:
                grid_params[key] = value
        return grid_params
    

def grid_maker(num_x_grid_points: int, num_y_grid_points: int, grid_param_list):

    # Create arrays of cell borders using linspace with the specified number of points
    x = np.linspace(0, grid_param_list, num_x_grid_points)
    y = np.linspace(0, grid_param_list, num_y_grid_points)

    # Create a grid
    X, Y = np.meshgrid(x, y)

    return X, Y

#def spot_maker(made_grid):
    #spot_maker



if __name__ == "__main__":
    my_data = get_wave_data("MasterVariablesWave","root:packages:MFP3D:main:variables")
    pass

if __name__ == "__main__":
    grid_param_list = ['ScanSize']
    my_grid_param = create_grid_params(grid_param_list, my_data)
    pass


if __name__ == "__main__":
    my_grid = grid_maker(60,60,my_grid_param['ScanSize'])
    pass