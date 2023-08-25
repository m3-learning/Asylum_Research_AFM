from pathlib import Path
from typing import Any, Literal, Type
from dataclasses import dataclass, field
from typing import List
from Asylum_Research_AFM.Core.Interface import AFM

_possible_params = Literal[
    "ScanSize",
    "PointLines",
    "ScanRate",
    "ImagingMode",
    "AmplitudeSetpointVolts",
    "DriveAmplitude",
    "DriveFrequency",
    "IntegralGain",
    "ScanSpeed",
    "ScanAngle",
    "XOffset",
    "YOffset",
    "ScanPoints",
    "ScanLines",
    "ProportionalGain",
    "FBFilterBW",
    "BaseSuffix",
    "StartDist",
    "ForceDist",
    "ForceScanRate",
    "Velocity",
    "VelocitySynch",
    "ApproachVelocity",
    "RetractVelocity",
    "DwellTime",
    "NumPtsPerSec",
    "ForceFilterBW",
    "InvOLS",
    "KappaFactor",
    "AmpInvOLS",
    "DisplaySpringConstant",
    "ForceSpotNumber",
    "TriggerPoint",
    "FmapScanTime",
    "FmapXYVelocity",
    "FMapScanPoints",
    "FMapScanLines",
    "FMapBaseSuffix",
]
_possible_PopupImage = Literal["ImagingMode", "LastScan"]

_possible_PopupForce = Literal[
    "DwellRampMode", "DwellSetting", "ImagingMode", "TriggerChannel", "SetSens"
]
force_spot = "ForceSpotNumber"


# # @dc.dataclass(kw_only=True)
# class MainPanel(AFM):
#     def __init__(self, script: bool = True, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.command_list = []
#         self.script = script

#     #     command_list: list = dc.field(default_factory=list)
#     #     script: bool = True


class MasterPanel(AFM):
    """
    MasterPanel API to set the master panel properties

    Args:
        AFM (obj): AFM class that contains the connection to the microscope
    """

    def __init__(self, script: bool = True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.command_list = []
        self.script = script

    def SetValue(self, variable, value):
        """
        SetValue Sets a value within igor

        Args:
            variable (str): name of the variable to change
            value (Any): value to change the variable to

        Returns:
            str: string command to send to igor
        """
        return f'PV("{variable}",{value})'

    def ChangePopupImage(self, variable, value):
        """
        ChangePopupImage changes the popup image in igor

        Args:
            variable (str): popup image variable to change
            value (Any): value to change the variable to

        Returns:
            str: string command to send to igor
        """

        return f"PopupMenu {variable}Popup_0 mode={value}"

    def ChangePopupForce(self, variable, value):
        """
        ChangePopupForce Changes the popup force in igor

        Args:
            variable (str): popup force variable to change
            value (Any): value to change the variable to

        Returns:
            str: string command to send to igor
        """

        return f"PopupMenu {variable}Popup_1 mode={value}"

    def igor_spot_maker(self, image_posx, image_posy):
        """
        igor_spot_maker function to create a spot in igor

        Args:
            image_posx (float): image position x
            image_posy (float): image position y

        Returns:
            str: string command to send to igor
        """
        return f"ARGo2ImagePos({image_posx},{image_posy})"

    def draw_spot(self):
        """
        draw_spot draws the spot in igor

        Returns:
            str: string command to send to igor
        """

        return r'DrawSpot("Draw")'

    def clear_spot(self):
        """
        clear_spot clears the spot in igor

        Returns:
            str: string command to send to igor
        """

        return r'DrawSpot("Clear")'

    def change_force_spot(self, force_spot, value):
        """
        change_force_spot changes the force spot in igor

        Args:
            force_spot (_type_): _description_
            value (_type_): _description_

        Returns:
            _type_: _description_
        """
        return f'PV("{force_spot}", {value})'

    def go_to_spot(self):
        """
        go_to_spot moves cantilever to the spot in igor

        Returns:
            str: string command to send to igor
        """
        return r"GoToSpot()"
    def change_variable_max(self, variable, value):
        """change_variable_max Sets a max value within igor

        Args:
            variable (_type_):  name of the variable to change
            value (_type_): value to change the variable's max to

          Returns:
           str: string command to send to igor
        """
        return f'PVH("{variable}","{value}")'
    def td_setramp(self, xpos, ypos, max_time=0.15):
        """
        td_setramp moves cantilever to the spot in igor

        Returns:
            str: string command to send to igor
        """
        
        return f'td_SetRamp({max_time},"PIDSloop.0.Setpoint",0, {xpos},"PIDSloop.1.Setpoint",0, {ypos} ,"",0,0,"")'
        
    def show_tip(self):
        return r'CheckBox ShowXYSpotCheck_1 value=1'


    def update_params(self: Type["MasterPanel"], param: _possible_params, value: Any):
        """
        update_params updates a parameter in igor

        Args:
            self (Type['MasterPanel']): MasterPanel class
            param (_possible_params): parm from list of possible params
            value (Any): value to change the parameter to
        """

        self.on_update(self.SetValue(param, value))

    def update_PopupImage(self: Type["MasterPanel"], param: _possible_PopupImage, value: Any):
        """
        update_PopupImage Updates the popup image in igor

        Args:
            self (Type['MasterPanel']): MasterPanel class
            param (_possible_PopupImage): possible popup images to change
            value (Any): value to change the popup image to
        """
        self.on_update(self.ChangePopupImage(param, value))

    def update_PopupForce(self: Type["MasterPanel"], param: _possible_PopupForce, value: Any):
        self.on_update(self.ChangePopupForce(param, value))

    def update_spot(self: Type["MasterPanel"], image_posx: Any, image_posy: Any):
        self.on_update(self.igor_spot_maker(image_posx, image_posy))

    def draw_update(self: Type["MasterPanel"]):
        self.on_update(self.draw_spot())

    def clear_update(self: Type["MasterPanel"]):
        self.on_update(self.clear_spot())

    def update_location(self: Type["MasterPanel"], force_spot, value: Any):
        self.on_update(self.change_force_spot(force_spot, value))

    def move_location(self: Type["MasterPanel"]):
        self.on_update(self.go_to_spot())
    
    def variable_max_update(self: Type["MasterPanel"], variable, value:Any):
        self.on_update(self.change_variable_max(variable, value))
    
    def td_update_move(self: Type["MasterPanel"], xpos: Any, ypos:Any, max_time=0.15):
        self.on_update(self.td_setramp(xpos, ypos, max_time))
        
    def show_update(self: Type["MasterPanel"]):
        self.on_update(self.show_tip())

    def on_update(self, str_update):
        if self.script:
            self.command_list.append(str_update)
        else:
            self.write_arcmd(str_update)
            self.send_command()

    def execute(self):
        self.write_arcmd(self.command_list)
        self.send_command()
        self.command_list = []


if __name__ == "__main__":
   # Create an instance of MasterPanel
    try:
        master_panel_instance = MasterPanel()
    except:
        pass
        # Test the show_update method
    master_panel_instance.show_update()
        # Test the execute method
    master_panel_instance.execute()

