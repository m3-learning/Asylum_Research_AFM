from ..core.Interface import AFM
import numpy as np 
from ..Controls.master_panel import MainPanel


class GridScan(MainPanel):

    def __init__(self, num_x_grid_points, num_y_grid_points, igor_path=r"C:\AsylumResearch\v19\RealTime\Igor Pro Folder\Igor.exe", basepath='./', filename='ToIgor', verbose = False):

        #super().__init__( igor_path, basepath, filename, verbose)
        super().__init__(num_x_grid_points,num_y_grid_points)

        self.num_x_grid_points = num_x_grid_points
        self.num_y_grid_points = num_y_grid_points

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


    def grid_maker(self):

        scansize = self.get_params(["ScanSize"], "MasterVariablesWave","root:packages:MFP3D:main:variables")

        # Create arrays of cell borders using linspace with the specified number of points
        x = np.linspace(0, scansize, self.num_x_grid_points)
        y = np.linspace(0, scansize, self.num_y_grid_points)

        # Create a grid
        X, Y = np.meshgrid(x, y)

        return zip(X.flatten(), Y.flatten())
    
    def grid_stepper(self, sleep_time=0):
        madegrid= self.grid_maker()
        for X, Y in madegrid:
            self.update_spot(X,Y)
            self.draw_spot()
        
            

