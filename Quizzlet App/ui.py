from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzlet")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20,width=400,height=600)


        self.score_label = Label(text="Score:0",font=("Arial",10,"normal"),fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1,padx=(80,0))


        self.canvas = Canvas(width=300,height=250,bg="white",highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=288,
            text="Some Question Text",
            font = ("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)


        true_button_image = PhotoImage(file = "Quizzlet App\images\\true.png")
        self.true_button = Button(image=true_button_image,border=0,highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row = 2,column=0,padx=20)


        false_button_image = PhotoImage(file = "Quizzlet App\images\\false.png")
        self.false_button = Button(image=false_button_image,border=0,highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row = 2,column=1,padx=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score:{self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text = q_text)
        else:
            self.canvas.itemconfig(self.question_text,text = "You have reached the end of the quiz!!!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000,self.get_next_question)