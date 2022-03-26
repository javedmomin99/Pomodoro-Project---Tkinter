import tkinter
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 5
reps= 20
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down_timer(count = 60 * 5)
    global reps
    reps = reps + 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60



    #If it's the 8th Rep:
    if reps % 8 == 0:
        count_down_timer(long_break_sec)
        title_label.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        #If it's 2st/4rd/6th Rep:
        count_down_timer(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        #If it's 1st/3rd/5th/7th Rep:
        count_down_timer(work_sec)
        title_label.config(text="WORK", fg=GREEN)

        


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down_timer(count):
    count_min = math.floor(count / 60)
    # rounds to the largest whole number ex: 4.8 is rounded to 4
    count_sec = count % 60
    # % gives remainder
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down_timer, count-1)
        #1000 means 1000 milliseconds wait time
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark = str(mark) + "✓"
            check_mark.config(text= mark)
        
    


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=50,pady=50,bg=YELLOW)



title_label = tkinter.Label(text="Timer", bg = YELLOW, fg=GREEN,font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1,row=0)

canvas = tkinter.Canvas(width=500, height=500, bg=YELLOW,highlightthickness=0)
# Numbers 200 & 224 are in Pixels
tomato_img = tkinter.PhotoImage(file="tomato.png")
#keyword Arguments are required to be called with same keyword always
canvas.create_image(250,250,image=tomato_img)
#250,250 are x and y co-ordiantes respectively.
# Canvas Image is Half of Canvas Width & Height so that it fits perfectly
timer_text = canvas.create_text(250,265,text="00:00",fill="white",font=(FONT_NAME,38,"bold"))
canvas.grid(column=1,row=1)

start_button = tkinter.Button(text="Start", highlightthickness=0,font=(FONT_NAME, 15, "bold"),command=start_timer)
start_button.grid(column=0,row=2)
reset_button = tkinter.Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 15, "bold"),command=reset_timer)
reset_button.grid(column=2, row=2)
check_mark = tkinter.Label(text="", highlightthickness=0,bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_mark.grid(column=1, row=2)

window.mainloop()