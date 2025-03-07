# EditorPerRepo
Open a different editor per repo when opening a repo on GitHub Desktop!

The CLI version can be found here: https://github.com/rynstwrt/EditorPerRepoCLI

<br>

## FEATURES:
- Config to add editors to the GUI
- Support for **glob patterns** and **environment variables** in paths.

<br>

## SETUP:
1. In GitHub Desktop: File > Options > Integrations > Configure custom editor...
2. Set the path to a **pythonw** executable.
    - Running with `pythonw.exe` instead of `python.exe` prevents showing a console window.
3. Set the arguments to the path to the downloaded repo's `main.py` file with a space and `%TARGET_PATH%` after it.
    - Ex: `%HOME%\Documents\GitHub\EditorPerRepo\main.py %TARGET_PATH%`
4. Set up your favorite editors in the `epr-config.json` file.
5. That's it!

<br>

## OPTIONAL CLI ARGUMENTS:
- `--skip-open`: Run EditorPerRepo without opening the selected editor.
- `--ignore-saved`: Run EditorPerRepo without opening the assigned editor for that directory.

<br>

## CONFIG EXAMPLE:
```json
{
    "editors": [
        {
            "name": "Pycharm (x64)",
            "editor_path": "C:/Program Files/JetBrains/*/*/pycharm64.exe"
        },
        {
            "name": "Webstorm (x64)",
            "editor_path": "C:/Program Files/JetBrains/*/*/webstorm64.exe",
            "associated_dirs": [
                "C:\\Users\\ryans\\Dropbox\\OpenSCAD Projects\\8x8-LED-Matrix-Lamp"
            ]
        },
        {
            "name": "Visual Studio Code",
            "editor_path": "%LocalAppData%/Programs/Microsoft VS Code/Code.exe",
            "associated_dirs": [
                "C:/Example/Path/Here",
                "C:/Example/Second/Path/Here"
            ]
        }
    ]
}
```
