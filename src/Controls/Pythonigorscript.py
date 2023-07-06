Function SendScript()

	String Evil = ""
	Evil += "@echo off"+"\r"
	Evil += "\"C:\\Users\\Asylum User\\anaconda3\\python.exe\""
	Evil += " "+"\"C:\Users\Asylum User\Documents\code\Asylum_Research_AFM\Test Script.py"+"\r"
	Evil += "pause"+"\r"
	RunDosCMD(Evil)
End //