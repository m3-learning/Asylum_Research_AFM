from pathlib import Path
from typing import Any, Literal, Type, Union
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
""" Imaging Mode options:  1-Contact, 2-AC Mode, 3-FM Mode, 4-PFM Mode, 5-Fast Force Map, 6-AC Fast Force Map, 7-FM Fast Force Map
    Last Scan options: 1-Continous Mode, 2-One Frame Mode
"""
_possible_PopupForce = Literal["DwellRampMode", "DwellSetting", "ImagingMode", "TriggerChannel", "SetSens"]
""" 
    Dwell Ramp Mode options: 1-Deflection, 2-ZSensor, 3-Other[Indentation]
    Dwell Setting options: 1-No Dwell, 2-Toward Surface, 3-Away From Surface, 4-Both
    Imaging Mode options: 1-Contact, 2-AC Mode, 3-FM Mode, 4-PFM Mode, 5-Fast Force Map, 6-AC Fast Force Map, 7-FM Fast Force Map
    Trigger Channel options: 1-None, 2-Deflection, 3-Force, 4-DeflVolts, 5-Amplitude, 6-AmpPercent, 7-Phase, 8-AmpVolts, 9-RawZSensor, 
    10-Lateral, 11-LateralVolts, 12-Bias, 13-UserIn0, 14-UserIn0Volts, 15-UserIn1, 16-UserIn1Volts, 17-UserIn2, 18-UserIn2Volts, 
    19-BackPackIn0, 20-BackPackIn0Volts, 21-BackPackIn1, 22-BackPackIn1Volts, 23-BackPackIn2, 24-BackPackIn2Volts, 25-BackPackIn3, 
    26-BackPackIn3Volts, 27-BackPackIn4, 28-BackPackIn4Volts, 29-Frequency, 30-Count, 31-Drive, 32-DriveVolts
    Set Sensitivity options: 1-Defl InvOLS, 2-Amp InvOLS   
    """
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
            variable (str): name of the variable to change, NOTE:must be exactly how it is found in igor (case sensitive)
            value (int): value to change the variable to

        Returns:
            str: string command to send to igor
        """
        return f'PV("{variable}",{value})'

    def ChangePopupImage(self, variable, value):
        """
        ChangePopupImage changes the setting of a popup menu for an image parameter in igor

        Args:
            variable (str): image popup menu variable to change
            value (int): (which choice) value to change the menu (options above)

        Returns:
            str: string command to send to igor
        """

        return f"PopupMenu {variable}Popup_0 mode={value}"

    def ChangePopupForce(self, variable, value):
        """
        ChangePopupForce Changes the setting of a popup menu for a force parameter in igor

        Args:
            variable (str): force popup menu to change
            value (int): value to change the menu to(options above)

        Returns:
            str: string command to send to igor
        """

        return f"PopupMenu {variable}Popup_1 mode={value}"

    def go_to_image_spot(self, image_posx, image_posy):
        """
        go_to_image_spot sends the image cursor to the inputted spot in igor

        Args:
            image_posx (float): image position x
            image_posy (float): image position y

        Returns:
            str: string command to send to igor
        """
        return f"ARGo2ImagePos({image_posx},{image_posy})"

    def draw_spot(self):
        """
        draw_spot draws a spot marker on an image in igor

        Returns:
            str: string command to send to igor
        """

        return r'DrawSpot("Draw")'

    def clear_spot(self):
        """
        clear_spot clears all spot markers on an image in igor

        Returns:
            str: string command to send to igor
        """

        return r'DrawSpot("Clear")'

    def change_force_spot(self, force_spot, value):
        """
        change_force_spot assigns which number marker to move the cantilever to in igor

        Args:
            force_spot (_type_): the variable FORCESPOTNUMBER in igor 
            value (_type_): the number of the marked spot that you want to move the cantilever tip to

        Returns:
            _type_: string command to send to igor 
        """
      #  print(f'PV("{force_spot}", {value})')
        return f'PV("{force_spot}", {value})'

    def tip_to_spot(self):
        """
        tip_to_spot moves cantilever to the spot in igor

        Returns:
            str: string command to send to igor
        """
        return r"GoToSpot()"
    def change_variable_max(self, variable:str, value):
        """
        change_variable_max Sets a max value of a parameter/variable within igor

        Args:
            variable (_type_):  name of the variable to change, NOTE:must be exactly how it is found in igor (case sensitive)
            value (_type_): value to change the variable's max to

          Returns:
           str: string command to send to igor
        """
        return f'PVH("{variable}", {value})'
    def td_setramp(self, xpos, ypos, max_time=0.15):
        """
        td_setramp moves cantilever to the inputted spot in igor without needing a marker

        Returns:
            str: string command to send to igor
        """
        
        return f'td_SetRamp({max_time},"PIDSloop.0.Setpoint",0, {xpos},"PIDSloop.1.Setpoint",0, {ypos} ,"",0,0,"")'
        
    def show_tip(self):
        """
        show_tip ensures that the show tip checkbox in igor is checked

        Returns:
            str: string command to send to igor
        """
        return r'CheckBox ShowXYSpotCheck_1 value=1'


    def update_params(self: Type["MasterPanel"], param: Union[str, _possible_params], value: Any):
        """
        update_params updates a parameter in igor 
        and adds the resulting igor command to the command list to be sent  


        Args:
            self (Type['MasterPanel']): MasterPanel class
            param (str or _possible_params): parm from list of possible params or user inputted string NOTE:must be exactly how it is found in igor (case sensitive)
            value (Any): value to change the parameter to
        """

        self.on_update(self.SetValue(param, value))

    def variable_max_update(self: Type["MasterPanel"], variable:str, value:Any):
        """ 
        variable_max_update creates the command that Sets a max value of a parameter/variable within igor
        and adds the resulting igor command to the command list to be sent to igor

        Args:
            self (Type['MasterPanel']): MasterPanel class
            variable (_type_): the parameter which you want to update the max value of 
            value (Any): _description_
        """
        self.on_update(self.change_variable_max(variable, value))

    def update_PopupImage(self: Type["MasterPanel"], param: Union[str, _possible_PopupImage], value: Any):
        """
        update_PopupImage Updates the popup image menu in igor 
        and adds the resulting igor command to the command list to be sent 

        Args:
            self (Type['MasterPanel']): MasterPanel class
            param (_possible_PopupImage): a variable from list of most commonly used possible image popup menus to change or user inputted string NOTE:must be exactly how it is found in igor (case sensitive)
            value (Any): value to change the popup menu to
        """
        self.on_update(self.ChangePopupImage(param, value))

    def update_PopupForce(self: Type["MasterPanel"], param: Union[str, _possible_PopupForce] , value: Any):
        """
        update_PopupForce updates the popup force menu you assign to it in igor 
        and adds the resulting igor command to the command list to be sent 

        Args:
            self (Type['MasterPanel']): MasterPanel class
            param (_possible_PopupForce): a variable from list of most commonly used possible force popup menus to change 
            or user inputted string NOTE:must be exactly how it is found in igor (case sensitive)
            value (Any): value to change the popup menu to
        """

        self.on_update(self.ChangePopupForce(param, value))

    def update_spot(self: Type["MasterPanel"], image_posx: Any, image_posy: Any):
        """ 
        update_spot creates the command that sends the image cursor to the inputted spot on a scan in igor 
        and adds the resulting igor command to the command list to be sent

        Args:
            self (Type['MasterPanel']): MasterPanel class
            image_posx (Any): x point position
            image_posy (Any): y point postion
        """
        self.on_update(self.go_to_image_spot(image_posx, image_posy))

    def draw_update(self: Type["MasterPanel"]):
        """ 
        draw_update creates the command that draws a spot mark on a scan in igor
        and adds the resulting igor command to the command list to be sent to igor

        Args:
            self (Type['MasterPanel']): MasterPanel class
        """
        self.on_update(self.draw_spot())

    def clear_update(self: Type["MasterPanel"]):
        """ 
        clear_update creates the command that clears all spot markers on an image in igor
        and adds the resulting igor command to the command list to be sent to igor

        Args:
            self (Type['MasterPanel']): MasterPanel class
        """
        self.on_update(self.clear_spot())

    def update_location(self: Type["MasterPanel"], force_spot, value: Any):
        """ 
        update_loction creates the command that assigns which number marker to move the cantilever to in igor
        and adds the resulting igor command to the command list to be sent to igor

        Args:
            self (Type['MasterPanel']): MasterPanel class
            force_spot (_type_): _description_
            value (Any): _description_
        """
        self.on_update(self.change_force_spot(force_spot, value))

    def move_location(self: Type["MasterPanel"]):
        """ 
        move_location creates the command that moves cantilever to the spot in igor
        and adds the resulting igor command to the command list to be sent to igor

        Args:
            self (Type['MasterPanel']): MasterPanel class
        """
        self.on_update(self.tip_to_spot())
    
    def td_update_move(self: Type["MasterPanel"], xpos: Any, ypos:Any, max_time=0.15):
        """ 
        td_update_move creates the command that moves cantilever to the inputted spot in igor without needing a marker
        and adds the resulting igor command to the command list to be sent to igor

        Args:
            self (Type['MasterPanel']): MasterPanel class
            xpos (Any): _description_
            ypos (Any): _description_
            max_time (float, optional): transient time. Defaults to 0.15.
        """
        self.on_update(self.td_setramp(xpos, ypos, max_time))
        
        
    def SquareWaveTrigger(self: Type["MasterPanel"],x_start,x_stop,y_start,y_stop,trigger_voltage,time_scan,time_wait):
        """
        SquareWaveTrigger creates the igor command to call the igor function to create the square wave used
        to trigger the band excitation waveform (stephen_scan_05) and adds this resulting igor command to the command list
        to be sent to igor  
        """        
        #igor_cmd = str(stephen_scan_05(x_start, x_stop, y_start, y_stop, trigger_voltage, time_scan, time_wait))
        
        self.on_update(f'stephen_scan_05({x_start}, {x_stop}, {y_start}, {y_stop}, {trigger_voltage}, {time_scan}, {time_wait})')
        
   # def setTriggerType(self: Type["MasterPanel"], ):     
        
    def show_tip_update(self: Type["MasterPanel"]):
        """ 
        show_tip_update creates the command that ensures that the show tip checkbox in igor is checked
        and adds the resulting igor command to the command list to be sent to igor

        Args:
            self (Type['MasterPanel']): MasterPanel class
        """
        self.on_update(self.show_tip())

    def on_update(self, str_update):
        """
        Update the internal command list or send a single command based on the script status.

        If the script is active, the provided `str_update` is appended to the command list.
        If the script is not active, the `str_update` is immediately sent using `write_arcmd` and `send_command`.

        Args:
            str_update (str): The command or update string to be processed.
        """
        if self.script:
            self.command_list.append(str_update)
        else:
            self.write_arcmd(str_update)
            self.send_command()

    def execute(self):
        """
        Execute the accumulated commands in the command list.

        This function writes the accumulated commands using `write_arcmd` and sends them using `send_command`.
        After execution, the command list is cleared.
        """
        self.write_arcmd(self.command_list)
        self.send_command()
        self.command_list = []