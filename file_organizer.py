import os
import shutil
from pathlib import Path

file_types = {
    "json": [".json"],
    "txt": [".txt"],
    "csv": [".csv"]
}

folder_path = Path(input("Enter folder path: "))

for file in folder_path.iterdir():
    if file.is_file():
        for folder,extension in file_types.items():
            if file.suffix.lower() in extension:
                dest=folder_path/folder
                dest.mkdir(exist_ok=True)
                shutil.move(str(file),dest/file.name)
                break