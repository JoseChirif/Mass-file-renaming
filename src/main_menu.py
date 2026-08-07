from __future__ import annotations

import sys
import webbrowser
import tkinter as tk

import ttkbootstrap as ttk
from PIL import Image, ImageTk

from config.config import icon_picture_png, icon_picture_ico, logo_github_png, __version__
from functions.functions import (
    adjust_text,
    execute_script0,
    execute_script1,
    execute_script2,
    get_instructions,
    load_available_languages,
    load_translations,
)
from ui.theme import create_main_window


CURRENT_VERSION = f"v{__version__}"
DEFAULT_LANGUAGE = "en"
REPOSITORY_URL = "https://github.com/JoseChirif/Mass-file-renaming-with-excel"


language = DEFAULT_LANGUAGE
languages_by_label = dict(sorted(load_available_languages().items(), key=lambda item: item[1]))
languages_by_name = {value: key for key, value in languages_by_label.items()}
translations = load_translations(language)


window = None
language_var = None
combo_languages = None
lbl_project_title = None
lbl_language = None
lbl_menu = None
btn_option_1 = None
btn_option_2 = None
btn_option_3 = None
lbl_notes_title = None
lbl_notes_content = None
lbl_instructions = None
lbl_version = None
github_button = None

app_logo_image = None
github_logo_image = None


def _load_image(path, size):
    """Load and resize an image for ttk widgets."""
    image = Image.open(path)
    image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)


def _open_repository():
    """Open the project repository in the default browser."""
    webbrowser.open_new_tab(REPOSITORY_URL)


def _refresh_texts():
    """Refresh all visible texts after a language change."""
    global translations

    translations = load_translations(language)

    project_title = translations["project_title"]
    language_text = translations["language_text"]
    select_an_option_text = translations["select_an_option_text"]
    text_button_1 = translations["text_button_1"]
    text_button_2 = translations["text_button_2"]
    text_button_3 = translations["text_button_3"]
    notes_title = translations["notes_title"]
    notes_content = translations["notes_content"]
    instructions_text = translations["instructions_text"]

    window.title(project_title)
    lbl_project_title.config(text=project_title)
    lbl_language.config(text=language_text)
    lbl_menu.config(text=select_an_option_text)
    btn_option_1.config(text=text_button_1)
    btn_option_2.config(text=text_button_2)
    btn_option_3.config(text=text_button_3)
    lbl_notes_title.config(text=notes_title)
    lbl_notes_content.config(text=notes_content)
    lbl_instructions.config(text=instructions_text)

    if language in languages_by_name:
        language_var.set(languages_by_name[language])


def select_language(event=None):
    """Handle a language selection from the combobox."""
    global language

    selected_label = combo_languages.get()
    language = languages_by_name.get(selected_label, DEFAULT_LANGUAGE)
    _refresh_texts()


def _open_instructions():
    """Open the instructions page for the current language."""
    get_instructions(language)


def _close_app():
    """Close the application cleanly."""
    if window is not None and window.winfo_exists():
        window.destroy()
    sys.exit(0)


