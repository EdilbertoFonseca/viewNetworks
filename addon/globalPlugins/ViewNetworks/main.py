# -*- coding: UTF-8 -*-

"""
Author: Edilberto Fonseca <edilberto.fonseca@outlook.com>
Copyright: (C) 2025 Edilberto Fonseca

This file is covered by the GNU General Public License.
See the file COPYING for more details or visit:
https://www.gnu.org/licenses/gpl-2.0.html

Created on: 07/08/2022
Refactored on: 2026
"""

import subprocess

import addonHandler
import queueHandler
import ui
import wx
from logHandler import log

# Get add-on summary for use in UI messages
ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]

# Initialize translation support
addonHandler.initTranslation()

ENCODING_CHOICES = ('cp850', 'cp1252', 'latin-1', 'utf-8', 'cp437')

NETSH_LIST_CMD = ['netsh', 'wlan', 'show', 'profile']


def run_netsh(command, encoding):
	"""
	Executes a netsh command using the selected encoding,
	with safe fallback in case of decoding issues.
	"""
	try:
		log.debug(f"Running netsh with encoding: {encoding}")
		return subprocess.check_output(
			command,
			encoding=encoding,
			errors='strict',
			shell=False
		)
	except UnicodeDecodeError:
		log.warning(f"Unicode error with {encoding}, falling back to latin-1.")
		return subprocess.check_output(
			command,
			encoding='latin-1',
			errors='replace',
			shell=False
		)


class ViewNetworks(wx.Dialog):
	"""Unified dialog for listing Wi-Fi networks and showing profile details."""
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(ViewNetworks, cls).__new__(cls)
		else:
			msg = _("An instance of {} is already open.").format(ADDON_SUMMARY)
			queueHandler.queueFunction(queueHandler.eventQueue, ui.message, msg)
		return cls._instance

	def __init__(self, parent, title):
		if getattr(self, "_initialized", False):
			return
		self._initialized = True

		super().__init__(parent, title=title)
		self.SetMinSize((600, 500))
		self.CentreOnScreen()

		panel = wx.Panel(self)

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		topSizer = wx.BoxSizer(wx.HORIZONTAL)
		buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
		outputSizer = wx.BoxSizer(wx.VERTICAL)
		bottomSizer = wx.BoxSizer(wx.HORIZONTAL)

		# Network name
		labelNetwork = wx.StaticText(panel, label=_("Network name:"))
		topSizer.Add(labelNetwork, 0, wx.ALL | wx.CENTER, 5)

		self.textNetwork = wx.TextCtrl(panel)
		topSizer.Add(self.textNetwork, 1, wx.ALL | wx.EXPAND, 5)

		# Encoding selection
		labelEncoding = wx.StaticText(panel, label=_("Encoding:"))
		topSizer.Add(labelEncoding, 0, wx.ALL | wx.CENTER, 5)

		self.choiceEncoding = wx.Choice(panel, choices=ENCODING_CHOICES)
		self.choiceEncoding.SetSelection(0)  # cp850 default
		topSizer.Add(self.choiceEncoding, 0, wx.ALL | wx.CENTER, 5)

		# Action buttons
		self.buttonList = wx.Button(panel, label=_("&List saved networks"))
		self.buttonDetails = wx.Button(panel, label=_("Show &network details"))

		self.Bind(wx.EVT_BUTTON, self.onListNetworks, self.buttonList)
		self.Bind(wx.EVT_BUTTON, self.onShowDetails, self.buttonDetails)

		buttonSizer.Add(self.buttonList, 0, wx.ALL | wx.CENTER, 5)
		buttonSizer.Add(self.buttonDetails, 0, wx.ALL | wx.CENTER, 5)

		# Output text
		self.textOutput = wx.TextCtrl(
			panel,
			style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2
		)
		outputSizer.Add(self.textOutput, 1, wx.ALL | wx.EXPAND, 5)

		# Bottom buttons
		self.buttonCopy = wx.Button(panel, label=_("&Copy"))
		self.buttonClose = wx.Button(panel, wx.ID_CANCEL, label=_("&Close"))

		self.Bind(wx.EVT_BUTTON, self.onCopy, self.buttonCopy)
		self.Bind(wx.EVT_BUTTON, self.onClose, self.buttonClose)

		bottomSizer.Add(self.buttonCopy, 0, wx.ALL | wx.CENTER, 5)
		bottomSizer.Add(self.buttonClose, 0, wx.ALL | wx.CENTER, 5)

		# Layout
		mainSizer.Add(topSizer, 0, wx.EXPAND)
		mainSizer.Add(buttonSizer, 0, wx.CENTER)
		mainSizer.Add(outputSizer, 1, wx.EXPAND)
		mainSizer.Add(bottomSizer, 0, wx.CENTER)

		panel.SetSizer(mainSizer)

		self.textOutput.SetFocus()

	# Actions
	def getSelectedEncoding(self):
		return self.choiceEncoding.GetStringSelection() or 'cp850'

	def displayOutput(self, text, announce=None):
		self.textOutput.SetValue(text)
		self.textOutput.SetFocus()
		if announce:
			ui.message(announce)

	def onListNetworks(self, event):
		encoding = self.getSelectedEncoding()
		ui.message(_("Listing saved Wi-Fi networks."))
		log.info("Listing Wi-Fi profiles")

		try:
			output = run_netsh(NETSH_LIST_CMD, encoding)
			self.displayOutput(output, _("Saved Wi-Fi networks loaded."))
		except Exception as e:
			log.error(f"Error listing networks: {e}")
			self.displayOutput(
				_("Error listing networks:\n{}").format(e),
				_("Error listing networks.")
			)

	def onShowDetails(self, event):
		network = self.textNetwork.GetValue().strip()
		if not network:
			ui.message(_("Please enter a network name."))
			self.textNetwork.SetFocus()
			return

		encoding = self.getSelectedEncoding()
		ui.message(_("Showing details for network {}.").format(network))
		log.info(f"Showing details for network: {network}")

		command = [
			'netsh', 'wlan', 'show', 'profile',
			f'name="{network}"', 'key=clear'
		]

		try:
			output = run_netsh(command, encoding)
			self.displayOutput(
				output,
				_("Network details loaded.")
			)
		except Exception as e:
			log.error(f"Error retrieving network {network}: {e}")
			self.displayOutput(
				_("Error retrieving network details:\n{}").format(e),
				_("Error retrieving network details.")
			)

	def onCopy(self, event):
		content = self.textOutput.GetValue()
		if not content:
			ui.message(_("There is no content to copy."))
			return

		if wx.TheClipboard.Open():
			wx.TheClipboard.SetData(wx.TextDataObject(content))
			wx.TheClipboard.Close()
			ui.message(_("Content copied to clipboard."))

	def onClose(self, event):
		ViewNetworks._instance = None
		self.Destroy()
