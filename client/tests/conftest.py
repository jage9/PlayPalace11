import pytest
import wx


@pytest.fixture(scope="session")
def wx_app():
    """Ensure a wx App exists for dialog tests."""
    if not wx.App.IsDisplayAvailable():
        pytest.skip("GUI display is not available for wx dialogs")
    app = wx.App(False)
    yield app
    app.Destroy()
