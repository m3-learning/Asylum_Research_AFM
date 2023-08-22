from subprocess import Popen, TimeoutExpired
import tempfile
from pathlib import Path

from .igor_activex import get_wave_data
from typing import List


class AFM:

    def __init__(self, igor_path:Path=Path(r"C:\AsylumResearch\v19\RealTime\Igor Pro Folder\Igor.exe"), basepath: Path=None, filename='ToIgor', verbose = False):  # noqa: E501

        if not basepath:
            basepath = Path(tempfile.mkdtemp())
        self.basepath = basepath.absolute()
        self.igor_path = igor_path
        self.filename = filename
        self.arcmd = self.basepath / f'{self.filename}.arcmd'
        self.verbose = verbose
        self.bat = self.basepath / f'{self.filename}.bat'
        self.write_bat()

    @property
    def cmd_basepath(self) -> Path:
        return self.basepath

    @property
    def cmd_igor_path(self):
        return self.igor_path

    def write_file(self, file, content):

        if isinstance(content, str):
            content = [content]

        with open(file, 'w') as f:
            for line in content:
                f.write(line + '\n')

    def write_bat(self):
        # arcmd = self.arcmd.replace("\\\\","\\")
        content = f'@echo off\n\"{self.igor_path}\" \"{self.arcmd}\"'
        self.write_file(self.bat, content)


    def write_arcmd(self, content):
        self.write_file(self.arcmd, content)


    def send_command(self):
        p = Popen(self.bat)
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
