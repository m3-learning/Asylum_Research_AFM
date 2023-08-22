from src.Controls.master_panel import *


if __name__ == "__main__":
    basepath = r"C:\Users\Asylum User\Documents\code\junk"
    afm = AFM(basepath=basepath)
    main_panel = MainPanel() 
    main_panel.update_spot(7e-6, 6e-6) 
    main_panel.draw_update()
    spotnumber = afm.get_params(["ForceSpotNumber"], "ForceVariablesWave","root:packages:MFP3D:main:variables")
    main_panel.script = True 
    print(main_panel.command_list)
    afm.write_arcmd(main_panel.command_list)
    afm.send_command()
    pass