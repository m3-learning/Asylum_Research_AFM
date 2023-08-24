# for the imaging tab of the panel
def ScanSize(self, value):
    string_command = self.SetValue("ScanSize", value)
    self.on_update(string_command)


def PointLines(self, value):
    string_command = self.SetValue("PointLines", value)
    self.on_update(string_command)


def ScanRate(self, value):
    """Set the AFM Scan rate in Hz"""
    string_command = self.SetValue("ScanRate", value)
    self.on_update(string_command)


def AmplitudeSetpointVolts(self, value):
    """Sets the amplitude setpoint in volts"""
    string_command = self.SetValue("AmplitudeSetpointVolts", value)
    self.on_update(string_command)


def DriveAmplitude(self, value):
    """Sets the amplitude of the drive in volts"""
    string_command = self.SetValue("DriveAmplitude", value)
    self.on_update(string_command)


def DriveFrequency(self, value):
    """Sets the frequency of the drive in Hz"""
    string_command = self.SetValue("DriveFrequency", value)
    self.on_update(string_command)


def IntegralGain(self, value):
    """
    IntegralGain sets the integral gain for the feedback loop.

    Args:
        value (float): value for the integral gain
    """
    string_command = self.SetValue("IntegralGain", value)
    self.on_update(string_command)


def ScanSpeed(self, value):
    string_command = self.SetValue("ScanSpeed", value)
    self.on_update(string_command)


def ScanAngle(self, value):
    string_command = self.SetValue("ScanAngle", value)
    self.on_update(string_command)


def XOffset(self, value):
    string_command = self.SetValue("XOffset", value)
    self.on_update(string_command)


def YOffset(self, value):
    string_command = self.SetValue("YOffset", value)
    self.on_update(string_command)


def ScanPoints(self, value):
    string_command = self.SetValue("ScanPoints", value)
    self.on_update(string_command)


def ScanLines(self, value):
    string_command = self.SetValue("ScanLines", value)
    self.on_update(string_command)


def ProportionalGain(self, value):
    string_command = self.SetValue("ProportionalGain", value)
    self.on_update(string_command)


def FBFilterBW(self, value):
    string_command = self.SetValue("FBFilterBW", value)
    self.on_update(string_command)


def BaseSuffix(self, value):
    string_command = self.SetValue("BaseSuffix", value)
    self.on_update(string_command)


# for the Force tab
def StartDist(self, value):
    string_command = self.SetValue("StartDist", value)
    self.on_update(string_command)


def ForceDist(self, value):
    string_command = self.SetValue("ForceDist", value)
    self.on_update(string_command)


def ForceScanRate(self, value):
    string_command = self.SetValue("ForceScanRate", value)
    self.on_update(string_command)


def Velocity(self, value):
    string_command = self.SetValue("Velocity", value)
    self.on_update(string_command)


def ApproachVelocity(self, value):
    string_command = self.SetValue("ApproachVelocity", value)
    self.on_update(string_command)


def RetractVelocity(self, value):
    string_command = self.SetValue("RetractVelocity", value)
    self.on_update(string_command)


def DwellTime(self, value):
    string_command = self.SetValue("DwellTime", value)
    self.on_update(string_command)


def NumPtsPerSec(self, value):
    string_command = self.SetValue("NumPtsPerSec", value)
    self.on_update(string_command)


def ForceFilterBW(self, value):
    string_command = self.SetValue("ForceFilterBW", value)
    self.on_update(string_command)


def InvOLS(self, value):
    string_command = self.SetValue("InvOLS", value)
    self.on_update(string_command)


def KappaFactor(self, value):
    string_command = self.SetValue("KappaFactor", value)
    self.on_update(string_command)


def AmpInvOLS(self, value):
    string_command = self.SetValue("AmpInvOLS", value)
    self.on_update(string_command)


def DisplaySpringConstant(self, value):
    string_command = self.SetValue("DisplaySpringConstant", value)
    self.on_update(string_command)


def ForceSpotNumber(self, value):
    string_command = self.SetValue("ForceSpotNumber", value)
    self.on_update(string_command)


def TriggerPoint(self, value):
    string_command = self.SetValue("TriggerPoint", value)
    self.on_update(string_command)


# Fmap
def FmapScanTime(self, value):
    string_command = self.SetValue("FmapScanTime", value)
    self.on_update(string_command)


def FmapXYVelocity(self, value):
    string_command = self.SetValue("FmapXYVelocity", value)
    self.on_update(string_command)


def FMapScanPoints(self, value):
    string_command = self.SetValue("FMapScanPoints", value)
    self.on_update(string_command)


def FMapScanLines(self, value):
    string_command = self.SetValue("FMapScanLines", value)
    self.on_update(string_command)


def FMapBaseSuffix(self, value):
    string_command = self.SetValue("FMapBaseSuffix", value)
    self.on_update(string_command)
