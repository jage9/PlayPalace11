"""Dialog for trusting self-signed TLS certificates."""

from dataclasses import dataclass
from typing import Sequence

import wx


@dataclass
class CertificateInfo:
    """Structured information about a presented certificate."""

    host: str
    common_name: str
    sans: Sequence[str]
    issuer: str
    valid_from: str
    valid_to: str
    fingerprint: str  # Display-friendly fingerprint
    fingerprint_hex: str  # Raw hex without delimiters
    pem: str
    matches_host: bool


class CertificatePromptDialog(wx.Dialog):
    """Modal dialog prompting the user to trust an unverified certificate."""

    def __init__(self, parent, info: CertificateInfo):
        super().__init__(parent, title="Untrusted Certificate", size=(500, 420))
        self.info = info
        self._create_ui()
        self.CenterOnParent()

    def _create_ui(self):
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        intro = wx.StaticText(
            panel,
            label="The server presented a certificate that could not be verified.",
        )
        intro.Wrap(460)
        sizer.Add(intro, 0, wx.ALL | wx.EXPAND, 12)

        warning_text = (
            "Hostname matches certificate." if self.info.matches_host
            else f"Hostname mismatch: expected {self.info.host}."
        )
        warning = wx.StaticText(panel, label=warning_text)
        if not self.info.matches_host:
            warning.SetForegroundColour(wx.Colour(200, 50, 50))
        sizer.Add(warning, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 12)

        grid = wx.FlexGridSizer(0, 2, 4, 8)
        grid.AddGrowableCol(1, 1)

        def add_row(label, value):
            lbl = wx.StaticText(panel, label=label)
            lbl.SetFont(lbl.GetFont().Bold())
            grid.Add(lbl, 0, wx.ALIGN_TOP)
            text = wx.StaticText(panel, label=value)
            text.Wrap(360)
            grid.Add(text, 0, wx.ALIGN_TOP | wx.EXPAND)

        add_row("Server host:", self.info.host or "(unknown)")
        add_row("Common name:", self.info.common_name or "(none)")
        sans = ", ".join(self.info.sans) if self.info.sans else "(none)"
        add_row("Subject Alt Names:", sans)
        add_row("Issuer:", self.info.issuer or "(unknown)")
        add_row("Valid from:", self.info.valid_from or "(unknown)")
        add_row("Valid to:", self.info.valid_to or "(unknown)")
        add_row("Fingerprint (SHA-256):", self.info.fingerprint)

        sizer.Add(grid, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 12)

        info_text = wx.StaticText(
            panel,
            label="If you trust this certificate, PlayPalace will remember it and only reconnect if the fingerprint matches in the future.",
        )
        info_text.Wrap(460)
        sizer.Add(info_text, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 12)

        button_sizer = wx.StdDialogButtonSizer()
        trust_btn = wx.Button(panel, wx.ID_OK, "Trust Certificate")
        trust_btn.SetDefault()
        cancel_btn = wx.Button(panel, wx.ID_CANCEL)
        button_sizer.AddButton(trust_btn)
        button_sizer.AddButton(cancel_btn)
        button_sizer.Realize()

        sizer.Add(button_sizer, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 10)

        panel.SetSizer(sizer)
