import keyboard


#These are the lists of apps and their passwords.
adp_Password = "Your Password Here"
outlook_Password = "Your Password Here"

#Making functions for each shortcut so when you click your shortcut keys it knows what to do and made it a function for easy adding and removing of stuff for it to do.
def adp_Action():
	#This will print the ADP password
	keyboard.write(adp_Password)

def outlook_Action():
	#This will print the Outlook password
	keyboard.write(outlook_Password)

#Registered shortcuts
keyboard.add_hotkey('shift+alt+a', adp_Action)
keyboard.add_hotkey('shift+alt+o', outlook_Action)

#Keeps the program running with a message at the beginning when its started up. Uses ESC as a out to quit the program.
print('Listening, press ESC to stop')
keyboard.wait('esc')
print('Stopped')
