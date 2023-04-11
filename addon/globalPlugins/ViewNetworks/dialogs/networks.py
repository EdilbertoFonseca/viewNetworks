#-*- coding: utf-8 -*-

# Dialog for viewing saved networks.
# Author: Edilberto Fonseca.
#Date of creation: 07/08/2022.

import wx
import subprocess
import addonHandler
from ui import message

addonHandler.initTranslation()


class ViewNetworks(wx.Dialog):

	def __init__(self, parent, title):
		self.title = title
		super(ViewNetworks, self).__init__(parent, title=title)
		panel = wx.Panel(self)
		boxSizer = wx.BoxSizer(wx.VERTICAL)
		listWiFiSizer= wx.BoxSizer(wx.HORIZONTAL)
		buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

		listNetworks = subprocess.check_output(['netsh', 'wlan', 'show', 'profile'], encoding='cp858')

		self.textListWifi = wx.TextCtrl(panel, -1, value=listNetworks, style = wx.TE_MULTILINE, size = (900, 400))
		listWiFiSizer.Add(self.textListWifi, 0, wx.ALL|wx.EXPAND, 5)

		self.buttonClose = wx.Button(panel, wx.ID_CANCEL, label=_('&Close'))
		self.Bind(wx.EVT_BUTTON, self.onClose, id=wx.ID_CANCEL)
		buttonSizer.Add(self.buttonClose, 0, wx.ALL|wx.EXPAND, 5)

		boxSizer.Add(listWiFiSizer)
		boxSizer.Add(buttonSizer, 0, wx.ALL|wx.CENTER, 5)
		panel.SetSizer(boxSizer)

	def onClose(self, event):
		"""Close dialog."""
		self.Destroy()
