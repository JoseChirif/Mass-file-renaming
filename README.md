<h1> <img src="https://raw.githubusercontent.com/JoseChirif/Mass-file-renaming-with-excel/refs/heads/main/assets/icon.png" width="20" height="20" loading="lazy"/>  MASS FILE RENAMING WITH EXCEL </h1>


Generate an automatic excel template with the name of all files in the same folder of your project. Then, rename all of them with one click (as the new value you assing in the excel).

![Mass file renaming intro](https://github.com/user-attachments/assets/a83851ec-b4ee-43c1-a433-60317cde5f2f)

  <!--- Badges /> --->
<p align="center">
  <img src="https://img.shields.io/github/languages/top/JOSECHIRIF/Mass-file-renaming" alt="Languages" loading="lazy"/>
  &nbsp;
  <img src="https://img.shields.io/badge/python-3.11.5-blue" alt="Python version" loading="lazy"/>
  &nbsp;
  <img src="https://img.shields.io/github/license/JoseChirif/Mass-file-renaming-with-excel" alt="License" loading="lazy"/>
  &nbsp;
  <img src="https://img.shields.io/github/release/JoseChirif/Mass-file-renaming-with-excel" alt="release" loading="lazy"/>
</p>

<br>

# Table of contents
- [Video instructions](#%EF%B8%8F-video-instructions)
- [Setup](#%EF%B8%8F-setup)
- [Languages-instructions](#-languages-instructions)
- [Instructions](#-instructions)
- [Documentation and colaboration](#%EF%B8%8F-documentation-and-collaboration)
- [Thanks](#thanks-)
- [Author](#%EF%B8%8F-author)
<br><br>


# ▶️ Video instructions

Check the instruction guide on YouTube 🎬:
- **[English](https://youtu.be/rBNrmsQ4fyY?si=wv__NWci72Ke8G9l&t=63)**.
- **[Español](https://youtu.be/_Wgyd-unk2c?si=m4rJ2b2gfxsuI9q5&t=62)**. 

<br>
It covers the **📑 execution**, which can be found below in this README.
<br><br>


# 🛠️ SETUP

### 1. Download

<!-- Option a: Download the last release -->
<details>
  <summary>
    Option a: Download the last release
  </summary>
  <br>

  <ol>
    <li>Download the last release.rar
      <table>
        <tr>
        <td><img src="https://github.com/user-attachments/assets/7beb6303-cdca-432b-9ffd-0bb4ac70c0b3" loading="lazy"/></td>
        <td><img src="https://github.com/user-attachments/assets/4944850f-5813-4b2b-8070-185721ad348d" loading="lazy"/></td>
        </tr>
      </table>
    </li>
    <li>Extract the .rar program
    </li>
  </ol>

</details>
<br>
<!-- Option a: Download the last release:END -->


<!-- Option b: Clone the repository -->
<details>
  <summary>
    Option b: Clone the repository
  </summary>
  <br>

  <ol>
    <li>Clone the repository with the command: <pre><code>git clone https://github.com/JoseChirif/Mass-file-renaming-with-excel.git </code></pre>
    </li>

  </ol>

</details>
<br>
<!-- Option b: Clone the repository:END -->





### 2. Install requirements

<ol>
 <li> Install virtual environment with command <pre><code>python -m venv venv</code></pre> </li>

<li> Activate the virtual environment:
  <ol> On <strong>Windows</strong>
  <pre><code>venv\Scripts\activate</code></pre></ol> 
  <ol> On <strong>Mac/Linux</strong>
  <pre><code>source venv/bin/activate</code></pre></ol> 
</li>

<li> Install dependencies from requirements.txt: <pre><code>pip install -r requirements.txt</code></pre>  (check that your venv is active). </li>

</ol>
<br>



### 3. Execute
  
<!-- Option a: Make a onefile.exe file - RECOMMENDED (Click here):START -->
<details>
  <summary>
    Option a: Make a onefile.exe file - RECOMMENDED (Click here)
  </summary>
  <br>

  <ol>
    <li>Run: <pre><code>python build_exe.py</code></pre>
      or Run: <pre><code>pyinstaller --onefile --windowed --clean --noupx `
  --add-data "assets/*;assets" `
  --add-data "config/*;config" `
  --add-data "functions/*;functions" `
  --add-data "instructions/*;instructions" `
  --add-data "locales/*;locales" `
  --add-data "src/*;src" `
  --add-data "LICENSE;." `
  --add-data "README.md;." `
  --add-data "instructions/styles/styles.css;instructions/styles" `
  --add-data "instructions/pictures/1 - Move to folder.png;instructions/pictures" `
  --add-data "instructions/pictures/2 - Main menu.png;instructions/pictures" `
  --add-data "instructions/pictures/3 - excel template.png;instructions/pictures" `
  --add-data "instructions/pictures/4 - Flash fill excel.gif;instructions/pictures" `
  --add-data "instructions/pictures/5 - renaming.png;instructions/pictures" `
  --add-data "instructions/pictures/6 - options to modify names.png;instructions/pictures" `
  --icon "assets/icon.ico" `
  --name "0 rename.exe" `
  "run.py"</code></pre>
    </li><br>

  <li>Then a "dist" folder will be created in the project's directory, containing a "0 rename.exe" folder. Inside it, you will find the .exe file and the "_internal" folder.
    <img src="https://github.com/user-attachments/assets/06193611-8f98-4721-812a-641d40ff30a8" alt="dist folder" loading="lazy">
  </li>

  </ol>

</details>
<br>
<!-- Option a: Make a onefile.exe file - RECOMMENDED (Click here):END -->



<!-- Option b: Make a .exe file with dependencies (Click here):START -->
<details>
  <summary>
    Option b: Make a .exe file with dependencies (Click here)
  </summary>
  <br>

  <ol>
    <li>Run: <pre><code>pyinstaller --windowed --clean --noupx `
  --add-data "assets/*;assets" `
  --add-data "config/*;config" `
  --add-data "functions/*;functions" `
  --add-data "instructions/*;instructions" `
  --add-data "locales/*;locales" `
  --add-data "src/*;src" `
  --add-data "LICENSE;." `
  --add-data "README.md;." `
  --add-data "instructions/styles/styles.css;instructions/styles" `
  --add-data "instructions/pictures/1 - Move to folder.png;instructions/pictures" `
  --add-data "instructions/pictures/2 - Main menu.png;instructions/pictures" `
  --add-data "instructions/pictures/3 - excel template.png;instructions/pictures" `
  --add-data "instructions/pictures/4 - Flash fill excel.gif;instructions/pictures" `
  --add-data "instructions/pictures/5 - renaming.png;instructions/pictures" `
  --add-data "instructions/pictures/6 - options to modify names.png;instructions/pictures" `
  --icon "assets/icon.ico" `
  --name "0 rename.exe" `
  "run.py"</code></pre>
    </li><br>

  <li>Then the folder "dist" will be created in the project's folder. Inside you´ll find other folder with the project name´s and there is the .exe file with the folder "_internal".
    <img src="https://github.com/user-attachments/assets/b7ba0f73-ece8-4447-b1a2-9da60a013e75" alt="dist folder with dependecies" loading="lazy">
  </li>
  <li>Move and keep .exe file with the folder "_internal" together all the time. <strong>The .exe file won't work if the "_internal" folder is not in the same directory.</strong></li>

  </ol>

</details>
<br>
<!-- Option b: Make a .exe file with dependencies (Click here):END -->




<!-- Option c: Execute from python (Click here):START -->
<details>
  <summary>
    Option c: Execute from python (Click here)
  </summary>
  <br>

  <ol>
    <li>Execute run.py to enter the main menu: 
      <pre><code>python run.py</code></pre>
    </li><br>
    <li><p><strong>Scripts will modify the name of files in project's parent directory instead of where the executable is.</strong></p></li>
    <img src="https://github.com/user-attachments/assets/5550e35f-2d79-4afd-bb6a-b61d27045e82" alt="father's directory" loading="lazy">

  </ol>
  

    
</details>
<br>
<!-- Option c: Execute from python (Click here):END -->    



# 🌐 LANGUAGES (instructions):
- [Instructions in **ENGLISH** (click here)](#-instructions)

- [Instrucciones en **ESPAÑOL** (click here)](https://github.com/JoseChirif/Mass-file-renaming/blob/main/instructions/Instructions%20-%20es.md)

<br>

# 📑 INSTRUCTIONS
  1. Move the executable to the folder where the files you want to modify are located.
    ![move_to_folder](https://github.com/user-attachments/assets/a186ba66-b2f7-452f-8797-4f054907d76f)
    **If you created the folder "_internal", move it together.**

  2. With the main menu open you can run all scripts.
    ![Main menu](https://github.com/user-attachments/assets/74ce9fb0-3c13-4362-8180-7c721d530cb4)

  3. The first button will create an excel with the name of all files and folders of the folder where it is.
    ![excel template](https://github.com/user-attachments/assets/c43eb533-498d-46a5-87d3-1ab98e0f8348)

  4. Fill column C of the excel with new names (or leave it empty if you don't wanna change the name).
    ![Flash fill excel](https://github.com/user-attachments/assets/ec5e8c1a-dc87-49f7-bff6-abe98b32a57c)
  >    **Tips:** 
  >    - If there is a regex, made 2 or 3 examples and use excel flash fill.
  >    - If you want to unlock the sheet to use more columns, click on the 3rd button of the main menu does it.

  5. The second button will change the original name of all files with the new name assings in the column C of the excel.
    ![renaming](https://github.com/user-attachments/assets/e8aa9663-363b-4297-aa6f-55cae6d83c77)


  **You have 2 options:** <br>
    ![options to modify names](https://github.com/user-attachments/assets/8d4136fe-5dc2-43c5-875a-fc729e16124d) 
  - Option 1: Made a new folder (with the same name as the project) and copy all the files with the new name.
  - Option 2: Overwrite the files with the new names.

  Choose the option that you prefeer.


**WELL DONE, files has been renamed successfully!**


# 🗃️ Documentation and collaboration
**📚 For detailed documentation and collaboration guidelines, please visit the [Wiki!](https://github.com/JoseChirif/Mass-file-renaming-with-excel/wiki) <br>**
The [Wiki](https://github.com/JoseChirif/Mass-file-renaming-with-excel/wiki) contains everything you need to get started and contribute effectively. Your support and collaboration are greatly appreciated! 🚀✨


# Thanks! 👏
✨ Thank you for checking out this project! If you found it useful, feel free to leave a ⭐ on the repository.

<br>

# ✍️ Author
[@Jose Chirif](https://github.com/JoseChirif)

## 🚀 About me
I'm an Industrial Engineer specialized in process optimization, business intelligence, and Applied Artificial Intelligence. I focus on developing AI-driven solutions and data science tools to automate complex analytical workflows and enhance decision-making.

[Porfolio - Network - Contact](https://linktr.ee/jchirif)


<br>

### ❤️ Support me
If you enjoy my work and want to support me, feel free to donate through the links below. Your support means a lot!

<p align="center">
    <a href="https://buymeacoffee.com/Jchirif" target="_blank">
        <img alt="Buy Me a Tea" src="https://img.shields.io/badge/Buy%20Me%20a%20Tea-☕-586DE0?style=for-the-badge&labelColor=586DE0">
    </a>
    &nbsp;    &nbsp;  &nbsp;  
    <a href="https://paypal.me/JChirif" target="_blank">
        <img alt="Paypal" src="https://img.shields.io/badge/Donate%20via%20PayPal-❤️-FF9900?style=for-the-badge&logo=paypal&labelColor=FF9900">
    </a>
</p>

