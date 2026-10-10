"""oi-browser: AI-friendly browser automation via CDP."""

from oi_browser.install import (
    InstallEvent,
    chromium_executable,
    ensure_chromium,
    install_chromium_stream,
)
from oi_browser.mode import BrowserMode
from oi_browser.models import ActionMetrics, TabInfo, ToolResult
from oi_browser.session import BrowserSession
from oi_browser.settings import OiSettings, settings
from oi_browser.tool_interface import browser_tool

__all__ = [
    "BrowserSession",
    "browser_tool",
    "BrowserMode",
    "OiSettings",
    "settings",
    "ToolResult",
    "ActionMetrics",
    "TabInfo",
    "InstallEvent",
    "chromium_executable",
    "ensure_chromium",
    "install_chromium_stream",
]
