# -*- coding: UTF-8 -*-

# Description: Dialog for viewing saved networks.
# Author: Edilberto Fonseca.
# Email: edilberto.fonseca@outlook.com.
# Date of creation: 07/08/2022.

# Standard Python imports.
import subprocess

import addonHandler
import queueHandler
import ui
import wx

# For translation process
addonHandler.initTranslation()

# Get the title of the addon defined in the summary.
ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]


class ViewNetworks(wx.Dialog):
	"""Initialize the dialog for viewing saved networks."""
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(ViewNetworks, cls).__new__(cls, *args, **kwargs)
		else:
			msg = _("An instance of {} is already open.").format(ADDON_SUMMARY)
			queueHandler.queueFunction(queueHandler.eventQueue, ui.message, msg)
		return cls._instance

	def __init__(self, parent, title):
		if hasattr(self, "initialized"):
			return
		self.initialized = True

		self.title = title
		super(ViewNetworks, self).__init__(parent, title=title)
		panel = wx.Panel(self)
		boxSizer = wx.BoxSizer(wx.VERTICAL)
		listWiFiSizer = wx.BoxSizer(wx.HORIZONTAL)
		buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

		# Attempt to retrieve the list of saved Wi-Fi networks.
		try:
			listNetworks = subprocess.check_output(['netsh', 'wlan', 'show', 'profile'], encoding='cp850')
		except (subprocess.CalledProcessError, FileNotFoundError) as e:
			listNetworks = _("Error fetching networks: ") + str(e)

		# Display the list of networks in a read-only text control.
		self.textListWifi = wx.TextCtrl(
			panel, -1, value=listNetworks, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(480, 400))
		listWiFiSizer.Add(self.textListWifi, 1, wx.ALL | wx.EXPAND, 5)

		# Add a Close button to the dialog.
		self.buttonClose = wx.Button(panel, wx.ID_CANCEL, label=_('&Close'))
		self.Bind(wx.EVT_BUTTON, self.onClose, id=wx.ID_CANCEL)
		buttonSizer.Add(self.buttonClose, 0, wx.ALL | wx.CENTER, 5)

		# Add the sizers to the main sizer and set it on the panel.
		boxSizer.Add(listWiFiSizer, 1, wx.ALL | wx.EXPAND, 5)
		boxSizer.Add(buttonSizer, 0, wx.ALL | wx.CENTER, 5)
		panel.SetSizerAndFit(boxSizer)

	def onClose(self, event):
		"""Close the dialog."""
		self.Destroy()
