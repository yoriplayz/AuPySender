
import pywhatkit
import tkinter as tk
from tkinter import messagebox


def send_message():
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
                "Please enter a message to send."
            )
            return

        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            messagebox.showerror(
                "Invalid Time",
                "Please enter a valid hour (0-23) and minute (0-59)."
            )
            return

        pywhatkit.sendwhatmsg(no, msg, hour, minute)

        messagebox.showinfo(
            "Success",
            "Message scheduling process completed!"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter numeric values for hour and minute."
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Main Window
root = tk.Tk()
root.title("AuPySender")
root.geometry("450x550")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

# Heading
title = tk.Label(
    root,
    text="AuPySender",
    font=("Helvetica", 24, "bold"),
    fg="white",
    bg="#1e1e2e"
)
title.pack(pady=25)

# Phone Number Input
tk.Label(
    root,
    text="Phone Number (+CountryCode):",
    font=("Helvetica", 12),
    fg="white",
    bg="#1e1e2e"
).pack(anchor="w", padx=20)

phone_entry = tk.Entry(
    root,
    font=("Helvetica", 12),
    width=35,
    bg="#6c7086",
    fg="white",
    insertbackground="white"
)
phone_entry.pack(pady=8)

# Message Input
tk.Label(
    root,
    text="Message:",
    font=("Helvetica", 12),
    fg="white",
    bg="#1e1e2e"
).pack(anchor="w", padx=20, pady=(20, 0))

message_text = tk.Text(
    root,
    height=5,
    width=35,
    font=("Helvetica", 12),
    bg="#6c7086",
    fg="white",
    insertbackground="white"
)
message_text.pack(pady=8)

# Time Input
tk.Label(
    root,
    text="Time (24-hour format):",
    font=("Helvetica", 12),
    fg="white",
    bg="#1e1e2e"
).pack(pady=(15, 5))

time_frame = tk.Frame(root, bg="#1e1e2e")
time_frame.pack()

hour_entry = tk.Entry(
    time_frame,
    font=("Helvetica", 12),
    width=8,
    bg="#6c7086",
    fg="white",
    insertbackground="white",
    justify="center"
)
hour_entry.pack(side="left", padx=10)

tk.Label(
    time_frame,
    text=":",
    font=("Helvetica", 12),
    fg="white",
    bg="#1e1e2e"
).pack(side="left")

minute_entry = tk.Entry(
    time_frame,
    font=("Helvetica", 12),
    width=8,
    bg="#6c7086",
    fg="white",
    insertbackground="white",
    justify="center"
)
minute_entry.pack(side="left", padx=10)

# Send Button
send_button = tk.Button(
    root,
    text="Send Message",
    font=("Helvetica", 14, "bold"),
    bg="#4CAF50",
    fg="black",
    activebackground="#45a049",
    width=25,
    height=2,
    relief="flat",
    command=send_message
)
send_button.pack(pady=35)

# Footer
tk.Label(
    root,
    text="Developed by: Yori | Python & PyWhatKit",
    font=("Helvetica", 10),
    fg="white",
    bg="#1e1e2e"
).pack(side="bottom", pady=15)

root.mainloop()
