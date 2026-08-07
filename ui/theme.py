from __future__ import annotations

from contextlib import contextmanager
from types import SimpleNamespace
import unicodedata

import tkinter as tk
import ttkbootstrap as ttk

APP_THEME = "bootstrap-dark"
MAIN_WINDOW_SIZE = "650x700"
MIN_WINDOW_WIDTH = 300
MARGIN = 30
BUTTON_PADDING_X = 20
BUTTON_PADDING_Y = 2
BUTTON_SPACING = 10
BUTTON_BORDER_WIDTH = 2
PADDING_TEXT_BUTTON_X = 20
PADDING_TEXT_BUTTON_Y = 2

TITLE_FONT = ("Segoe UI", 14, "bold")
SECTION_FONT = ("Segoe UI", 10, "bold")
BODY_FONT = ("Segoe UI", 10)
SMALL_FONT = ("Segoe UI", 9)
LINK_FONT = ("Segoe UI", 14)
BUTTON_FONT = ("Segoe UI", 10)

_APP_ROOT = None
_TEMP_ROOT = None

_FALLBACK_COLORS = SimpleNamespace(
    primary="#0d6efd",
    secondary="#6c757d",
    success="#198754",
    info="#0dcaf0",
    warning="#ffc107",
    danger="#dc3545",
    light="#f8f9fa",
    dark="#212529",
    bg="#222222",
    fg="#f8f9fa",
    selectbg="#0d6efd",
    selectfg="#ffffff",
    border="#495057",
    inputfg="#f8f9fa",
    inputbg="#2b3035",
    active="#0b5ed7",
)


def set_app_root(root):
    """Register the main app root so dialogs can inherit the active theme."""
    global _APP_ROOT
    _APP_ROOT = root


def get_app_root():
    """Return the registered app root if it is still alive."""
    if _APP_ROOT is not None and getattr(_APP_ROOT, "winfo_exists", lambda: False)():
        return _APP_ROOT
    return None


def get_theme_colors(master=None):
    """Return the current ttkbootstrap colors or a safe fallback."""
    root = master or get_app_root()
    if root is not None and hasattr(root, "style"):
        return root.style.colors
    return _FALLBACK_COLORS


def configure_app_styles(root):
    """Register reusable styles for the themed screens."""
    colors = get_theme_colors(root)
    style = root.style
    style.configure("App.TFrame", background=colors.bg)
    style.configure("App.TLabel", background=colors.bg, foreground=colors.fg, font=BODY_FONT)
    style.configure("Title.TLabel", background=colors.bg, foreground=colors.fg, font=TITLE_FONT)
    style.configure("Section.TLabel", background=colors.bg, foreground=colors.fg, font=SECTION_FONT)
    style.configure("Body.TLabel", background=colors.bg, foreground=colors.fg, font=BODY_FONT)
    style.configure("Small.TLabel", background=colors.bg, foreground=colors.fg, font=SMALL_FONT)
    style.configure("Link.TLabel", background=colors.bg, foreground=colors.primary, font=LINK_FONT)
    style.configure("SmallLink.TLabel", background=colors.bg, foreground=colors.primary, font=("Segoe UI", 9, "underline"))
    style.configure("Loading.TLabel", background=colors.bg, foreground=colors.fg, font=BODY_FONT)


def create_main_window(title, icon_path=None, size=MAIN_WINDOW_SIZE, min_width=MIN_WINDOW_WIDTH):
    """Create the main ttkbootstrap window using the app theme."""
    root = ttk.Window(title=title, theme=APP_THEME)
    set_app_root(root)
    configure_app_styles(root)

    if size:
        root.geometry(size)
    if min_width is not None:
        root.minsize(min_width, 0)
    if icon_path:
        root.iconbitmap(icon_path)

    return root


@contextmanager
def dialog_parent(master=None):
    """Yield a themed parent window for dialogs, creating a temporary one if needed."""
    global _TEMP_ROOT

    parent = master or get_app_root()
    temp_root = False

    if parent is None or not getattr(parent, "winfo_exists", lambda: False)():
        parent = ttk.Window(theme=APP_THEME)
        parent.withdraw()
        configure_app_styles(parent)
        _TEMP_ROOT = parent
        temp_root = True

    try:
        yield parent
    finally:
        if temp_root and parent.winfo_exists():
            parent.destroy()
        if temp_root and _TEMP_ROOT is parent:
            _TEMP_ROOT = None


def show_info(title, message, parent=None):
    """Show an info dialog using ttkbootstrap."""
    with dialog_parent(parent) as dialog_parent_window:
        ttk.Messagebox.show_info(message, title, parent=dialog_parent_window)


def show_error(title, message, parent=None):
    """Show an error dialog using ttkbootstrap."""
    with dialog_parent(parent) as dialog_parent_window:
        ttk.Messagebox.show_error(message, title, parent=dialog_parent_window)


def ask_yes_no(title, message, parent=None):
    """Show a yes/no dialog and return True for Yes."""
    with dialog_parent(parent) as dialog_parent_window:
        answer = ttk.Messagebox.yesno(message, title, parent=dialog_parent_window)

    if isinstance(answer, bool):
        return answer

    normalized = unicodedata.normalize("NFKD", str(answer)).encode("ascii", "ignore").decode("ascii")
    return normalized.strip().lower() in {"yes", "y", "si", "s", "true", "1"}


