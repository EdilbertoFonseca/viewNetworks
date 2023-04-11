#-*- coding: utf-8 -*-

# This add-on lists all the networks you have ever connected to.
# And try as far as possible to display the password.
# Note: This add-on does not break passwords or try to do so, it is only for recovering # passwords that for some reason you forgot.
# Author: Edilberto Fonseca.
# Creation date: 07/08/2022.

import globalPluginHandler
from scriptHandler import script
import addonHandler
import wx
import gui
import os
from .dialogs.networks import ViewNetworks
from .dialogs.password import ViewPassword

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
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_networks, networck)

		# Translators: Search the networks and try to recover the password.
		recoverPassword = self.mainMenu.Append(-1, _('&Recover Password'))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_recoverPassword, recoverPassword)

		# Translators: Menu About the addon.
		about = self.mainMenu.Append(-1, _('&About'))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_showAbout, about)

		# Translators: Open the help page.
		help = self.mainMenu.Append(-1, _('&Help'))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_onHelp, help)

		# Translators: Creates the item in the NVDA menu.
		toolsMenu.AppendSubMenu(self.mainMenu, _('&View Networks'))

	@script(gesture='kb:Windows+alt+N', description=_('Displays the networks you have connected to.'), category=_('View Networks'))
	def script_networks(self, gesture):
		# Translators: title of the profiles dialog in the Wireless Network Connection interface.
		self.dlg = ViewNetworks(gui.mainFrame, _('Network Profiles'))
		gui.mainFrame.prePopup()
		self.dlg.Show()
		self.dlg.Centre()
		gui.mainFrame.postPopup()

	@script(gesture='kb:Windows+alt+P', description=_('Recover saved networks password.'), category=_('View Networks'))
	def script_recoverPassword(self, gesture):
		# Translators: Title of the Recover Password dialog.
		self.dlg = ViewPassword(gui.mainFrame, _('Recover Password.'))
		gui.mainFrame.prePopup()
		self.dlg.Show()
		self.dlg.Centre()
		gui.mainFrame.postPopup()

	@script(gesture='kb:Windows+alt+O',description=_('About the ViewNetworks Add-on.'), category=_('View Networks'))
	def script_showAbout(self, gesture):
		def showAbout():
			summary = _('Summary: {}\n').format(addonHandler.getCodeAddon().manifest['summary'])
			version = _('Version: {}\n').format(addonHandler.getCodeAddon().manifest['version'])
			description = _('Description: {}\n').format(addonHandler.getCodeAddon().manifest['description'])
			author = _('Autor: {}\n\n').format(addonHandler.getCodeAddon().manifest['author'])
			minimumNVDAVersion = _('Minimum version of NVDA required: {}\n').format(addonHandler.getCodeAddon().manifest['minimumNVDAVersion'])
			lastTestedNVDAVersion = _('Latest version of NVDA tested: {}').format(addonHandler.getCodeAddon().manifest['lastTestedNVDAVersion'])

			gui.messageBox( # Translators: About the addon.
			summary +
			version +
			description +
			author +
			minimumNVDAVersion +
			lastTestedNVDAVersion,
			_('Add-on information'))
		wx.CallAfter(showAbout)

	@script(gesture='kb:Windows+alt+J', description=_('Opens the ViewNetworks add-on help page.'), category=_('View Networks'))
	def script_onHelp(self, gesture):
		"""Open the addon's help page"""
		wx.LaunchDefaultBrowser(addonHandler.Addon(os.path.join(os.path.dirname(__file__), "..", "..")).getDocFilePath())
