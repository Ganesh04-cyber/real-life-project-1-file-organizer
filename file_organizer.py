import os
import shutil
from pathlib import Path

file_types = {
    "json": [".json"],
    "txt": [".txt"],
    "csv": [".csv"]
}

folder_path = Path(input("Enter folder path: "))

for file in folder_path.iterdir():                                  # Loop through all items in the folder
    if file.is_file():                                                # Only proceed if it's a file
        for folder, extensions in file_types.items():                # Loop through the categories
            if file.suffix.lower() in extensions:                  # Check if file matches extension
                dest = folder_path / folder                       # Create path to destination folder
                dest.mkdir(exist_ok=True)                           # Make the folder if it doesn't exist
                shutil.move(str(file), dest / file.name)           # Move the file
                break                                                  # it will stop the code if folders already exists or else it will proceed
