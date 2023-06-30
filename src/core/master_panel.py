from typing import Any, Literal, Self
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

@dc.dataclass
class MainPanel(AFM):
    command_list: list = dc.field(default_factory=list())
    script: bool = True
    
    def SetValue(self, variable, value):
        return f'PV(\"{variable}\",{value})'

    def update_params(self: Self, param: _possible_params, value: Any):
        self.on_update(self.SetValue(param, value))  

    def on_update(self, str_update):
        if self.script:
            self.command_list.append(str_update)
        else:
            self.write_arcmd(str_update)
            self.send_command()

    # TODO add setter and return statement for command list

     