def show_question(title, message, buttons, parent=None):
    """Show a themed question dialog with custom buttons."""
    with dialog_parent(parent) as dialog_parent_window:
        return ttk.Messagebox.show_question(
            message,
            title,
            buttons=buttons,
            parent=dialog_parent_window,
            localize=False,
        )


class VerticalChoiceDialog:
    """A themed modal dialog with vertically stacked option buttons."""

    def __init__(self, title, message, option1, option2, cancel_title, master=None):
        self.result = None
        self.master, self._temp_root = self._resolve_master(master)

        self.window = ttk.Toplevel(master=self.master, title=title)
        self.window.resizable(False, False)
        self.window.transient(self.master)
        self.window.grab_set()
        self.window.protocol("WM_DELETE_WINDOW", self._cancel)
        self.window.bind("<Escape>", lambda event: self._cancel())

        frame = ttk.Frame(self.window, style="App.TFrame", padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(
            frame,
            text=message,
            style="Body.TLabel",
            justify="left",
            anchor="w",
            wraplength=520,
        ).pack(fill="x", anchor="w", pady=(0, 16))

        buttons_frame = ttk.Frame(frame, style="App.TFrame")
        buttons_frame.pack(fill="x")

        self.option1_button = ttk.Button(
            buttons_frame,
            text=option1,
            bootstyle="primary",
            command=self._choose_option1,
            padding=(14, 8),
        )
        self.option1_button.pack(fill="x", pady=(0, 10))

        self.option2_button = ttk.Button(
            buttons_frame,
            text=option2,
            bootstyle="success",
            command=self._choose_option2,
            padding=(14, 8),
        )
        self.option2_button.pack(fill="x")

        footer = ttk.Frame(frame, style="App.TFrame")
        footer.pack(fill="x", pady=(16, 0))

        cancel_button = ttk.Button(
            footer,
            text=cancel_title,
            bootstyle="secondary",
            command=self._cancel,
            padding=(14, 6),
        )
        cancel_button.pack(side="right")

        self.window.update_idletasks()
        self.window.place_window_center()
        self.option1_button.focus_set()

    @staticmethod
    def _resolve_master(master=None):
        root = master or get_app_root()
        temp_root = None

        if root is None or not getattr(root, "winfo_exists", lambda: False)():
            root = ttk.Window(theme=APP_THEME)
            root.withdraw()
            configure_app_styles(root)
            temp_root = root

        return root, temp_root

    def _choose_option1(self):
        self.result = 1
        self._close()

    def _choose_option2(self):
        self.result = 2
        self._close()

    def _cancel(self):
        self.result = None
        self._close()

    def _close(self):
        if self.window.winfo_exists():
            try:
                self.window.grab_release()
            except Exception:
                pass
            self.window.destroy()
        if self._temp_root is not None and self._temp_root.winfo_exists():
            self._temp_root.destroy()

    def show(self):
        self.window.wait_window()
        return self.result


def choose_from_options(title, option1, option2, cancel_title="Cancel", parent=None):
    """Show a two-option themed question dialog and return 1, 2, or None."""
    dialog = VerticalChoiceDialog(
        title=title,
        message=title,
        option1=option1,
        option2=option2,
        cancel_title=cancel_title,
        master=parent,
    )
    return dialog.show()


class FileProgressDialog:
    """A themed modal progress dialog for file-by-file operations."""

    def __init__(self, total, title="Processing files", master=None):
        self.total = max(int(total), 1)
        self.current = 0
        self.master, self._temp_root = self._resolve_master(master)

        self.window = ttk.Toplevel(master=self.master, title=title)
        self.window.resizable(False, False)
        self.window.transient(self.master)
        self.window.grab_set()
        self.window.protocol("WM_DELETE_WINDOW", lambda: None)

        frame = ttk.Frame(self.window, style="App.TFrame", padding=20)
        frame.pack(fill="both", expand=True)

        self.label = ttk.Label(
            frame,
            text=self._format_message(0),
            style="Body.TLabel",
            justify="left",
            anchor="w",
            wraplength=360,
        )
        self.label.pack(fill="x", pady=(0, 12))

        self.progress = ttk.Progressbar(
            frame,
            mode="determinate",
            maximum=self.total,
            value=0,
            bootstyle="info",
        )
        self.progress.pack(fill="x")

        self.window.update_idletasks()
        self.window.place_window_center()
        self.window.lift()

    @staticmethod
    def _resolve_master(master=None):
        root = master or get_app_root()
        temp_root = None

        if root is None or not getattr(root, "winfo_exists", lambda: False)():
            root = ttk.Window(theme=APP_THEME)
            root.withdraw()
            configure_app_styles(root)
            temp_root = root

        return root, temp_root

    def _format_message(self, current):
        return f"Processing file {current} of {self.total} files"

    def update(self, current):
        self.current = max(0, min(int(current), self.total))
        self.progress.configure(value=self.current)
        self.label.configure(text=self._format_message(self.current))
        self.window.update_idletasks()

    def close(self):
        if self.window.winfo_exists():
            try:
                self.window.grab_release()
            except Exception:
                pass
            self.window.destroy()
        if self._temp_root is not None and self._temp_root.winfo_exists():
            self._temp_root.destroy()
