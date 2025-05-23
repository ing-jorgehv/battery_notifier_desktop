import tkinter as tk



def show_battery_full_alert():
    root = tk.Tk()
    root.title("Battery Full Warning")
    root.overrideredirect(True)
    root.attributes("-topmost", True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 420
    height = 220
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

    canvas = tk.Canvas(root, width=width, height=height, highlightthickness=0)
    canvas.pack()

    # Place frame on top
    frame = tk.Frame(canvas, bg="#add8e6") # light blue
    frame.place(x=10, y=10, width=width - 20, height=height - 20)

    label = tk.Label(
        frame,
        text="🔋 Battery is Full\nPlease unplug the charger.",
        font=("Segoe UI", 14),
        bg="#add8e6"
    )
    label.pack(pady=30)

    ok_button = tk.Button(
        frame,
        text="OK",
        font=("Segoe UI", 12),
        bg="white", 
        fg="black",
        relief="flat",
        activebackground="#A9A9A9", # dark gray
        command=root.destroy
    )
    ok_button.pack(pady=10)

    root.mainloop()
