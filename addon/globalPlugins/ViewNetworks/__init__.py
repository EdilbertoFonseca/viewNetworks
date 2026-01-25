# -*- coding: UTF-8 -*-

"""
Author: Edilberto Fonseca <edilberto.fonseca@outlook.com>
Copyright: (C) 2025 Edilberto Fonseca

This file is covered by the GNU General Public License.
See the file COPYING for more details or visit:
https://www.gnu.org/licenses/gpl-2.0.html

Created on: 07/08/2022
"""

import addonHandler
import globalPluginHandler
import gui
import wx
from logHandler import log
from scriptHandler import script

# imports from the View Networks addon.
from .main import ViewNetworks

# Config# Get the add-on summary contained in the manifest.
ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]

# Initialize translation support
addonHandler.initTranslation()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu

		# Translators: Creates the item in the NVDA menu.
		self.menuItem = self.toolsMenu.Append(wx.ID_ANY, "&{}...".format(ADDON_SUMMARY))

		# Vincular ação ao item
		gui.mainFrame.sysTrayIcon.Bind(
			wx.EVT_MENU,
			self.script_networks,
			self.menuItem 
		)

	@script(
		gesture="kb:Windows+alt+N",
		description=_("Displays the networks you have connected to."),
		category=ADDON_SUMMARY,
	)
	def script_networks(self, gesture):
		# Translators: title of the profiles dialog in the Wireless Network Connection interface.
		self.dlg = ViewNetworks(gui.mainFrame, _("Network Profiles"))
		gui.mainFrame.prePopup()
		self.dlg.Centre()
		self.dlg.Show()
		gui.mainFrame.postPopup()

	def terminate(self):
		try:
			self.toolsMenu.Remove(self.menuItem)
		except Exception as e:
			log.warning(f"Error removing Scraps and agenda organizer menu item: {e}")
