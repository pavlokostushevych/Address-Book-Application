# 🧠 Personal Assistant (Team Project)

A console and GUI-based Personal Assistant app built in Python using [`prompt_toolkit`](https://github.com/prompt-toolkit/python-prompt-toolkit), [`rich`](https://github.com/Textualize/rich), and [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter).  
The project manages contacts, notes, and to-do lists via a modular architecture and offers both terminal and graphical user interfaces.

📦 Installable via [`setuptools`](https://setuptools.pypa.io/en/latest/), with entry points for launching either version.

---

## 💡 Project Overview

This project was developed during an **8-day Agile sprint** simulating a real-world software development environment. The student team followed professional workflows, including Scrum roles and regular collaboration with a technical mentor.

- **My role**:  
  I chose the Scrum Master role, focusing on communication, organizing meetings, task management, and Trello usage.  
  Additionally, I contributed to core features in `main.py`.  
  I also worked on bugfixes after integrating the GUI (`gui.py`), which was written by the Team Lead.  
  In my repository, you can find the reworked `setup.py` configuration and newly created entry points for convenient launching.

---
## Team Repository & My Contributions

The full team project repository is maintained by the Team Lead and can be found here: [Team Repository](https://github.com/Kunandiir/goit_project)  
(My Student GitHub nickname: [rynikk21](https://github.com/rynikk21))

You can track my individual commits and contributions within this team repository using my GitHub nickname.

---

## 📂 Project Structure

- [`goit_project/`](./goit_project) — main Python package with core modules:  
  - [main.py](goit_project/goit_project/main.py) — program entry and core logic
  - [notes.py](goit_project/goit_project/notes.py) — notes management module
  - [gui.py](goit_project/goit_project/gui.py) — graphical user interface code
  - [setup.py](goit_project/setup.py) — installation and packaging configuration

- [`photos/`](./photos) — Photos documenting the project  

---

## 🧩 Implemented Features
This Personal Assistant Python application includes the following features:

👥 Contacts Book
- 📇 Store contacts with:
  - Name
  - Address
  - Phone number(s)
  - Email(s)
  - Birthday(s)

- 🎂 Show contacts with birthdays coming up in a given number of days.
- ✅ Input validation for phone numbers and emails (regex check).
- 🔍 Search contacts by name or other fields.
- ✏️ Edit existing contact records.
- 🗑️ Delete contact records.

📝 Notes Manager
- 🧾 Create and store textual notes.
- 🔍 Search notes by content.
- ✏️ Edit notes.
- 🗑️ Delete notes.
- 🏷️ Add tags (keywords) to notes.
- 🔎 Search and sort notes by tags.

📂 Folder Sorting Tool
- 🗃️ Sort files in a selected folder by category:
  - Images
  - Videos
  - Documents
  - Archives
  - Others

🤖 Smart Command Suggestion
✨ Intelligent input analysis: the assistant can suggest the most relevant command based on user input (even if it's incorrect or incomplete).

---

## Getting Started (Windows)

### Download & Install

1. **Download the project:**

   Clone or download the `goit_project` folder to your local machine.

2. **Navigate to the project folder:**

   Open your terminal (Command Prompt, PowerShell, or Bash) and change directory to the folder containing `setup.py`:

   ```bash
   cd path/to/goit_project
   
3. **Install the project with dependencies:**

    Run the following command to install the package and its dependencies:

   ```bash
   pip install .

### Requirements

- **Python version:** This project was developed and tested with **Python 3.11**. Versions 3.8 and above should work.
- The following Python packages will be installed automatically:
  - `customtkinter`
  - `prompt_toolkit`
  - `rich`


Environment Variables
Make sure the Python scripts' install location is added to your system's PATH environment variable so you can run the commands globally from any terminal.

On Windows, the scripts are typically installed to:

```bash
%LOCALAPPDATA%\Packages\PythonSoftwareFoundation.Python.<version>_qbz5n2kfra8p0\LocalCache\local-packages\Python<version>\Scripts
```

Add this folder to your PATH environment variable if it’s not already there.

Running the Program
After installation, you can launch the program via terminal using the provided commands:

To run the GUI version:
```bash
start_project
```
To run the Console version:
```bash
start_project_console
```
