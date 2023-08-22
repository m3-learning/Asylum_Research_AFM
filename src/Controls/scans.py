import time
import tempfile

import numpy as np

from ..core.Interface import AFM
from ..Controls.master_panel import MainPanel


class GridScan():

    def __init__(self, num_x_grid_points, num_y_grid_points, igor_path=r"C:\AsylumResearch\v19\RealTime\Igor Pro Folder\Igor.exe", basepath=None, filename='ToIgor', verbose = False):


        self.num_x_grid_points = num_x_grid_points
        self.num_y_grid_points = num_y_grid_points
        self.main_panel = MainPanel(script=True, igor_path=igor_path, basepath=basepath, filename=filename, verbose=verbose)
        self._raw_grid = ()
        self.numbered_grid: dict[int, tuple] = {}
# =======
#         self.numbered_grid: list[dict[int, tuple]] = []

#         # a measurement class
#         self.measurement = measurement
# >>>>>>> main


    @property
    def num_x_grid_points(self):
        return self._num_x_grid_points

    @num_x_grid_points.setter
    def num_x_grid_points(self, value):
        if value is not None:
            self._num_x_grid_points = value

    @property
    def num_y_grid_points(self):
        return self._num_y_grid_points

    @num_y_grid_points.setter
    def num_y_grid_points(self, value):
        if value is not None:
            self._num_y_grid_points = value


    def make_grid(self):
        self._raw_grid = None
        scansize = self.main_panel.get_params(["ScanSize"], "MasterVariablesWave","root:packages:MFP3D:main:variables")

        # Create arrays of cell borders using linspace with the specified number of points
        x = np.linspace(0, scansize, self.num_x_grid_points)
        y = np.linspace(0, scansize, self.num_y_grid_points)

        # Create a grid
        X, Y = np.meshgrid(x, y)

        self._raw_grid = zip(X.flatten(), Y.flatten())

    def _create_force_spot(self, x: float, y: float) -> int:
        self.main_panel.update_spot(x,y)
        self.main_panel.draw_update()
        self.main_panel.execute()
        spotnumber = self.main_panel.get_params(["ForceSpotNumber"], "ForceVariablesWave","root:packages:MFP3D:main:variables")
        return spotnumber


    def create_grid_on_igor(self, sleep_time=0):
        self.numbered_grid = {}
        for X, Y in self._raw_grid:
            self.numbered_grid[int(self._create_force_spot(X,Y))] = (X, Y)
            time.sleep(sleep_time)
# =======
#         #self.main_panel.execute()
#         #spotnumber = self.main_panel.get_params(["ForceSpotNumber"], "ForceVariablesWave","root:packages:MFP3D:main:variables")
#         #return spotnumber


#     def create_grid_on_igor(self, sleep_time=0):
#         for X, Y in self._raw_grid:
#             self._create_force_spot(X,Y)
#             self.numbered_grid.append({len(self.numbered_grid)+1, (X, Y)})
#             time.sleep(sleep_time)

    def clean_up(self):
        self.main_panel.clear_update()
        self.main_panel.execute()

#     # Generator
# [ measurement_object, spot number]
#     def run_scan(self):
#         scan_generator = self.dict_generator(self.numbered_grid)

#             # TODO Go there
#             ## TODO get the z value
#             # TODO Dwell
#             # TODO Run_Measurement

#     @staticmethod
#     def dict_generator(list_):
#         for list_ in list_:
#             yield list_


# >>>>>>> main
