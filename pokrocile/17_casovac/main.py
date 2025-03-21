import tkinter as tk
import time


class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Časovač")
        self.root.geometry("400x400")

        self.total_exam_time = 20 * 60  # 20min
        self.part_time = 6 * 60 + 40  # 6:40min
        self.current_part = 1
        self.remaining_time = self.part_time
        self.running = False

        self.time_label = tk.Label(root, text=time.strftime('%H:%M:%S'), font=("Arial", 16))
        self.time_label.pack()

        self.part_label = tk.Label(root, text=f"Část: {self.current_part}", font=("Arial", 24, "bold"))
        self.part_label.pack()

        self.countdown_label = tk.Label(root, text=self.format_time(self.remaining_time), font=("Arial", 32))
        self.countdown_label.pack()

        self.canvas = tk.Canvas(root, width=200, height=200)
        self.canvas.pack()

        self.start_pause_button = tk.Button(root, text="Start/Pause", command=self.toggle_timer)
        self.start_pause_button.pack()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack()

        self.update_clock()
        self.draw_timer()

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def update_clock(self):
        self.time_label.config(text=time.strftime('%H:%M:%S'))
        self.root.after(1000, self.update_clock)

    def update_timer(self):
        if self.running:
            if self.remaining_time > 0:
                self.remaining_time -= 1
            else:
                if self.current_part < 3:
                    self.current_part += 1
                    self.remaining_time = self.part_time
                else:
                    self.running = False
                    return

            self.part_label.config(text=f"Část: {self.current_part}")
            self.countdown_label.config(text=self.format_time(self.remaining_time))
            self.draw_timer()
            self.root.after(1000, self.update_timer)

    def toggle_timer(self):
        self.running = not self.running
        if self.running:
            self.update_timer()

    def reset_timer(self):
        self.running = False
        self.current_part = 1
        self.remaining_time = self.part_time
        self.part_label.config(text=f"Část: {self.current_part}")
        self.countdown_label.config(text=self.format_time(self.remaining_time))
        self.draw_timer()

    def draw_timer(self):
        self.canvas.delete("all")
        angle = (self.remaining_time / self.part_time) * 360
        self.canvas.create_arc(10, 10, 190, 190, start=90, extent=-angle, fill="blue")
        self.canvas.create_oval(60, 60, 140, 140, fill="white")


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
