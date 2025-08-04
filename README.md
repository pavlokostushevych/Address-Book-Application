📄 Wersja polska poniżej – [Przejdź do wersji PL](#pl)

# 🧠 Personal Assistant (Team Project)

A console and GUI-based Personal Assistant app built in Python using [`prompt_toolkit`](https://github.com/prompt-toolkit/python-prompt-toolkit), [`rich`](https://github.com/Textualize/rich), and [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter).  
The project manages contacts, notes, and to-do lists via a modular architecture and offers both terminal and graphical user interfaces.

📦 Installable via [`setuptools`](https://setuptools.pypa.io/en/latest/), with entry points for launching either version.

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
- ✨ Intelligent input analysis: the assistant can suggest the most relevant command based on user input (even if it's incorrect or incomplete).

💾 Data Persistence
- 📦 The program automatically saves data (contacts, notes) upon exit or even in case of a crash, ensuring no user input is lost.
---

## 💡 Project Overview
This project was developed during an 8-day Agile sprint simulating a real-world software development environment. The student team followed professional workflows, applying Scrum methodology with clearly assigned roles and iterative progress.

We used:

🛠 Trello for task management (screenshots available in the [`photos/`](./photos))

💬 Slack for team communication

📞 Zoom, teams for daily stand-up meetings and sprint reviews

My role:
I chose the Scrum Master role, focusing on communication, organizing meetings, task tracking, and ensuring smooth collaboration.
Additionally, I contributed to core features in main.py.
I also worked on bugfixes after integrating the GUI (gui.py), which was developed by the Team Lead.
In my repository, you’ll find a reworked setup.py and newly added entry_points to easily launch either the GUI or console version.

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

## 🎥 Project Presentation & Possible Usage
This repository showcases the design and development of a Personal Assistant application written in Python. You can explore the application in two ways:

📸 Visual Preview
To quickly get a sense of how the application works, check out:

[`photos/`](./photos) — includes screenshots of the GUI and CLI interfaces of the assistant, project management in action on our Trello board — showing how we organized and tracked tasks during development.  
[`goit_project/`](./goit_project) — you can review the source code of the application.

💻 Try It Yourself
If you want to interact with the assistant directly:

Head down to the section ## Getting Started (Windows)

Follow the installation steps to set up the application on your system

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

## 📬 Contact

If you have any questions, feel free to reach out:  

- Email: pavlo.kostushevych@gmail.com  
- LinkedIn: [linkedin.com/in/pavlo-kostushevych-ab364b376](https://www.linkedin.com/in/pavlo-kostushevych-ab364b376/)

---
## PL

# 🧠 Personal Assistant (Projekt zespołowy)

Konsolowa i graficzna aplikacja „Personal Assistant” napisana w Pythonie z użyciem [`prompt_toolkit`](https://github.com/prompt-toolkit/python-prompt-toolkit), [`rich`](https://github.com/Textualize/rich), oraz [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter). 
Projekt zarządza kontaktami, notatkami i listą zadań przy użyciu architektury modułowej, oferując zarówno interfejs terminalowy, jak i graficzny.

📦 Możliwa do zainstalowania przez [`setuptools`](https://setuptools.pypa.io/en/latest/), z punktami wejścia pozwalającymi uruchomić obie wersje.

---

## 🧩 Zaimplementowane funkcje
Ta aplikacja Personal Assistant w Pythonie zawiera następujące funkcje:

👥 Książka kontaktów
- 📇 Przechowywanie kontaktów zawierających:
  - Imię
  - Adres
  - Numer(y) telefonu
  - Email(e)
  - Datę(y) urodzin

- 🎂 Wyświetlanie kontaktów, które mają urodziny w ciągu określonej liczby dni
- ✅ Walidacja poprawności numeru telefonu i adresu email (sprawdzenie regex)
- 🔍 Wyszukiwanie kontaktów po imieniu lub innych polach
- ✏️ Edytowanie istniejących kontaktów
- 🗑️ Usuwanie kontaktów

📝 Menedżer notatek
- 🧾 Tworzenie i przechowywanie notatek tekstowych
- 🔍 Wyszukiwanie notatek po treści
- ✏️ Edytowanie notatek
- 🗑️ Usuwanie notatek
- 🏷️ Dodawanie tagów (słów kluczowych) do notatek
- 🔎 Wyszukiwanie i sortowanie notatek po tagach

📂 Narzędzie sortowania folderów
- 🗃️ Sortowanie plików w wybranym folderze według kategorii:
  - Obrazy
  - Wideo
  - Dokumenty
  - Archiwa
  - Inne

🤖 Inteligentne podpowiedzi komend
- ✨ Analiza wprowadzanych danych: asystent sugeruje najbardziej odpowiednią komendę nawet przy błędnym lub niepełnym wpisie

💾 Trwałość danych
- 📦 Program automatycznie zapisuje dane (kontakty, notatki) przy wyjściu lub nawet w przypadku awarii, zapobiegając ich utracie
---

## 💡 Przegląd projektu
Projekt został zrealizowany podczas 8-dniowego sprintu Agile, symulującego środowisko pracy w rzeczywistym zespole developerskim. Zespół studencki stosował profesjonalne praktyki, w tym metodologię Scrum z jasno określonymi rolami i iteracyjnym postępem pracy.

Wykorzystaliśmy:

🛠 Trello do zarządzania zadaniami (zrzuty ekranu dostępne w [`photos/`](./photos))

💬 Slack do komunikacji zespołowej

📞 Zoom i Teams do codziennych stand-upów i przeglądów sprintów

Moja rola:
Wybrałem rolę Scrum Mastera — odpowiadałem za komunikację, organizację spotkań, śledzenie zadań i zapewnienie płynnej współpracy.
Dodatkowo, współtworzyłem funkcje główne w pliku main.py.
Zajmowałem się również poprawkami błędów po integracji GUI (gui.py), stworzonego przez lidera zespołu.
W moim repozytorium znajdziesz przeprojektowany setup.py oraz nowe entry_points, umożliwiające łatwe uruchamianie wersji GUI lub konsolowej.



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

## 🎥 Project Presentation & Possible Usage
This repository showcases the design and development of a Personal Assistant application written in Python. You can explore the application in two ways:

📸 Visual Preview
To quickly get a sense of how the application works, check out:

[`photos/`](./photos) — includes screenshots of the GUI and CLI interfaces of the assistant, project management in action on our Trello board — showing how we organized and tracked tasks during development.  
[`goit_project/`](./goit_project) — you can review the source code of the application.

💻 Try It Yourself
If you want to interact with the assistant directly:

Head down to the section ## Getting Started (Windows)

Follow the installation steps to set up the application on your system

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

## 📬 Contact

If you have any questions, feel free to reach out:  

- Email: pavlo.kostushevych@gmail.com  
- LinkedIn: [linkedin.com/in/pavlo-kostushevych-ab364b376](https://www.linkedin.com/in/pavlo-kostushevych-ab364b376/)

---
