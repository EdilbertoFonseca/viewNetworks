#-*- coding: utf-8 -*-

# Dialog to recover the password.
# Author: Edilberto Fonseca.
#Date of creation: 07/08/2022.

# Standard Python imports.
import subprocess

# Standard NVDA imports.
import wx
import addonHandler

# For translation process
addonHandler.initTranslation()


class ViewPassword(wx.Dialog):

	def __init__(self, parent, title):
		self.title = title
		super(ViewPassword, self).__init__(parent, title=title)
		panel = wx.Panel(self)
		boxSizer = wx.BoxSizer(wx.VERTICAL)
		searchSizer= wx.BoxSizer(wx.HORIZONTAL)
		buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

		labelSearch = wx.StaticText(panel, label=_('Enter the network name: '))
		searchSizer.Add(labelSearch, 0, wx.ALL|wx.EXPAND, 5)

		self.textSearch = wx.TextCtrl(panel, -1)
		searchSizer.Add(self.textSearch, 0, wx.ALL|wx.EXPAND, 5)

		labelContent = wx.StaticText(panel, label=_('key content: '))
		searchSizer.Add(labelContent, 0, wx.ALL|wx.EXPAND, 5)

		self.textKeyContent = wx.TextCtrl(panel, -1)
		self.textKeyContent.Enable(False)
		searchSizer.Add(self.textKeyContent, 0, wx.ALL|wx.EXPAND, 5)

		buttonSearch = wx.Button(panel, -1, label=_('&Search'))
		self.Bind(wx.EVT_BUTTON, self.onSearch, buttonSearch)
		buttonSizer.Add(buttonSearch, 0, wx.ALL|wx.EXPAND, 5)

		buttonClean = wx.Button(panel, -1, label=_('C&lean'))
		self.Bind(wx.EVT_BUTTON, self.onClean, buttonClean)
		buttonSizer.Add(buttonClean, 0, wx.ALL|wx.EXPAND, 5)

		buttonClose = wx.Button(panel, wx.ID_CANCEL, label=_('&Close'))
		self.Bind(wx.EVT_BUTTON, self.onClose, id=wx.ID_CANCEL)
		buttonSizer.Add(buttonClose, 0, wx.ALL|wx.EXPAND, 5)

		boxSizer.Add(searchSizer)
		boxSizer.Add(buttonSizer, 0, wx.ALL|wx.CENTER, 5)
		panel.SetSizer(boxSizer)

	def onSearch(self, event):
		"""Search for a certain network, and try to recover your password."""

		nameWiFi = self.textSearch.GetValue()

		try:
			information = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', nameWiFi, 'key=clear'], encoding='cp858')
			for line in information.split('\n'):
				if "Conteúdo da Chave" in line:
					# getting the password
					pos = line.find(':')
					password = line[pos+2:]
					self.textKeyContent.Enable(True)
					self.textKeyContent.SetValue(password)
					self.textKeyContent.SetFocus()
		except:
			if self.textKeyContent == None:
				# Translators: Message displayed when key content cannot be obtained.
				wx.MessageBox(_('Unable to get network key content {}!').format(nameWiFi), _('Atention'))
				self.textSearch.Clear()
				self.textSearch.SetFocus()
			else:
				 # Translators: Message displayed when the network is not found.
				wx.MessageBox(_('Could not get network information {}!').format(nameWiFi), _('Atention'))
				self.textSearch.Clear()
				self.textSearch.SetFocus()

	def onClean(self, event):
		"""Clear the fields for a future search."""
		self.textSearch.Clear()
		self.textKeyContent.Clear()
		self.textKeyContent.Enable(False)
		self.textSearch.SetFocus()


	def onClose(self, event):
		"""Close dialog."""
		self.Destroy()
