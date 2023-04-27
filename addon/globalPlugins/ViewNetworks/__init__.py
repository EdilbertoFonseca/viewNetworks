# -*- coding: utf-8 -*-

# This add-on lists all the networks you have ever connected to.
# And try as far as possible to display the password.
# Note: This add-on does not break passwords or try to do so, it is only for recovering # passwords that for some reason you forgot.
# Author: Edilberto Fonseca.
# Creation date: 07/08/2022.

# Standard Python imports.
import os

# Standard NVDA imports.
import globalPluginHandler
from scriptHandler import script
import addonHandler
import wx
import gui

# imports from the View Networks addon.
from .dialogs.networks import ViewNetworks
from .dialogs.password import ViewPassword

# For translation process
addonHandler.initTranslation()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.create_menu()

	def create_menu(self):
		self.mainMenu = wx.Menu()
		toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu

		# Translators: Lists the profiles in the Wireless Network Connection interface.
		networck = self.mainMenu.Append(-1, _('&Network Profiles'))
		gui.mainFrame.sysTrayIcon.Bind(
			wx.EVT_MENU, self.script_networks, networck)

		# Translators: Search the networks and try to recover the password.
		recoverPassword = self.mainMenu.Append(-1, _('&Recover Password'))
		gui.mainFrame.sysTrayIcon.Bind(
			wx.EVT_MENU, self.script_recoverPassword, recoverPassword)

		# Translators: Creates the item in the NVDA menu.
		toolsMenu.AppendSubMenu(self.mainMenu, _('&View Networks'))

	@script(
		gesture='kb:Windows+alt+N',
		description=_('Displays the networks you have connected to.'),
		category=_('View Networks')
	)
	def script_networks(self, gesture):
		# Translators: title of the profiles dialog in the Wireless Network Connection interface.
		self.dlg = ViewNetworks(gui.mainFrame, _('Network Profiles'))
		gui.mainFrame.prePopup()
		self.dlg.Show()
		self.dlg.Centre()
		gui.mainFrame.postPopup()

	@script(
		gesture='kb:Windows+alt+P',
		description=_('Recover saved networks password.'),
		category=_('View Networks')
	)
	def script_recoverPassword(self, gesture):
		# Translators: Title of the Recover Password dialog.
		self.dlg = ViewPassword(gui.mainFrame, _('Recover Password.'))
		gui.mainFrame.prePopup()
		self.dlg.Show()
		self.dlg.Centre()
		gui.mainFrame.postPopup()
