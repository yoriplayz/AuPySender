# AuPySender

**A simple WhatsApp Message Scheduler built with Python.**

AuPySender is a lightweight desktop application that allows users to schedule WhatsApp messages through a graphical user interface (GUI). Built using Python, Tkinter, and PyWhatKit, it eliminates the need to enter scheduling details through the terminal.

With AuPySender, you can enter a recipient's phone number, compose a message, select a sending time, and let PyWhatKit handle the scheduling process through WhatsApp Web.

## Features

- **Graphical User Interface:** Simple and intuitive desktop interface powered by Tkinter.
- **Phone Number Input:** Supports international phone numbers with country codes.
- **Message Composer:** Multi-line text area for composing messages.
- **Message Scheduling:** Schedule messages using the 24-hour time format.
- **Input Validation:** Validates phone number format, message content, and scheduling time.
- **Error Handling:** Displays notifications for invalid inputs and unexpected errors.
- **Dark Interface:** Minimal dark-themed design with a green action button.
- **Standalone Executable:** Can be packaged into a Windows `.exe` using PyInstaller.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Tkinter | Graphical user interface |
| PyWhatKit | WhatsApp message scheduling |
| PyInstaller | Windows executable packaging |

## Application Preview

<!-- Add screenshots of AuPySender here -->
<img width="942" height="502" alt="Screenshot 2026-11-03 171836" src="https://github.com/user-attachments/assets/7aa2a24e-439f-4128-9136-35b7579ea8da" />
<img width="1912" height="1038" alt="Screenshot 2026-11-03 171516" src="https://github.com/user-attachments/assets/5f72dcd1-9534-4841-aa3c-e5a56b9cc8b7" />

## Installation

### Option 1: Download the Executable

If you don't want to install Python or configure dependencies:

1. Visit the repository's **Releases** section.
2. Download `AuPySender.exe`.
3. Run the executable.

No separate Python installation is required.

### Option 2: Run from Source

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/AuPySender.git
```

**2. Navigate to the project directory**

```bash
cd AuPySender
```

**3. Install dependencies**

```bash
python -m pip install pywhatkit
```

**4. Run the application**

```bash
python main.py
```

## How to Use

1. Launch AuPySender.
2. Enter the recipient's phone number, including the international country code (e.g., `+91`).
3. Compose your WhatsApp message.
4. Enter the desired hour and minute using the 24-hour format.
5. Click **Send Message**.
6. PyWhatKit will open WhatsApp Web and handle the scheduled sending process.

## Building from Source

AuPySender can be converted into a standalone Windows executable using PyInstaller.

**1. Install PyInstaller**

```bash
python -m pip install pyinstaller
```

**2. Generate the executable**

```bash
python -m PyInstaller --clean --noconfirm --onefile --windowed --name AuPySender main.py
```

**3. Locate the executable**

After the build completes, the executable will be available inside:

```text
dist/AuPySender.exe
```

### Optional: Custom Application Icon

To include a custom `.ico` application icon:

```bash
python -m PyInstaller --clean --noconfirm --onefile --windowed --name AuPySender --icon=icon.ico main.py
```

**Note:** Build the executable on Windows for Windows distribution. PyInstaller does not automatically cross-compile executables for different operating systems.

## Project Structure

```text
AuPySender/
│
├── main.py
├── README.md
├── .gitignore
│
├── build/          # Temporary build files
├── dist/           # Generated executable
└── AuPySender.spec # PyInstaller configuration
```

## Requirements

For running from source:

- Python 3.x
- PyWhatKit
- Tkinter
- Active internet connection
- WhatsApp account

For running the standalone executable:

- Windows operating system
- Active internet connection
- WhatsApp account

## Important Notes

- You must be logged into WhatsApp Web.
- Your computer must remain powered on and connected to the internet during scheduling.
- WhatsApp Web must remain accessible to PyWhatKit.
- Scheduling depends on the availability and behaviour of WhatsApp Web.
- A successful scheduling operation does not independently confirm message delivery.
- Use the application responsibly and respect recipients' consent.

## Author

**Yori**

Developed with Python, Tkinter, and PyWhatKit.

---
