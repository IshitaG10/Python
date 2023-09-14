from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#378805"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
   window.after_cancel(timer)
   label.config(text= "Timer",fg=GREEN)
   canvas.itemconfig(timer_text,text =  "00:00")
   check_mark.config(text="")
   global reps
   reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
   global reps
   reps+=1
   
   work_sec = WORK_MIN*60
   short_break_sec = SHORT_BREAK_MIN*60
   long_break_sec = LONG_BREAK_MIN*60

   if reps % 8 == 0:
      count_down(long_break_sec)
      label.config(text="Break",fg = RED)
   
   elif reps % 2 == 0:
      count_down(short_break_sec)
      label.config(text="Break",fg=PINK)

   else:
      count_down(work_sec)
      label.config(text="Work",fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
       count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
     timer = window.after(1000,count_down,count-1)
    else:
       start_timer()
       marks = ""
       work_session = math.floor(reps/2)
       for _ in range(work_session):
          marks+= "✔"
       check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=80,pady=50,bg=YELLOW)

label = Label(text="Timer",font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW)
label.grid(row=0,column=1)


canvas = Canvas(height=250,width=270,bg = YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="pomodoro\\tomato.png")
canvas.create_image(128,112,image = tomato_img)
timer_text = canvas.create_text(128,125,text="00:00",fill="white",font=(FONT_NAME,22,"bold"))
canvas.grid(row=1,column=1)


start_button = Button(text="Start",font=(FONT_NAME,15,"bold"),command=start_timer)
start_button.grid(row = 2, column=0)

reset_button = Button(text="Reset",font=(FONT_NAME,15,"bold"),command=reset_timer)
reset_button.grid(row = 2, column=2)

check_mark = Label(fg=GREEN,font=(15),bg=YELLOW)
check_mark.grid(row = 3, column=1)
check_mark.config(pady=20)
window.mainloop()