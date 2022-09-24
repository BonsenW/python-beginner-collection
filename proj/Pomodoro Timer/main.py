import tkinter as tk
import datetime
import winsound

COLOURS = {
    "PINK" : "#e2979c",
    "RED" : "#e7305b",
    "GREEN" : "#9bdeac",
    "LY" : "#f7f5dd",
    "MY" : "#dbd9c3",
    "DY" : "#bab8a6"
}

FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

class App(tk.Tk):
    
    current_reps = 0
    timer = None
    
    def __init__(self):
        super().__init__()
        
        self.title("Pomodoro")
        self.config(padx=100, pady=50, bg=COLOURS["LY"])


        # Create Canvas
        self.canvas = tk.Canvas(width=200, height=224, bg=COLOURS['LY'], highlightthickness=0)
        self.tomato_img = tk.PhotoImage(master=self.canvas, file="tomato.png")
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))


        # Header
        self.header_label = tk.Label(text="Timer", fg=COLOURS["GREEN"], font=(FONT_NAME, 40, "bold"), bg=COLOURS["LY"])


        # Buttons
        self.start_button = tk.Button(text="Start", font=(FONT_NAME, 16, "bold"), bg=COLOURS["MY"], activebackground=COLOURS["DY"], border=0, command=self.start_timer)
        self.reset_button = tk.Button(text="Reset", font=(FONT_NAME, 16, "bold"), bg=COLOURS["MY"], activebackground=COLOURS["DY"], border=0, command=self.reset_timer)


        # Checklists
        self.checkmark_label = tk.Label(fg=COLOURS["GREEN"], font=(FONT_NAME, 15, "bold"), bg=COLOURS["LY"])
        
        self.layout_ui()
        
    def reset_timer(self):
        self.current_reps = 0

        self.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.header_label["text"] = "Timer"
        self.checkmark_label["text"] = ''
    
    def start_timer(self):
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        
        self.current_reps += 1
        if self.current_reps % 8 == 0:
            self.header_label["text"] = "Break"
            self.header_label["fg"] = COLOURS["RED"]
            self.checkmark_label["text"] += '✔'
            self.count_down(long_break_sec)
            self.current_reps = 0
            self.checkmark_label["text"] = ''
        elif self.current_reps % 2 == 0:
            self.header_label["text"] = "Break"
            self.header_label["fg"] = COLOURS["PINK"]
            self.checkmark_label["text"] += '✔'
            self.count_down(short_break_sec)
        else:
            self.header_label["text"] = "Work"
            self.header_label["fg"] = COLOURS["GREEN"]
            self.count_down(work_sec)
        winsound.Beep(1000, 1000)
    
    def count_down(self, count):
        self.canvas.itemconfig(self.timer_text, text=str(datetime.timedelta(seconds=count))[2::])
        if count >= 0:
            self.timer = self.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()

    def layout_ui(self):
        self.canvas.grid(row=1, column=1)
        self.header_label.grid(row=0, column=1)
        self.start_button.grid(row=2,column=0)
        self.reset_button.grid(row=2,column=3)
        self.checkmark_label.grid(row=3, column=1)


if __name__ == "__main__":
    app = App()
    app.mainloop()