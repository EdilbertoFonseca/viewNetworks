# -*- coding: UTF-8 -*-

# Description: Dialog to recover the password.
# Author: Edilberto Fonseca.
# Email: edilberto.fonseca@outlook.com.
# Date of creation: 07/08/2022.

# Standard Python imports.
import subprocess

import addonHandler
import wx
from gui import messageBox

# For translation process
addonHandler.initTranslation()


class ViewPassword(wx.Dialog):

	def __init__(self, parent, title):
		self.title = title
		super(ViewPassword, self).__init__(parent, title=title)
		panel = wx.Panel(self)
		boxSizer = wx.BoxSizer(wx.VERTICAL)
		searchSizer = wx.BoxSizer(wx.HORIZONTAL)
		buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

		labelSearch = wx.StaticText(panel, label=_('Enter the network name: '))
		searchSizer.Add(labelSearch, 0, wx.ALL | wx.EXPAND, 5)

		self.textSearch = wx.TextCtrl(panel, -1)
		searchSizer.Add(self.textSearch, 1, wx.ALL | wx.EXPAND, 5)

		labelContent = wx.StaticText(panel, label=_('Key content: '))
		searchSizer.Add(labelContent, 0, wx.ALL | wx.EXPAND, 5)

		self.textKeyContent = wx.TextCtrl(panel, -1, style=wx.TE_READONLY)
		searchSizer.Add(self.textKeyContent, 1, wx.ALL | wx.EXPAND, 5)

		buttonSearch = wx.Button(panel, -1, label=_('&Search'))
		self.Bind(wx.EVT_BUTTON, self.onSearch, buttonSearch)
		buttonSizer.Add(buttonSearch, 0, wx.ALL | wx.EXPAND, 5)

		buttonClean = wx.Button(panel, -1, label=_('C&lean'))
		self.Bind(wx.EVT_BUTTON, self.onClean, buttonClean)
		buttonSizer.Add(buttonClean, 0, wx.ALL | wx.EXPAND, 5)

		buttonClose = wx.Button(panel, wx.ID_CANCEL, label=_('&Close'))
		self.Bind(wx.EVT_BUTTON, self.onClose, id=wx.ID_CANCEL)
		buttonSizer.Add(buttonClose, 0, wx.ALL | wx.EXPAND, 5)

		boxSizer.Add(searchSizer, 1, wx.ALL | wx.EXPAND, 5)
		boxSizer.Add(buttonSizer, 0, wx.ALL | wx.CENTER, 5)
		panel.SetSizer(boxSizer)

	def onSearch(self, event):
		"""Search for a certain network, and try to recover your password."""
		nameWiFi = self.textSearch.GetValue()

		try:
			command = ['netsh', 'wlan', 'show', 'profile', nameWiFi, 'key=clear']
			information = subprocess.check_output(command, encoding='cp850')
			for line in information.split('\n'):
				if "Key Content" in line or "Conteúdo da Chave" in line:
					# getting the password
					pos = line.find(':')
					password = line[pos + 2:].strip()
					self.textKeyContent.Enable(True)
					self.textKeyContent.SetValue(password)
					self.textKeyContent.SetFocus()
					break
			else:
				self.show_message(_(f'Could not find key content for network {nameWiFi}!'), _('Attention'))
		except subprocess.CalledProcessError as e:
			self.show_message(_(f'Error retrieving network information for {nameWiFi}: {str(e)}'), _('Attention'))
			self.textSearch.Clear()
			self.textSearch.SetFocus()
		except FileNotFoundError:
			self.show_message(
				_('netsh command not found. Ensure you are running on a supported Windows environment.'),
				_('Error'))
			self.textSearch.Clear()
			self.textSearch.SetFocus()
		except Exception as e:
			self.show_message(_(f'An unexpected error occurred: {str(e)}'), _('Error'))
			self.textSearch.Clear()
			self.textSearch.SetFocus()

	def onClean(self, event):
		"""Clear the fields for a future search."""
		self.textSearch.Clear()
		self.textKeyContent.Clear()
		self.textKeyContent.Enable(False)
		self.textSearch.SetFocus()

	def show_message(self, message, caption=_("Message"), style=wx.OK | wx.ICON_INFORMATION):
		"""
		Formats and displays messages to the user.
		Args:
			message (str): Message to be displayed.
			caption (str, optional): Window title. The default is _("Message").
			style (int, optional): Message box style, combining flags like wx.OK, wx.CANCEL, wx.ICON_INFORMATION, etc.
			The default is wx.OK | wx.ICON_INFORMATION.
		"""
		messageBox(message, caption, style)

	def onClose(self, event):
		"""Close dialog."""
		self.Destroy()
