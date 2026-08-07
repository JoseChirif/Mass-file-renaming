# Import libraries
import os
import pandas as pd

# go to the parent directory if you are running this script directly (uncomment the following lines)
# import sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import functions
from functions.functions import choose_language, exit_if_directly_executed, working_directory, ask_replace, show_message, show_error, modify_excel_dataframe, load_translations

# Import parameters from config
from config.config import project_name, excel_name, files_to_avoid

    
    
## VARIABLES
# Get language
language = choose_language()

# Declare the main function to transmit the language parameter when executing it in other scripts.
def main(language):
    """
    Creates an Excel file with the names of files in the current directory (if running from an executable) or in the parent project directory (if running directly from run.py). The function takes the provided language parameter to handle the language-specific functionality.
    
    This function is located in src/a_Create_excel.py

    Arg:
        language (str): The language code (e.g., 'en', 'es') passed to customize language-specific content during Excel creation.

    Returns:
        None: This function does not return any value. It generates an Excel file with the file names from the directory.
    """
    # load translations (part 1)
    translations = load_translations(language)
    # Declare locale texts
    renamed = translations["renamed"]

    # Get destination folder
    folder_with_renamed_files = project_name + " - " + renamed
    


    # load translations (part 2 - final)
    # variables for excel
    excel_column_original_name = translations["excel_column_original_name"]
    excel_column_extention = translations["excel_column_extention"]
    excel_column_new_name = translations["excel_column_new_name"]
    notes_title = translations["notes_title"]
    excel_note1 = translations["excel_note1"].format(excel_column_new_name=excel_column_new_name)
    excel_note2 = translations["excel_note2"].format(excel_column_new_name=excel_column_new_name)
    excel_note3 = translations["excel_note3"]
    excel_note4 = translations["excel_note4"].format(project_name=project_name, folder_with_renamed_files=folder_with_renamed_files)
    excel_note5 = translations["excel_note5"]
    # Tkinter messages
    file_created_title = translations["file_created_title"]
    file_created_message = translations["file_created_message"].format(excel_name = excel_name)
    file_not_created_selected_title = translations["file_not_created_selected_title"]
    file_not_created_selected_message = translations["file_not_created_selected_message"]
    file_replaced_title = translations["file_replaced_title"]
    file_replaced_message = translations["file_replaced_message"].format(excel_name = excel_name)
    error_open_file = translations["error_open_file"].format(excel_name = excel_name)
    file_already_exist_title = translations['file_already_exist_title']
    file_already_exist_message = translations['file_already_exist_message'].format(excel_name = excel_name)
    error_text = translations['error_text']




    # Declare variables unique to this script
    excel_aditional_rows_to_unlock = 100



## EXECUTE
    # Ensure that the Excel is created in the corresponding folder
    excel_save_route = os.path.join(working_directory(), excel_name)


    ## DATAFRAME
    # Create a empty list to add data
    data = []

    # Iterate the files in the current directory
    for file in os.listdir(working_directory()):
        file_route = os.path.join(working_directory(), file)
        
        # If the file is not in "files_to_avoid" list
        if file not in files_to_avoid:
            if os.path.isfile(file_route):
                # Separate name and extension
                name, extention = os.path.splitext(file)
                # Add data to the list (with extension)
                data.append([name, extention, ""]) # new name empty
            elif os.path.isdir(file_route):
                # If it is a folder, it is added with empty extension
                data.append([file, "", ""])  # new name and extention empty

    # Create a DataFrame with the data
    df = pd.DataFrame(data, columns=[excel_column_original_name, excel_column_extention, excel_column_new_name])

    def save_excel_template():
        """Write the Excel template and format it."""
        df.to_excel(excel_save_route, index=False)
        modify_excel_dataframe(
            excel_save_route,
            excel_aditional_rows_to_unlock,
            notes_title,
            excel_note1,
            excel_note2,
            excel_note3,
            excel_note4,
            excel_note5,
        )



    ##EXCEL
    # Check if the file already exists
    if os.path.exists(excel_save_route):
        if not ask_replace(file_already_exist_title, file_already_exist_message):
            show_message(file_not_created_selected_title, file_not_created_selected_message)
            # If no replace excel is selected, the execution is aborted.
            exit_if_directly_executed()
        else:
            try:
                save_excel_template()
                show_message(file_replaced_title, file_replaced_message)
            except PermissionError: # If the excel is open.
                show_error(error_text, error_open_file)
                # Abort the execution
                exit_if_directly_executed()
    else:
        try:
            save_excel_template()
            show_message(file_created_title, file_created_message)
        except PermissionError: # If the excel is open.
            show_error(error_text, error_open_file)
            # Abort the execution
            exit_if_directly_executed()
            
            
            

    
    
if __name__ == "__main__":
    main(language)
