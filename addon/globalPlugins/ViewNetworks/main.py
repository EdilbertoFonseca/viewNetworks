# -*- coding: UTF-8 -*-

"""
Author: Edilberto Fonseca <edilberto.fonseca@outlook.com>
Copyright: (C) 2025
License: GPL v2
"""

import subprocess

import addonHandler
import queueHandler
import ui
import wx

addonHandler.initTranslation()

ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]

# Encodings mais comuns no Windows PT/EN
AVAILABLE_ENCODINGS = [
	"cp850",
	"cp1252",
	"latin1",
	"utf-8",
]


class ViewNetworks(wx.Dialog):
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super().__new__(cls)
		else:
			queueHandler.queueFunction(
				queueHandler.eventQueue,
				ui.message,
				_("O diálogo {} já está aberto.").format(ADDON_SUMMARY),
			)
		return cls._instance

	def __init__(self, parent, title):
		if hasattr(self, "initialized"):
			return
		self.initialized = True

		super().__init__(parent, title=title, size=(600, 500))

		panel = wx.Panel(self)
		mainSizer = wx.BoxSizer(wx.VERTICAL)

		# === Encoding ===
		encodingSizer = wx.BoxSizer(wx.HORIZONTAL)
		encodingLabel = wx.StaticText(panel, label=_("Codificação:"))
		self.encodingChoice = wx.Choice(panel, choices=AVAILABLE_ENCODINGS)
		self.encodingChoice.SetSelection(0)

		encodingSizer.Add(encodingLabel, 0, wx.ALL | wx.CENTER, 5)
		encodingSizer.Add(self.encodingChoice, 0, wx.ALL | wx.CENTER, 5)

		# === Campo de saída ===
		self.outputCtrl = wx.TextCtrl(
			panel,
			style=wx.TE_MULTILINE | wx.TE_READONLY,
		)

		# === Botões ===
		buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

		self.btnList = wx.Button(panel, label=_("&Listar redes salvas"))
		self.btnDetails = wx.Button(panel, label=_("&Mostrar detalhes da rede"))
		self.btnClose = wx.Button(panel, wx.ID_CANCEL, label=_("&Fechar"))

		buttonSizer.Add(self.btnList, 0, wx.ALL, 5)
		buttonSizer.Add(self.btnDetails, 0, wx.ALL, 5)
		buttonSizer.Add(self.btnClose, 0, wx.ALL, 5)

		# === Bindings ===
		self.btnList.Bind(wx.EVT_BUTTON, self.onListNetworks)
		self.btnDetails.Bind(wx.EVT_BUTTON, self.onShowDetails)
		self.Bind(wx.EVT_BUTTON, self.onClose, id=wx.ID_CANCEL)

		# === Layout ===
		mainSizer.Add(encodingSizer, 0, wx.EXPAND)
		mainSizer.Add(self.outputCtrl, 1, wx.ALL | wx.EXPAND, 5)
		mainSizer.Add(buttonSizer, 0, wx.CENTER)

		panel.SetSizer(mainSizer)
		self.Centre()

	# ======================================================
	# Utilitário central para executar netsh
	# ======================================================
	def run_netsh(self, args):
		encoding = self.encodingChoice.GetStringSelection()

		try:
			output = subprocess.check_output(
				args,
				stderr=subprocess.STDOUT,
				encoding=encoding,
				errors="replace",
				shell=False,
			)
			return output
		except subprocess.CalledProcessError as e:
			return e.output or str(e)
		except FileNotFoundError:
			return _("O comando netsh não foi encontrado no sistema.")

	# ======================================================
	# Detecção de ausência de Wi-Fi
	# ======================================================
	def has_wifi_support(self):
		output = self.run_netsh(["netsh", "wlan", "show", "interfaces"])

		indicators = [
			"Não há nenhuma interface",
			"There is no wireless",
			"WLAN AutoConfig",
			"não está em execução",
			"is not running",
		]

		for text in indicators:
			if text.lower() in output.lower():
				return False, output

		return True, output

	# ======================================================
	# Ações
	# ======================================================
	def onListNetworks(self, event):
		self.outputCtrl.Clear()

		has_wifi, diagnostic = self.has_wifi_support()
		if not has_wifi:
			self.outputCtrl.SetValue(
				_("Nenhuma interface Wi-Fi foi detectada neste sistema.\n\n") + diagnostic,
			)
			return

		output = self.run_netsh(["netsh", "wlan", "show", "profile"])
		self.outputCtrl.SetValue(output)

	def onShowDetails(self, event):
		dlg = wx.TextEntryDialog(
			self,
			_("Informe o nome da rede Wi-Fi:"),
			_("Detalhes da rede"),
		)

		if dlg.ShowModal() != wx.ID_OK:
			dlg.Destroy()
			return

		profile = dlg.GetValue().strip()
		dlg.Destroy()

		if not profile:
			ui.message(_("Nome da rede não informado."))
			return

		self.outputCtrl.Clear()

		has_wifi, diagnostic = self.has_wifi_support()
		if not has_wifi:
			self.outputCtrl.SetValue(
				_("Nenhuma interface Wi-Fi foi detectada neste sistema.\n\n") + diagnostic,
			)
			return

		output = self.run_netsh(
			["netsh", "wlan", "show", "profile", f"name={profile}", "key=clear"],
		)
		self.outputCtrl.SetValue(output)

	def onClose(self, event):
		self.Destroy()
