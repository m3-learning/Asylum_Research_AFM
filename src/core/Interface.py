from subprocess import Popen, TimeoutExpired
from .igor_activex import get_wave_data
from typing import List


class AFM:

    def __init__(self, igor_path=r"C:\AsylumResearch\v19\RealTime\Igor Pro Folder\Igor.exe", basepath='./', filename='ToIgor', verbose = False):  # noqa: E501

        self.basepath = basepath
        self.igor_path = igor_path
        self.filename = filename
        self.arcmd = f"{self.cmd_basepath}\\\\{self.filename}.arcmd"
        self.verbose = verbose
        self.bat = f"{self.cmd_basepath}\\\\{self.filename}.bat"
        self.write_bat()

    @property
    def cmd_basepath(self):
        return self.basepath.replace("\\", "\\\\")

    @property
    def cmd_igor_path(self):
        return self.igor_path.replace("\\", "\\\\")

    def write_file(self, file, content):
        
        if isinstance(content, str):
            content = [content]
        
        with open(file, 'w') as f:
            for line in content:
                f.write(line + '\n')
                
    def write_bat(self):
        arcmd = self.arcmd.replace("\\\\","\\")
        content = f'@echo off\n\"{self.igor_path}\" \"{arcmd}\"'
        self.write_file(self.bat, content)
        
    def write_arcmd(self, content):
        self.write_file(self.arcmd, content)

    def send_command(self):
        p = Popen(self.bat.replace("\\\\","\\"))
        try:
            outs, errs = p.communicate(timeout=15)
        except TimeoutExpired:
            p.kill()
            outs, errs = p.communicate()
        
        if self.verbose:
            return outs, errs
        
    def get_params(self, param_list: List[str], wave_name: str, wave_folder: str):
        param_dict = get_wave_data(wave_name, wave_folder)
        params = {}
        for key, value in param_dict.items():
            if key in param_list:
                params[key] = value
        if len(param_list) == 1:
            return params[param_list[0]]
        else:
            return params
