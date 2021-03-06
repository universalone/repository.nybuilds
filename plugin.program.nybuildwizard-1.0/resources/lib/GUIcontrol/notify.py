# -*- coding: utf-8 -*-
'''#####-----XBMC Library Modules-----#####'''
'''___info__ add other xbmc library modules xbmcgui will be needed'''
import xbmc
import xbmcgui


'''######------External Modules-----#####'''
'''___info__ add External Modules that are required'''
from addonvar import *

'''#####-----Internal Modules-----#####'''
'''___info__ add Internal Modules from your script that are required'''

'''#####-----Actions from inputs via remote keyboard etc-----#####'''

ACTION_LEFT = 1
ACTION_RIGHT = 2
ACTION_UP = 3
ACTION_DOWN = 4
ACTION_PAGE_UP = 5
ACTION_PAGE_DOWN = 6
ACTION_SELECT_ITEM = 7
ACTION_PARENT_DIR = 9
ACTION_PREVIOUS_MENU = 10
ACTION_SHOW_INFO = 11
ACTION_STOP = 13
ACTION_NEXT_ITEM = 14
ACTION_PREV_ITEM = 15
ACTION_SHOW_CODEC = 27
ACTION_SHOW_FULLSCREEN = 36
ACTION_DELETE_ITEM = 80
ACTION_MENU = 163
ACTION_LAST_PAGE = 160
ACTION_RECORD = 170

ACTION_CREATE_BOOKMARK = 96

ACTION_PAUSE = 12
ACTION_PLAY = 68
ACTION_PLAYER_FORWARD = 77
ACTION_PLAYER_PLAY = 79
ACTION_PLAYER_PLAYPAUSE = 229
ACTION_PLAYER_REWIND = 78

ACTION_MOUSE_WHEEL_UP = 104
ACTION_MOUSE_WHEEL_DOWN = 105
ACTION_MOUSE_MOVE = 107
ACTION_MOUSE_LEFT_CLICK = 100

KEY_NAV_BACK = 92
KEY_CONTEXT_MENU = 117
KEY_HOME = 159
KEY_ESC = 61467

REMOTE_0 = 58
REMOTE_1 = 59
REMOTE_2 = 60
REMOTE_3 = 61
REMOTE_4 = 62
REMOTE_5 = 63
REMOTE_6 = 64
REMOTE_7 = 65
REMOTE_8 = 66
REMOTE_9 = 67

ACTION_JUMP_SMS2 = 142
ACTION_JUMP_SMS3 = 143
ACTION_JUMP_SMS4 = 144
ACTION_JUMP_SMS5 = 145
ACTION_JUMP_SMS6 = 146
ACTION_JUMP_SMS7 = 147
ACTION_JUMP_SMS8 = 148
ACTION_JUMP_SMS9 = 149

class notify(xbmcgui.WindowXMLDialog):

	'''
	___info__ add buttons and controls,similar to example below
	BUTTON_CLOSE = 100
	HEADING_CTRL = 200
	TEXT_CTRL    = 201
	'''

	def __new__(cls,*args,**kwargs):
		return super(notify, cls).__new__(cls,'notify.xml', addon_path,'Default','720p')
		'''___info___
		xmlFilename	string - the name of the xml file to look for.
		scriptPath	string - path to script. used to fallback to if the xml doesn't exist in the current skin. (eg xbmcaddon.Addon().getAddonInfo('path'))
		defaultSkin	[opt] string - name of the folder in the skins path to look in for the xml. (default='Default')
		defaultRes	[opt] string - default skins resolution. (1080i, 720p, ntsc16x9, ntsc, pal16x9 or pal. default='720p')
		'''

	def __init__(self,*args,**kwargs):
		super(notify,self).__init__()
		'''
		___info__ addcode items you wish to be run when class is called
		'''

	def onInit(self):
		#xbmc.sleep(1000)
		#self.Close()
		'''
		onInit method.

		This method will be called to initialize of the window

		Parameters
				self	Own base class pointer
		Example:
				Define own function where becomes called from Kodi
				def onInit(self):
					print("Window.onInit method called from Kodi")
		'''
		pass

	def onAction(self,action):
		if action.getId() == KEY_NAV_BACK:
			self.Close()
		'''
		onAction method.

		This method will receive all actions that the main program will send to this window.

		Parameters
			self	Own base class pointer
			action	The action id to perform, see Action to get use of them
		Note
		By default, only the PREVIOUS_MENU and NAV_BACK actions are handled.
		Overwrite this method to let your script handle all actions.
		Don't forget to capture ACTION_PREVIOUS_MENU or ACTION_NAV_BACK, else the user can't close this window.
		Example:
			# Define own function where becomes called from Kodi
			def onAction(self, action):
			  if action.getId() == ACTION_PREVIOUS_MENU:
				print('action received: previous')
				self.close()
			  if action.getId() == ACTION_SHOW_INFO:
				print('action received: show info')
			  if action.getId() == ACTION_STOP:
				print('action received: stop')
			  if action.getId() == ACTION_PAUSE:
				print('action received: pause')
		'''
		pass

	def onClick(self,controlId):
		'''
		onClick method.

					This method will receive all click events that the main program will send to this window.

		Parameters
					self	Own base class pointer
		controlId	The one time clicked GUI control identifier
		Example:
				# Define own function where becomes called from Kodi
				def onClick(self,controlId):
					if controlId == 10:
						print("The control with Id 10 is clicked")
		'''
		pass

	def onControl(self,control):
		'''
		Function: onControl(self, Control)
				onControl method.

		This method will receive all click events on owned and selected controls when the control itself doesn't handle the message.

		Parameters
			self	Own base class pointer
			control	The Control class
		Example:
			# Define own function where becomes called from Kodi
			def onControl(self, control):
				print("Window.onControl(control=[%s])"%control)
		'''
		pass

	def onDoubleClick(self,controlId):
		'''
		Function: onDoubleClick(self, int controlId)
				onDoubleClick method.

		This method will receive all double click events that the main program will send to this window.

		Parameters
				self	Own base class pointer
				controlId	The double clicked GUI control identifier
		Example:
				# Define own function where becomes called from Kodi
				def onDoubleClick(self,controlId):
				  if controlId == 10:
					print("The control with Id 10 is double clicked")
		'''
		pass

	def onFocus(self,controlId):
		'''
		Function: onFocus(self, int controlId)
				onFocus method.

		This method will receive all focus events that the main program will send to this window.

		Parameters
			self	Own base class pointer
			controlId	The focused GUI control identifier
		Example:
		# Define own function where becomes called from Kodi
		def onDoubleClick(self,controlId):
		   if controlId == 10:
		   print("The control with Id 10 is focused")
		'''
		pass
		
	def Close(self):
		super(notify,self).close()
		'''
		Function: close()
			Closes this window.

		Closes this window by activating the old window.

		Note
			The window is not deleted with this method. 
		'''