def main_menu():
    """Build and show the main application menu."""
    global window, language_var, combo_languages
    global lbl_project_title, lbl_language, lbl_menu
    global btn_option_1, btn_option_2, btn_option_3
    global lbl_notes_title, lbl_notes_content, lbl_instructions, lbl_version
    global github_button, app_logo_image, github_logo_image

    initial_translations = load_translations(language)
    project_title = initial_translations["project_title"]
    language_text = initial_translations["language_text"]
    select_an_option_text = initial_translations["select_an_option_text"]
    text_button_1 = initial_translations["text_button_1"]
    text_button_2 = initial_translations["text_button_2"]
    text_button_3 = initial_translations["text_button_3"]
    notes_title = initial_translations["notes_title"]
    notes_content = initial_translations["notes_content"]
    instructions_text = initial_translations["instructions_text"]

    window = create_main_window(project_title, icon_picture_ico, size="650x700", min_width=300)
    window.protocol("WM_DELETE_WINDOW", _close_app)
    window.resizable(True, True)

    app_logo_image = _load_image(icon_picture_png, (50, 50))
    github_logo_image = _load_image(logo_github_png, (20, 20))

    main_frame = ttk.Frame(window, style="App.TFrame", padding=(30, 24, 30, 16))
    main_frame.pack(fill="both", expand=True)

    body_frame = ttk.Frame(main_frame, style="App.TFrame")
    body_frame.pack(side="top", fill="x")

    footer_frame = ttk.Frame(main_frame, style="App.TFrame")
    footer_frame.pack(side="bottom", fill="x", pady=(18, 0))

    header_frame = ttk.Frame(body_frame, style="App.TFrame")
    header_frame.pack(fill="x")

    brand_frame = ttk.Frame(header_frame, style="App.TFrame")
    brand_frame.pack(side="left", fill="x", expand=True)

    lbl_logo = ttk.Label(brand_frame, image=app_logo_image, style="App.TLabel")
    lbl_logo.image = app_logo_image
    lbl_logo.pack(side="left", padx=(0, 12))

    lbl_project_title = ttk.Label(
        brand_frame,
        text=project_title,
        style="Title.TLabel",
        wraplength=430,
        justify="left",
        anchor="w",
    )
    lbl_project_title.pack(side="left", fill="x", expand=True)

    github_button = ttk.Button(
        header_frame,
        text="GitHub",
        image=github_logo_image,
        compound="left",
        command=_open_repository,
        bootstyle="light",
        cursor="hand2",
        padding=(10, 6),
    )
    github_button.image = github_logo_image
    github_button.pack(side="right")

    ttk.Separator(body_frame, orient="horizontal").pack(fill="x", pady=(18, 18))

    language_frame = ttk.Frame(body_frame, style="App.TFrame")
    language_frame.pack(fill="x", pady=(0, 16))
    language_frame.columnconfigure(0, weight=1)

    lbl_language = ttk.Label(language_frame, text=language_text, style="Section.TLabel")
    lbl_language.grid(row=0, column=0, sticky="e", padx=(0, 10))

    language_var = tk.StringVar(value=languages_by_label.get(language, next(iter(languages_by_label.values()))))
    combo_languages = ttk.Combobox(
        language_frame,
        textvariable=language_var,
        values=list(languages_by_label.values()),
        state="readonly",
        width=24,
        bootstyle="secondary",
    )
    combo_languages.grid(row=0, column=1, sticky="e")
    combo_languages.bind("<<ComboboxSelected>>", select_language)

    lbl_menu = ttk.Label(
        body_frame,
        text=select_an_option_text,
        style="Section.TLabel",
        wraplength=560,
        justify="left",
        anchor="w",
    )
    lbl_menu.pack(fill="x", pady=(4, 12))

    options_frame = ttk.Frame(body_frame, style="App.TFrame")
    options_frame.pack(fill="x")

    btn_option_1 = ttk.Button(
        options_frame,
        text=text_button_1,
        command=lambda: execute_script0(language),
        bootstyle="primary",
        padding=(20, 12),
    )
    btn_option_1.pack(fill="x", pady=(0, 10))

    btn_option_2 = ttk.Button(
        options_frame,
        text=text_button_2,
        command=lambda: execute_script1(language),
        bootstyle="success",
        padding=(20, 12),
    )
    btn_option_2.pack(fill="x", pady=(0, 10))

    btn_option_3 = ttk.Button(
        options_frame,
        text=text_button_3,
        command=lambda: execute_script2(language),
        bootstyle="warning",
        padding=(20, 12),
    )
    btn_option_3.pack(fill="x")

    notes_frame = ttk.Frame(body_frame, style="App.TFrame")
    notes_frame.pack(fill="x", pady=(18, 0))

    lbl_notes_title = ttk.Label(
        notes_frame,
        text=notes_title,
        style="Section.TLabel",
        wraplength=560,
        justify="left",
        anchor="w",
    )
    lbl_notes_title.pack(fill="x", anchor="w", pady=(0, 4))

    lbl_notes_content = ttk.Label(
        notes_frame,
        text=notes_content,
        style="Body.TLabel",
        wraplength=560,
        justify="left",
        anchor="w",
    )
    lbl_notes_content.pack(fill="x", anchor="w")

    lbl_instructions = ttk.Label(
        footer_frame,
        text=instructions_text,
        style="SmallLink.TLabel",
        cursor="hand2",
    )
    lbl_instructions.pack(side="left")
    lbl_instructions.bind("<Button-1>", lambda event: _open_instructions())

    lbl_version = ttk.Label(footer_frame, text=CURRENT_VERSION, style="Small.TLabel")
    lbl_version.pack(side="right")

    window.bind(
        "<Configure>",
        lambda event: adjust_text(
            event,
            lbl_project_title,
            lbl_menu,
            lbl_notes_title,
            lbl_notes_content,
            margin=20,
        ),
    )

    window.mainloop()


if __name__ == "__main__":
    main_menu()
