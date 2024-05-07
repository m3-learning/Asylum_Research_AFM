from subprocess import Popen, TimeoutExpired
import tempfile
from pathlib import Path
from typing import List
from igor_activex import get_wave_data
from dataclasses import dataclass, field


@dataclass
class AFM:
    """
    AFM class for managing Asylum Research AFM operations.

    Parameters:
        igor_path (Path): The path to the Igor Pro executable.
        basepath (Path, optional): The base directory for storing temporary files.
            If not provided, a temporary directory will be created.
        filename (str, optional): The base filename for the generated files.
        verbose (bool, optional): If True, print verbose output. Default is False.
    """

    igor_path: Path = Path(r"C:\AsylumResearch\v19\RealTime\Igor Pro Folder\Igor.exe")
    basepath: Path = field(default_factory= Path(tempfile.mkdtemp()).absolute())
    filename: str = 'ToIgor'
    verbose: bool = False
    arcmd: Path = field(init=False)
    bat: Path = field(init=False)

    def __post_init__(self):
        """
        Initialize paths and create BAT file.
        """
        self.arcmd = self.basepath / f'{self.filename}.arcmd'
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
