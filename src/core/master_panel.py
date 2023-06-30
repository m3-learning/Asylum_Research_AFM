from ..core.Interface import AFM

class MainPanel(AFM):

    def __init__(self, script = True):
        super().__init__
        self.command_list = []

    def SetValue(self, variable, value):
        return f'PV(\"{variable}\",{value})'

    def ScanSize(self, value):
        string_command = self.SetValue("ScanSize", value)
        self.on_update(string_command)
    # to Replace the necessary command refer to Variable4masterPanel     

    def on_update(self, str_update):
        if self.script:
            self.command_list.append(str_update)
        else:
            self.write_arcmd(str_update)
            self.send_command()

    # TODO add setter and return statement for command list

     