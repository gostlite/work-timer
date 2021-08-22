
# ---------------------------- CONSTANTS ------------------------------- #
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #


from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg= YELLOW )


label = Label(text= "Timer", bg = YELLOW, fg=GREEN, font=(FONT_NAME, 50))
label.grid(column=1, row=0)

check_mark = Label(text="✓",  bg =YELLOW, fg=GREEN)
check_mark.grid(column=1, row=2)


def start_timer():

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    global reps
    reps += 1
    # if 1st/ 3rd/5th/7th rep
    if reps % 8 == 0:
        label.config(text= "BREAK", fg= RED)
        count_down(long_break_sec)
    #  if 2nd/4th/6th
    elif reps % 2 == 0:
        label.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)

    else:
        label.config(text="WORK", fg=GREEN)
        count_down(work_sec)

def resett():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="TIMER")
    global reps
    reps = 0

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count < 10:
        count_sec = f"0:{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file= "tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130,  text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# button

start = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=resett)
reset.grid(column=2, row=2)




window.mainloop()