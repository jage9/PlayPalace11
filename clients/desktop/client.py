"""
Play Palace v11 Client

A wxPython-based client for Play Palace with websocket support.
Features:
- Menu list with multiletter navigation (toggle-able)
- Chat input
- History display
- Alt+M shortcut to focus menu
"""

import wx
from ui import MainWindow
from ui.login_dialog import LoginDialog


def main():
    """Main entry point for the Play Palace v9 client."""
    app = wx.App(False)

    # Show login dialog
    login_dialog = LoginDialog()
    if login_dialog.ShowModal() == wx.ID_OK:
        credentials = login_dialog.get_credentials()
        login_dialog.Destroy()

        # Create main window with credentials
        frame = MainWindow(credentials)
        frame.Show()
        app.MainLoop()
    else:
        # User cancelled login
        login_dialog.Destroy()


if __name__ == "__main__":
    main()
