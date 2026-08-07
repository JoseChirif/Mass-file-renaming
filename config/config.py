# Import functions
from functions.functions import relative_route_to_file, get_filename_or_directory,  load_available_languages, load_translations, delete_extention

# Version
__version__ = '2.0.0'

# Common routes and variables
# icon_picture_ico
icon_picture_ico = relative_route_to_file("assets", "icon.ico")

# icon_picture_png
icon_picture_png = relative_route_to_file("assets", "icon.png")
  
# logo_github
logo_github_png = relative_route_to_file("assets", "icon_github.png")


# Common names in excel
project_name  = get_filename_or_directory()
excel_name = delete_extention(project_name) + '.xlsx' # this function doesn't consider the file extention


# Files to be ignored in df
files_to_avoid = [
    "_internal",
    excel_name,
    project_name # Gets the name of the current file
]    
# Add renamed folder in each language
# Get language dictionary from languages.json file
languages = load_available_languages()
# Iterate over each language in the language dictionary
for language in languages:
    # Load the translations of the current language
    tanslations = load_translations(language)
    # Add folder_with_renamed_files to the list
    if 'renamed' in tanslations:
        renamed = tanslations['renamed']
        folder_with_renamed_files = project_name + " - " + renamed
        files_to_avoid.append(folder_with_renamed_files)
        



