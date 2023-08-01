
from typing import Any, Literal, Type
import dataclasses as dc
from ..core.Interface import AFM

_possible_params = Literal["ScanSize",
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
    "FMapBaseSuffix",]
_possible_PopupImage = Literal["ImagingMode", "LastScan"]

_possible_PopupForce = Literal["DwellRampMode", "DwellSetting", "ImagingMode", "TriggerChannel", "SetSens"]
force_spot = 'ForceSpotNumber'
@dc.dataclass
class MainPanel(AFM):
    command_list: list = dc.field(default_factory=list)
    script: bool = True
        
    def SetValue(self, variable, value):
        return f'PV(\"{variable}\",{value})'
    
    def ChangePopupImage(self, variable, value):
        return f'PopupMenu {variable}Popup_0 mode={value}'
      
    def ChangePopupForce(self, variable, value):
        return f'PopupMenu {variable}Popup_1 mode={value}'
    
    def igor_spot_maker(self, image_posx,image_posy):
        return f'ARGo2ImagePos({image_posx},{image_posy})'
    
    def draw_spot(self):
        return f'DrawSpot(\"Draw\")'
    
    def change_force_spot(self, force_spot , value):
        return f'PV(\"{force_spot}\", {value})'
    
    def go_to_spot(self):
        return f'GoToSpot()'

    def update_params(self: Type['MainPanel'], param: _possible_params, value: Any):
        self.on_update(self.SetValue(param, value))  

    def update_PopupImage(self: Type['MainPanel'], param: _possible_PopupImage, value: Any):
        self.on_update(self.ChangePopupImage(param, value))  

    def update_PopupForce(self: Type['MainPanel'], param: _possible_PopupForce, value: Any):
        self.on_update(self.ChangePopupForce(param, value))  
    
    def update_spot(self: Type['MainPanel'], image_posx: Any, image_posy:Any):
        self.on_update(self.igor_spot_maker(image_posx,image_posy)) 
    
    def draw_update(self: Type['MainPanel']):
        self.on_update(self.draw_spot()) 

    def update_location(self: Type['MainPanel'], force_spot, value:Any ):
        self.on_update(self.change_force_spot(force_spot,value)) 
    
    def move_location(self: Type['MainPanel']):
        self.on_update(self.go_to_spot()) 


    def on_update(self, str_update):
        if self.script:
            self.command_list.append(str_update)
        else:
            self.write_arcmd(str_update)
            self.send_command()

    
    # TODO add setter and return statement for command list

     
