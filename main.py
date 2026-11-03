
import pywhatkit
import tkinter as tk
from tkinter import messagebox
import threading
import queue
from datetime import datetime



# CATPPUCCIN MOCHA THEME COLORS


BASE = "#1e1e2e"
MANTLE = "#181825"
SURFACE0 = "#313244"
SURFACE1 = "#45475a"

TEXT = "#cdd6f4"
SUBTEXT = "#bac2de"

GREEN = "#a6e3a1"
BLUE = "#89b4fa"
YELLOW = "#f9e2af"
RED = "#f38ba8"
MAUVE = "#cba6f7"



# FUNCTIONS


result_queue = queue.Queue()
job_active = False


def update_clock():
    now = datetime.now()

    clock_label.config(text=now.strftime("%H:%M:%S"))
    date_label.config(text=now.strftime("%A, %B %d, %Y"))

    root.after(1000, update_clock)


def update_status(status, color):
    status_label.config(
        text=f"●  {status}",
        fg=color
    )


def mark_sending():
    if job_active:
        update_status("Sending...", BLUE)


def send_message():

    global job_active

    no = phone_entry.get().strip()
    msg = message_text.get("1.0", tk.END).strip()

    try:
        hour = int(hour_entry.get())
        minute = int(minute_entry.get())

        if not no.startswith("+"):
            messagebox.showerror(
                "Invalid Phone Number",
                "Please enter a valid phone number with country code (e.g. +91)."
            )
            return

        if not msg:
            messagebox.showerror(
                "Empty Message",
                "Please enter a message."
            )
            return

        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            messagebox.showerror(
                "Invalid Time",
                "Please enter a valid hour (0-23) and minute (0-59)."
            )
            return

        now = datetime.now()

        target_time = now.replace(
            hour=hour,
            minute=minute,
            second=0,
            microsecond=0
        )

        if target_time <= now:
            messagebox.showerror(
                "Invalid Time",
                "Please enter a future time for scheduling the message."
            )
            return

        if job_active:
            messagebox.showwarning(
                "Job Already Active",
                "A message is already scheduled. Please wait for it to complete."
            )
            return

        job_active = True
        send_button.config(state="disabled")

        update_status("Waiting", YELLOW)

        delay = (target_time - now).total_seconds()

        def worker():
            try:
                pywhatkit.sendwhatmsg(
                    no, msg, hour, minute
                )

                result_queue.put(("success", None))

            except Exception as e:
                result_queue.put(("error", str(e)))

        threading.Thread(
            target=worker,
            daemon=True
        ).start()

        root.after(
            int(delay * 1000),
            mark_sending
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter numeric values for hour and minute."
        )


def check_result():

    global job_active

    try:
        result, error = result_queue.get_nowait()

        job_active = False
        send_button.config(state="normal")

        if result == "success":

            update_status("Completed", GREEN)

            messagebox.showinfo(
                "Completed",
                "PyWhatKit has completed the message sending process."
            )

        else:

            update_status("Error", RED)

            messagebox.showerror(
                "Error",
                f"An error occurred during the message sending process:\n{error}"
            )

    except queue.Empty:
        pass

    root.after(200, check_result)



# MAIN WINDOW


root = tk.Tk()

root.title("AuPySender")
root.geometry("500x750")
root.resizable(False, False)
root.configure(bg=BASE)



# HEADING


title = tk.Label(
    root,
    text="AuPySender",
    font=("Helvetica", 24, "bold"),
    fg=MAUVE,
    bg=BASE
)
title.pack(pady=(25, 5))

subtitle = tk.Label(
    root,
    text="Automated WhatsApp Message Sender",
    font=("Helvetica", 14),
    fg=SUBTEXT,
    bg=BASE
)
subtitle.pack()



# CLOCK AND DATE


clock_frame = tk.Frame(
    root,
    bg=MANTLE,
    highlightbackground=SURFACE0,
    highlightthickness=1
)
clock_frame.pack(
    pady=20,
    padx=35,
    fill="x"
)

