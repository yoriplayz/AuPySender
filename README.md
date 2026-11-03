# AuPySender

**A lightweight WhatsApp Message Scheduler built with Python.**

AuPySender is a desktop application that allows users to schedule WhatsApp messages through a graphical user interface (GUI). Built using Python, Tkinter, and PyWhatKit, it provides a simple alternative to entering scheduling details through the terminal.

With AuPySender, you can enter a recipient's phone number, compose a message, select a sending time, and let PyWhatKit handle the scheduling process through WhatsApp Web.

## Features

- **Graphical User Interface:** Clean and intuitive desktop interface built with Tkinter.
- **Catppuccin Mocha Theme:** A modern dark interface featuring the Catppuccin Mocha colour palette.
- **Live Digital Clock:** Displays the current system time and date, updating every second.
- **Phone Number Input:** Supports international phone numbers with country codes.
- **Message Composer:** Multi-line text area for composing WhatsApp messages.
- **Message Scheduling:** Schedule messages using the 24-hour time format.
- **Status Indicator:** Real-time application status displaying Waiting, Sending, Completed, or Error.
- **Background Processing:** Uses Python threading to keep the GUI responsive while PyWhatKit processes the scheduled message.
- **Input Validation:** Validates phone number format, message content, and scheduling time.
- **Error Handling:** Displays notifications for invalid inputs and unexpected errors.
- **Standalone Executable:** Can be packaged into a Windows `.exe` using PyInstaller.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Tkinter | Graphical user interface |
| PyWhatKit | WhatsApp message scheduling |
| Threading | Background processing |
| Queue | Communication between background thread and GUI |
| PyInstaller | Windows executable packaging |

## Application Preview

<!-- Add screenshots of AuPySender here -->
<img width="941" height="1034" alt="Screenshot 2026-11-03 190226" src="https://github.com/user-attachments/assets/4fd6293a-0348-4594-9477-15316ef7efc6" />
<img width="1911" height="1036" alt="Screenshot 2026-11-03 190121" src="https://github.com/user-attachments/assets/313adabd-d767-44e5-9f77-81a166327a83" />


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
6. AuPySender will process the scheduled message through PyWhatKit and WhatsApp Web.
7. Monitor the application status indicator to see the current processing state.

### Status Indicators

| Status | Colour | Description |
|---|---|---|
| Waiting | Yellow | A message is scheduled and waiting for its sending time. |
| Sending | Blue | The scheduled sending time has been reached. |
| Completed | Green | PyWhatKit has finished processing without raising an exception. |
| Error | Red | An exception occurred during processing. |

**Note:** The Sending indicator is triggered by the scheduled time rather than direct WhatsApp delivery information. Completed indicates successful execution of the PyWhatKit function, not confirmed message delivery.

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
├── build/                  # Temporary PyInstaller build files
├── dist/                   # Generated executable
└── AuPySender.spec         # PyInstaller configuration
```

## Requirements

**For running from source:**

- Python 3.x
- PyWhatKit
- Tkinter
- Active internet connection
- WhatsApp account

**For running the standalone executable:**

- Windows operating system
- Active internet connection
- WhatsApp account

## Important Notes

- You must be logged into WhatsApp Web.
- Your computer must remain powered on and connected to the internet during scheduling.
- WhatsApp Web must remain accessible to PyWhatKit.
- The application currently supports scheduling one message at a time.
- Scheduling is currently limited to a future time on the same day.
- The status indicator reflects the application's processing state, not confirmed WhatsApp delivery.
- Scheduling depends on the availability and behaviour of WhatsApp Web.
- Use the application responsibly and respect recipients' consent.


## Author

**Yori**

Developed with Python, Tkinter, and PyWhatKit.

---
