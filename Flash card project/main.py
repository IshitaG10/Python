from tkinter import *
import pandas as pd
import random
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT_SIZE = 35
WORD_FONT_SIZE = 80
FONT_NAME = "Arial"


# ---------------------------- DATA SETUP ------------------------------- #
try:
        df = pd.read_csv("Flash card project\data\\words_to_learn.csv")
        
except FileNotFoundError:
        df = pd.read_csv("Flash card project\data\\french_words.csv")
finally:
        words = df.to_dict(orient="records")
        word = {}
        keys = list(df.columns)
        front_card_title = keys[0]
        back_card_title = keys[1]

# ---------------------------- FLIP CARD ------------------------------- #
def flip_card(word):
    canvas.itemconfig(canvas_image,image = flash_card_back)
    canvas.itemconfig(title_text,text = back_card_title,fill= "white")
    canvas.itemconfig(word_text,text = word[back_card_title],fill= "white")


# ---------------------------- NEXT CARD ------------------------------- #

def next_card():
    global flip_timer,word
    window.after_cancel(flip_timer) #to avoid a flip if we press the next button before the card flips 
    word = random.choice(words)
    canvas.itemconfig(canvas_image,image = flash_card_front)
    canvas.itemconfig(title_text,text = front_card_title,fill = "black")
    canvas.itemconfig(word_text,text = word[front_card_title],fill = "black")
    flip_timer = window.after(3000,flip_card,word) #(ms,function_name,argument to be passed to the function)


# ---------------------------- IS KNOWN ------------------------------- #
def is_known():
    global words
    words.remove(word)
    new_df = pd.DataFrame(words)
    new_df.to_csv("Flash card project\data\words_to_learn.csv",index=FALSE)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
flip_timer =  window.after(3000,func = flip_card)

#flash card
canvas = Canvas(width=850,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
flash_card_front = PhotoImage(file="Flash card project\images\card_front.png")
flash_card_back = PhotoImage(file="Flash card project\images\card_back.png")
canvas_image = canvas.create_image(425,263,image = flash_card_front)
title_text = canvas.create_text(425,110,text="",font=(FONT_NAME,TITLE_FONT_SIZE,"italic"))
word_text = canvas.create_text(425,263,text="",font=(FONT_NAME,WORD_FONT_SIZE,"bold"))
canvas.grid(row=0,column=0,columnspan=2)


#buttons
right_button_image = PhotoImage(file = "Flash card project\images\\right.png")
right_button = Button(image=right_button_image,highlightthickness=0,border=0,command=is_known)
right_button.grid(row=1,column=0)

wrong_button_image = PhotoImage(file = "Flash card project\images\\wrong.png")
wrong_button = Button(image=wrong_button_image,highlightthickness=0,border=0,command=next_card)
wrong_button.grid(row=1,column=1)

#calling function to get first word
next_card()

window.mainloop()