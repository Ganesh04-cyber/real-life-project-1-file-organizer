Smart File Organizer – Python Automation Project

A real-life Python automation tool that automatically sorts and organizes files into clean, categorized folders — perfect for daily productivity and portfolio.

 Project Description
The Smart File Organizer is a Python-based automation script that helps you clean up messy directories (like Downloads or Desktop) by 
automatically detecting file types and moving them into corresponding folders such as Images, Documents, or Music.

This project is part of a daily job-preparation series focused on Python + Security + Automation with real-world use cases.

Objectives
Automate repetitive and manual file organization tasks.

Showcase Python skills in a real-world scenario.

Demonstrate usage of os, shutil, and pathlib for filesystem manipulation.

Key Features
Auto-detects file types by extension
Creates folders dynamically (if not already present)
Moves files into correct folders without overwriting
Can be run anytime on any folder

Built using only Python’s built-in modules (no external packages)

Technologies Used
Tool	Purpose
pathlib	File path manipulation
os	OS-level directory handling
shutil	Moving files between folders

Folder Structure After Running
Before:

Downloads/
├── photo.jpg
├── resume.pdf
├── music.mp3

After:

Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── resume.pdf
├── Music/
│   └── music.mp3

How It Works
You run the script and input the folder path.

It loops through all files in that folder.

Based on extension, each file is moved into a relevant subfolder.

If the subfolder doesn’t exist, it’s created automatically.

 Code Logic (Simplified)
python
Copy
Edit
file_types = {
    "Images": [".jpg", ".png"],
    "Documents": [".pdf", ".docx"],
    "Music": [".mp3", ".wav"]
}

for file in folder_path.iterdir():
    if file.is_file():
        for folder, extensions in file_types.items():
            if file.suffix.lower() in extensions:
                dest = folder_path / folder
                dest.mkdir(exist_ok=True)
                shutil.move(str(file), dest / file.name)
                break

                
Skills Demonstrated
File and directory automation

Real-time decision-making using if, loops, and conditions

Modular coding using dictionaries for config

Reusable, customizable script logic



 Use Cases
Developers cleaning their Downloads folder

Office workers organizing scanned documents

Freelancers managing project files

Anyone tired of manually dragging files 😅









