import time
import tempfile

import numpy as np

from ..Core.Interface import AFM
from .master_panel import MasterPanel


class GridScan:
    
    def __init__(
        self,
        numXgridpoints,
        numYgridpoints,
        igor_path=r"C:\AsylumResearch\v19\RealTime\Igor Pro Folder\Igor.exe",
        filename="ToIgor",
        script = True, 
        verbose=False,
    ):

        self.numXgridpoints = numXgridpoints
        self.numYgridpoints = numYgridpoints
        self.masterpanel = MasterPanel(script=True, igor_path=igor_path, filename=filename, verbose=verbose)
        self._raw_grid = ()
        self.numbered_grid: dict[int, tuple] = {}

    @property
    def numXgridpoints(self):
        return self._numXgridpoints

    @numXgridpoints.setter
    def numXgridpoints(self, value):
        if value is not None:
            self._numXgridpoints = value

    @property
    def numYgridpoints(self):
        return self._numYgridpoints

    @numYgridpoints.setter
    def numYgridpoints(self, value):
        if value is not None:
            self._numYgridpoints = value

    # def make_grid(self, dimensions = True):
    #     #TODO fix for different aspect ratio
        
    #     self._raw_grid = None

    #     if dimensions:
    #         scansize = self.masterpanel.get_params(
    #             ["ScanSize"], "MasterVariablesWave", "root:packages:MFP3D:main:variables"
    #         )
    #     else:
    #         scansize = self.numXgridpoints

    #     # Create arrays of cell borders using linspace with the specified number of points
    #     x = np.linspace(0, scansize, self.numXgridpoints)
    #     y = np.linspace(0, scansize, self.numYgridpoints)

    #     # Create a grid
    #     X, Y = np.meshgrid(x, y)

    #     self._raw_grid = zip(X.flatten(), Y.flatten())

    def _create_force_spot(self, x: float, y: float) -> int:
        self.masterpanel.update_spot(x, y)
        self.masterpanel.draw_update()
        return (x, y)
    
    def checkbox(self):
        self.masterpanel.show_update()
        self.masterpanel.execute()
        return ("It has been checked")
    

    def create_grid_on_igor(self, sleep_time=0):
        self.numbered_grid = {}
        spot_start = self.masterpanel.get_params(
            ["ForceSpotNumber"],
            "ForceVariablesWave",
            "root:packages:MFP3D:main:variables",
        )
        for ind, (x, y) in enumerate(self._raw_grid):
            self.numbered_grid[int(spot_start + ind)] = self._create_force_spot(x, y)

    def clean_up(self):
        self.masterpanel.clear_update()
        self.masterpanel.execute()

    def lvdt_grid(self):
        self.make_grid(dimensions=False)

        scansize = self.masterpanel.get_params(["ScanSize"], "MasterVariablesWave", "root:packages:MFP3D:main:variables")
        Xoffset = self.masterpanel.get_params(["XOffset"], "MasterVariablesWave", "root:packages:MFP3D:main:variables")
        Yoffset = self.masterpanel.get_params(["YOffset"], "MasterVariablesWave", "root:packages:MFP3D:main:variables")
        Xlvdtsens = self.masterpanel.get_params(["XLVDTSens"], "MasterVariablesWave", "root:packages:MFP3D:main:variables")
        Xlvdtoffset = self.masterpanel.get_params(["XLVDTOffset"], "MasterVariablesWave", "root:packages:MFP3D:main:variables")
        Ylvdtsens = self.masterpanel.get_params(["YLVDTSens"], "MasterVariablesWave", "root:packages:MFP3D:main:variables")
        Ylvdtoffset = self.masterpanel.get_params(["YLVDTOffset"], "MasterVariablesWave", "root:packages:MFP3D:main:variables")
        widthratio = self.masterpanel.get_params(["FastRatio"], "MasterVariablesWave", "root:packages:MFP3D:main:variables")
        heightratio = self.masterpanel.get_params(["SlowRatio"], "MasterVariablesWave", "root:packages:MFP3D:main:variables")
        scanangle = self.masterpanel.get_params(["ScanAngle"], "MasterVariablesWave", "root:packages:MFP3D:main:variables")
        # Creating meshgrid
        GridYLocMat, GridXLocMat = np.meshgrid(
            np.arange(scansize/2/heightratio, -scansize/2/heightratio - scansize/(self.numXgridpoints-1)/heightratio, -scansize/(self.numXgridpoints-1)/heightratio),
            np.arange(-scansize/2/widthratio, scansize/2/widthratio + scansize/(self.numYgridpoints-1)/widthratio, scansize/(self.numYgridpoints-1)/widthratio)
        )

        

        # Converting scanangle to radians
        theta = -scanangle * np.pi / 180

        

        # Initializing XLocVMat and YLocVMat with the same shape as GridXLocMat
        XLocVMat = np.zeros_like(GridXLocMat)
        YLocVMat = np.zeros_like(GridYLocMat)

        

        # Rotating grid locations
        for k1 in range(self.numYgridpoints):
            for k2 in range(self.numXgridpoints):
                R1 = np.array([GridXLocMat[k1, k2], GridYLocMat[k1, k2]])

        

                rotation_matrix = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
                R2 = np.dot(R1, rotation_matrix)

        

                GridXLocMat[k1, k2] = R2[0]
                GridYLocMat[k1, k2] = R2[1]

        

                XLocVMat[k1, k2] = (R2[0] + Xoffset) / Xlvdtsens + Xlvdtoffset
                YLocVMat[k1, k2] = (R2[1] + Yoffset) / Ylvdtsens + Ylvdtoffset

        

        # Transposing the matrices
        XLocVMat = XLocVMat.T
        YLocVMat = YLocVMat.T

        self.grid_loc = (XLocVMat, YLocVMat)
