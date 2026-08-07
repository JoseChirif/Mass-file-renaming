import subprocess
import sys

def build_exe():
    """This function pack the project into a onefile.exe file
    """
    subprocess.run([
        #onefile
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",
        "--windowed",
        "--clean",
        "--noupx",
        "--collect-all", "ttkbootstrap",
        "--hidden-import", "ttkbootstrap",
        
        # Adding project's folders
        "--add-data", "assets/*;assets",
        "--add-data", "config/*;config",
        "--add-data", "functions/*;functions",
        "--add-data", "instructions/*;instructions",
        "--add-data", "locales/*;locales",
        "--add-data", "src/*;src",
        "--add-data", "LICENSE;.",
        "--add-data", "README.md;.",
        
        # Adding specific files
        "--add-data", "instructions/styles/styles.css;instructions/styles",
        "--add-data", "instructions/pictures/1 - Move to folder.png;instructions/pictures",
        "--add-data", "instructions/pictures/2 - Main menu.png;instructions/pictures",
        "--add-data", "instructions/pictures/3 - excel template.png;instructions/pictures",
        "--add-data", "instructions/pictures/4 - Flash fill excel.gif;instructions/pictures",
        "--add-data", "instructions/pictures/5 - renaming.png;instructions/pictures",
        "--add-data", "instructions/pictures/6 - options to modify names.png;instructions/pictures",
        
        # icon, name and file to run in .exe
        "--icon", "assets/icon.ico",
        "--name", "0 rename",
        "run.py"
    ])

if __name__ == "__main__":
    build_exe()
