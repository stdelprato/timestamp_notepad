import PyInstaller.__main__
import sys
import os

# Get the path of the script to convert
script_path = os.path.abspath("timestamp_notepad.py")

# Check if the script exists
if not os.path.exists(script_path):
    print(f"Error: The script {script_path} does not exist.")
    sys.exit(1)

# Run PyInstaller
PyInstaller.__main__.run([
    script_path,
    '--onefile',
    '--windowed',
    '--name=TimestampNotepad',
    '--add-data=notepad_icon.ico:.',
    '--icon=notepad_icon.ico',
])

print("Executable created successfully!")