class AFM:

    def __init__(self, igor_path=r"C:\AsylumResearch\v18\Igor Pro Folder\Igor.exe", basepath='./', filename='ToIgor'):

        self.basepath = basepath
        self.igor_path = igor_path.replace("/", "\\")
        self.filename = filename
        self.bat = f"{self.cmd_basepath}\\{self.filename}.bat"
        self.arcmd = f"{self.cmd_basepath}\\{self.filename}.arcmd"

        self.write_bat()

    @property
    def cmd_basepath(self):
        return self.basepath.replace("/", "\\")

    @property
    def cmd_igor_path(self):
        return self.igor_path.replace("/", "\\")

    def write_file(self, file, content):
        
        if isinstance(content, str):
            content = [content]
        
        with open(file, 'w') as f:
            for line in content:
                f.write(line + '\n')
                
    def write_bat(self):
        
        content = f'@echo off\n\"{self.igor_path}\" \"{self.bat}\"'
        self.write_file(self.bat, content)
        
    def write_arcmd(self, content):
        self.write_file(self.arcmd, content)
    