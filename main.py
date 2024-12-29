from tkinter import *
from PIL import Image, ImageTk
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer_running = None

# ---------------------------- TIMER MECHANISM ------------------------------- #
def countdown(count):
    global reps
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_running
        timer_running = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)

def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- RESET TIMER ------------------------------- #
def reset_timer():
    window.after_cancel(timer_running)
    canvas.itemconfig(timer, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(
    text="Timer",
    fg=GREEN,
    bg=YELLOW,
    font=(FONT_NAME, 50, "bold"),
    pady=10
)
title_label.pack()

img = Image.open("tomato.png")
pic = ImageTk.PhotoImage(img)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=pic)
timer = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

check_marks = Label(
    text="",
    fg=GREEN,
    bg=YELLOW,
    font=(FONT_NAME, 20, "bold"),
    pady=10
)
check_marks.pack()

button_frame = Frame(window, bg=YELLOW)
button_frame.pack(fill=BOTH, pady=20)

start_button = Button(
    button_frame,
    text="Start",
    font=(FONT_NAME, 10, "bold"),
    bg=GREEN,
    fg="white",
    padx=10,
    pady=5,
    highlightthickness=0,
    border=0,
    command=start_timer
)
start_button.pack(side=LEFT, padx=(50, 20))

reset_button = Button(
    button_frame,
    text="Reset",
    font=(FONT_NAME, 10, "bold"),
    bg=PINK,
    fg="white",
    padx=10,
    pady=5,
    highlightthickness=0,
    border=0,
    command=reset_timer
)
reset_button.pack(side=RIGHT, padx=50)

window.mainloop()