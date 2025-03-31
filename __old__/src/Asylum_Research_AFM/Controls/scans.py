import time
import tempfile

import numpy as np

import sys
sys.path.append("c:\\Users\\Asylum User\\Documents\\Code\\Asylum_Research_AFM\\Asylum_Research_AFM\\src\\Asylum_Research_AFM\\core")
#sys

from Interface import AFM
from master_panel import MasterPanel


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
        self.numXgridpoints = numXgridpoints
        self.numYgridpoints = numYgridpoints
        self.masterpanel = MasterPanel(script=True, igor_path=igor_path, filename=filename, verbose=verbose)
        self._raw_grid = ()
        self.numbered_grid: dict[int, tuple] = {}
        self.grid_loc = ()
        self.grid_loc = ()

    @property
    def numXgridpoints(self):
        return self._numXgridpoints
    def numXgridpoints(self):
        return self._numXgridpoints

    @numXgridpoints.setter
    def numXgridpoints(self, value):
    @numXgridpoints.setter
    def numXgridpoints(self, value):
        if value is not None:
            self._numXgridpoints = value
            self._numXgridpoints = value

    @property
    def numYgridpoints(self):
        return self._numYgridpoints
    def numYgridpoints(self):
        return self._numYgridpoints

    @numYgridpoints.setter
    def numYgridpoints(self, value):
    @numYgridpoints.setter
    def numYgridpoints(self, value):
        if value is not None:
            self._numYgridpoints = value
            self._numYgridpoints = value

    def make_grid(self, dimensions = True):
        """ 
        if you want to make a grid using markers run this in order to create and array of x and y points that will be returned in _raw_grid that will be 
        calculated using numXgridpoints, numYgridpoints, and the scan size which is pulled using get_params, to run this function ensure that GridScan 
        was intialized with values for numXgridpoints and numYgridpoints

        Args:
            dimensions (bool, optional): _description_. Defaults to True.
        """
        #TODO fix for different aspect ratio
        
    def make_grid(self, dimensions = True):
        """ 
        if you want to make a grid using markers run this in order to create and array of x and y points that will be returned in _raw_grid that will be 
        calculated using numXgridpoints, numYgridpoints, and the scan size which is pulled using get_params, to run this function ensure that GridScan 
        was intialized with values for numXgridpoints and numYgridpoints

        Args:
            dimensions (bool, optional): _description_. Defaults to True.
        """
        #TODO fix for different aspect ratio
        
        self._raw_grid = None

        if dimensions:
            scansize = self.masterpanel.get_params(
                ["ScanSize"], "MasterVariablesWave", "root:packages:MFP3D:main:variables"
            )
        else:
            scansize = self.numXgridpoints

        if dimensions:
            scansize = self.masterpanel.get_params(
                ["ScanSize"], "MasterVariablesWave", "root:packages:MFP3D:main:variables"
            )
        else:
            scansize = self.numXgridpoints

        # Create arrays of cell borders using linspace with the specified number of points
        x = np.linspace(0, scansize, self.numXgridpoints)
        y = np.linspace(0, scansize, self.numYgridpoints)
        x = np.linspace(0, scansize, self.numXgridpoints)
        y = np.linspace(0, scansize, self.numYgridpoints)

        # Create a grid
        X, Y = np.meshgrid(x, y)

        self._raw_grid = zip(X.flatten(), Y.flatten())

    def _create_force_spot(self, x: float, y: float) -> int:
        """
        creates the commands send to the command list to igor in order send the marker to the specified position and create a marked spot there 

        Args:
            x (float): the x postition that you want to create a marked spot on 
            y (float): the y postition that you want to create a marked spot on 

        Returns:
            int:the position where the maked spot will be made  
        """
        self.masterpanel.update_spot(x, y)
        self.masterpanel.draw_update()
        """
        creates the commands send to the command list to igor in order send the marker to the specified position and create a marked spot there 

        Args:
            x (float): the x postition that you want to create a marked spot on 
            y (float): the y postition that you want to create a marked spot on 

        Returns:
            int:the position where the maked spot will be made  
        """
        self.masterpanel.update_spot(x, y)
        self.masterpanel.draw_update()
        return (x, y)
    
    def max_spot_value(self):
        """
        max_spot_value takes the number of x and y grid points that were inputted at initalization and multiplies them together and adds 10 and assigns that 
        value to the Force Spot Number Max so if you want to create the grid using markers go_to_spot will actually be able to move to any spot number


        Returns:
            _type_: print statement letting you know that it is changed
        """
        Spot_Number = "ForceSpotNumber"
        max_val_needed = (self.numXgridpoints * self.numYgridpoints) + 10
        self.masterpanel.variable_max_update(Spot_Number, max_val_needed)
        self.masterpanel.execute()
        return (f'Max Spot number has been updated to {max_val_needed}') 
    
    def checkbox(self):
        """
        ensures that the checkbox for whether or not the tip location shows is checked 

        Returns:
            _type_: print statement letting you know that it is checked 
        """
        self.masterpanel.show_tip_update()
        self.masterpanel.execute()
        return ("It has been checked")
    
    
    def max_spot_value(self):
        """
        max_spot_value takes the number of x and y grid points that were inputted at initalization and multiplies them together and adds 10 and assigns that 
        value to the Force Spot Number Max so if you want to create the grid using markers go_to_spot will actually be able to move to any spot number


        Returns:
            _type_: print statement letting you know that it is changed
        """
        Spot_Number = "ForceSpotNumber"
        max_val_needed = (self.numXgridpoints * self.numYgridpoints) + 10
        self.masterpanel.variable_max_update(Spot_Number, max_val_needed)
        self.masterpanel.execute()
        return (f'Max Spot number has been updated to {max_val_needed}') 
    
    def checkbox(self):
        """
        ensures that the checkbox for whether or not the tip location shows is checked 

        Returns:
            _type_: print statement letting you know that it is checked 
        """
        self.masterpanel.show_tip_update()
        self.masterpanel.execute()
        return ("It has been checked")
    

    def create_grid_on_igor(self, sleep_time=0):
        """ 
        if you are using the marked point method, this takes the values from _raw_grid and numbers each x an y value assigns that to the numbered_grid 
        dictionary and then runs through the dictionary and creates the igor statement that will move the cursor and mark the point for each x and y value, 
        to actually send the points  

        Args:
            sleep_time (int, optional): _description_. Defaults to 0.
        """
        """ 
        if you are using the marked point method, this takes the values from _raw_grid and numbers each x an y value assigns that to the numbered_grid 
        dictionary and then runs through the dictionary and creates the igor statement that will move the cursor and mark the point for each x and y value, 
        to actually send the points  

        Args:
            sleep_time (int, optional): _description_. Defaults to 0.
        """
        self.numbered_grid = {}
        spot_start = self.masterpanel.get_params(
            ["ForceSpotNumber"],
            "ForceVariablesWave",
            "root:packages:MFP3D:main:variables",
        )
        spot_start = self.masterpanel.get_params(
            ["ForceSpotNumber"],
            "ForceVariablesWave",
            "root:packages:MFP3D:main:variables",
        )
        for ind, (x, y) in enumerate(self._raw_grid):
            self.numbered_grid[int(spot_start + ind)] = self._create_force_spot(x, y)
            self.numbered_grid[int(spot_start + ind)] = self._create_force_spot(x, y)

    def clean_up(self):
        """
        sends a command to igor that cleans off any marks created using _create_force_spot
        """
        self.masterpanel.clear_update()
        self.masterpanel.execute()

    def lvdt_grid(self,dimensions=False):
        """
        Generate a grid of locations for scanning based on device parameters and dimensions.

        This method calculates a grid of scanning locations for a scanning device based on the device's parameters,
        including scan size, offsets, ratios, and scan angle. The grid is rotated and transformed according to the parameters
        to ensure accurate mapping of physical locations to measurement points.

        Args:
            dimensions (bool, optional): Whether to include dimensions. If True, the dimensions of the grid will be returned.
                                        Defaults to False.

        Returns:
            tuple or None: If dimensions is True, returns a tuple containing the X and Y dimensions of the generated grid.
                            If dimensions is False (default), sets the 'grid_loc' attribute of the object to the generated grid.
        """
        self.make_grid(dimensions=dimensions)

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
        
        
    def lvdt_grid2(self,dimensions=False):
        """
        Generate a grid of locations for scanning based on device parameters and dimensions.

        This method calculates a grid of scanning locations for a scanning device based on the scan size and number of points in x and y

        Args:
            dimensions (bool, optional): Whether to include dimensions. If True, the dimensions of the grid will be returned.
                                        Defaults to False.

        Returns:
            tuple or None: If dimensions is True, returns a tuple containing the X and Y dimensions of the generated grid.
                            If dimensions is False (default), sets the 'grid_loc' attribute of the object to the generated grid.
        """
        self.make_grid(dimensions=dimensions)

        scansize = self.masterpanel.get_params(["ScanSize"], "MasterVariablesWave", "root:packages:MFP3D:main:variables")
       
        # Creating meshgrid
       
        GridXLocMat,GridYLocMat = np.meshgrid(
            np.linspace(0,scansize,self.numXgridpoints),
            np.linspace(0,scansize,self.numYgridpoints)
            
        )    
        
        # Transposing the matrices
        XLocVMat = GridXLocMat.T
        YLocVMat = GridYLocMat.T

        self.grid_loc = (XLocVMat, YLocVMat)    