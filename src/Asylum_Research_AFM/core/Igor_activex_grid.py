import win32com.client as win32
import pywintypes
import numpy as np
from typing import List
from .Interface import AFM
#from ..Controls import master_pane


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