clock_label = tk.Label(
    clock_frame,
    text="00:00:00",
    font=("Helvetica", 32, "bold"),
    fg=GREEN,
    bg=MANTLE
)
clock_label.pack(pady=(15, 0))

date_label = tk.Label(
    clock_frame,
    text="Loading Date...",
    font=("Helvetica", 14),
    fg=SUBTEXT,
    bg=MANTLE
)
date_label.pack(pady=(0, 15))



# INPUT SECTION


input_frame = tk.Frame(root, bg=BASE)
input_frame.pack(padx=45, fill="x")


def create_label(text):
    return tk.Label(
        input_frame,
        text=text,
        font=("Helvetica", 12),
        fg=SUBTEXT,
        bg=BASE
    )


def create_entry(parent, width=35):
    return tk.Entry(
        parent,
        font=("Helvetica", 12),
        width=width,
        bg=SURFACE0,
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat",
        highlightthickness=1,
        highlightbackground=SURFACE1,
        highlightcolor=MAUVE
    )


# Phone Number Input

create_label(
    "Phone Number (+country code):"
).pack(anchor="w")

phone_entry = create_entry(input_frame)
phone_entry.pack(fill="x", pady=(7, 17), ipady=7)


# Message Input

create_label("Message:").pack(anchor="w")

message_text = tk.Text(
    input_frame,
    height=4,
    font=("Helvetica", 12),
    bg=SURFACE0,
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat",
    wrap="word",
    highlightthickness=1,
    highlightbackground=SURFACE1,
    highlightcolor=MAUVE
)
message_text.pack(fill="x", pady=(7, 17))


# Time Input

create_label(
    "Scheduled Time (24-hour format):"
).pack(anchor="w")

time_frame = tk.Frame(input_frame, bg=BASE)
time_frame.pack(anchor="w", pady=10)

hour_entry = create_entry(time_frame, 8)
hour_entry.pack(side="left", ipady=6)

tk.Label(
    time_frame,
    text=" : ",
    font=("Helvetica", 12),
    fg=SUBTEXT,
    bg=BASE
).pack(side="left", padx=8)

minute_entry = create_entry(time_frame, 8)
minute_entry.pack(side="left", ipady=6)



# STATUS INDICATOR


status_frame = tk.Frame(
    root,
    bg=MANTLE,
    highlightbackground=SURFACE0,
    highlightthickness=1
)
status_frame.pack(
    fill="x",
    padx=45,
    pady=(15, 10)
)

tk.Label(
    status_frame,
    text="MESSAGE STATUS",
    font=("Helvetica", 9, "bold"),
    fg=SUBTEXT,
    bg=MANTLE
).pack(side="left", padx=15, pady=12)

status_label = tk.Label(
    status_frame,
    text="●  Waiting",
    font=("Helvetica", 11, "bold"),
    fg=YELLOW,
    bg=MANTLE
)
status_label.pack(side="right", padx=15)



# SEND BUTTON


send_button = tk.Button(
    root,
    text="Send Message",
    font=("Helvetica", 14, "bold"),
    bg=GREEN,
    fg=BASE,
    activebackground=GREEN,
    activeforeground=BASE,
    width=30,
    height=2,
    relief="flat",
    cursor="hand2",
    command=send_message
)
send_button.pack(pady=20)



# FOOTER


tk.Label(
    root,
    text="Developed by Yori",
    font=("Helvetica", 10, "bold"),
    fg=MAUVE,
    bg=BASE
).pack(side="bottom", pady=(0, 5))

tk.Label(
    root,
    text="Python  |  Tkinter  |  PyWhatKit",
    font=("Helvetica", 9),
    fg=SUBTEXT,
    bg=BASE
).pack(side="bottom", pady=(0, 15))



# START APPLICATION


update_clock()
check_result()

root.mainloop()
