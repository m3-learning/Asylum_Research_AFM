from typing import Any, Literal, Type
import dataclasses as dc
from src.core.Interface import AFM

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

@dc.dataclass
class MainPanel(AFM):
    command_list: list = dc.field(default_factory=list)
    script: bool = True
        
    def SetValue(self, variable, value):
        return f'PV(\"{variable}\",{value})'
    
    def ChangePopUpImage(self, variable, value):
        return f'PopupMenu {variable}Popup_0 mode={value}'
      
    def ChangePopUpForce(self, variable, value):
        return f'PopupMenu {variable}Popup_1 mode={value}'

    def update_params(self: Type['MainPanel'], param: _possible_params, value: Any):
        self.on_update(self.SetValue(param, value))  

    def update_PopupImage(self: Type['MainPanel'], param: _possible_PopupImage, value: Any):
        self.on_update(self.ChangePopUpImage(param, value))  

    def update_PopupForce(self: Type['MainPanel'], param: _possible_PopupForce, value: Any):
        self.on_update(self.ChangePopUpForce(param, value))  

    def on_update(self, str_update):
        if self.script:
            self.command_list.append(str_update)
        else:
            self.write_arcmd(str_update)
            self.send_command()

    
    # TODO add setter and return statement for command list

     